import csv, json, html

INPUT = "data/sample_200_PRs.csv"
OUTPUT = "data/prs.jsonl"

with open(INPUT, encoding="utf-8-sig") as f, open(OUTPUT, "w", encoding="utf-8") as out:
    count = 0
    for row in csv.DictReader(f):
        desc = (row["body"] or "").strip() or "(no description)"
        text = (
            f"<b>Title:</b> {html.escape(row['title'])}<br><br>"
            f"<b>Description:</b><br>{html.escape(desc).replace(chr(10), '<br>')}<br><br>"
            f"<b>Refactoring type:</b> {html.escape(row['refactoring_type'])}<br><br>"
            f"<a href='{row['html_url']}' target='_blank'>Open PR on GitHub</a>"
        )
        out.write(json.dumps({"id": row["id"], "text": text}) + "\n")
        count += 1

print(f"Done: {count} PRs written")
