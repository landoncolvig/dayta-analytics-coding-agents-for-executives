#!/usr/bin/env python3
"""Generate a BigQuery data dictionary for a project (schema only, no data values).

Writes DATA_DICTIONARY.md (for humans and the agent) and schema.json (machine-readable):
every dataset, table, row count, and column (name, type, mode, description). It reads
metadata only and never selects row values, so no PII leaves the warehouse.

Usage:
  generate_data_dictionary.py --project PROJECT --key /path/service-account.json --out DIR [--prefer modeled]
"""
import argparse, json, os, sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--key", required=True, help="service-account key file")
    ap.add_argument("--out", required=True)
    ap.add_argument("--prefer", default="modeled",
                    help="dataset to list first and label as the clean layer")
    a = ap.parse_args()

    from google.cloud import bigquery
    from google.oauth2 import service_account
    creds = service_account.Credentials.from_service_account_file(a.key)
    c = bigquery.Client(project=a.project, credentials=creds)

    datasets = sorted((d.dataset_id for d in c.list_datasets(a.project)),
                      key=lambda x: (x != a.prefer, x))  # preferred dataset first

    out = {"project": a.project, "datasets": []}
    for ds in datasets:
        node = {"dataset": ds, "tables": []}
        try:
            tables = list(c.list_tables(ds))
        except Exception as e:
            node["error"] = str(e)[:140]
            out["datasets"].append(node)
            continue
        for t in tables:
            try:
                tb = c.get_table(t.reference)  # metadata only
            except Exception as e:
                node["tables"].append({"table": t.table_id, "error": str(e)[:140]})
                continue
            node["tables"].append({
                "table": tb.table_id,
                "type": tb.table_type,
                "rows": tb.num_rows,
                "description": tb.description or "",
                "columns": [{"name": f.name, "type": f.field_type, "mode": f.mode,
                             "description": f.description or ""} for f in tb.schema],
            })
        out["datasets"].append(node)

    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "schema.json"), "w") as fh:
        json.dump(out, fh, indent=2, default=str)

    md = [f"# Data dictionary, {a.project}", "",
          "Schema only, no data values. The live schema is the source of truth; "
          "refresh this file when tables change.", "",
          "Datasets: " + ", ".join(d["dataset"] for d in out["datasets"]), ""]
    for d in out["datasets"]:
        md.append(f"## {d['dataset']}")
        if d.get("error"):
            md += [f"_could not read: {d['error']}_", ""]
            continue
        for t in d["tables"]:
            if t.get("error"):
                md += [f"### {d['dataset']}.{t['table']}  _error: {t['error']}_", ""]
                continue
            ttype = t.get("type") or "TABLE"
            if ttype == "VIEW":
                count = "view"
            elif isinstance(t.get("rows"), int):
                count = f"{t['rows']:,} rows"
            else:
                count = ttype.lower()
            md.append(f"### {d['dataset']}.{t['table']}  ({count})")
            if t["description"]:
                md.append(t["description"])
            md += ["", "| column | type | description |", "|---|---|---|"]
            for col in t["columns"]:
                mode = "" if col["mode"] in ("NULLABLE", "", None) else f" {col['mode']}"
                desc = (col["description"] or "").replace("|", "\\|").replace("\n", " ")
                md.append(f"| `{col['name']}` | {col['type']}{mode} | {desc} |")
            md.append("")
    with open(os.path.join(a.out, "DATA_DICTIONARY.md"), "w") as fh:
        fh.write("\n".join(md))

    print(f"wrote DATA_DICTIONARY.md + schema.json to {a.out} "
          f"({len(out['datasets'])} datasets)")


if __name__ == "__main__":
    main()
