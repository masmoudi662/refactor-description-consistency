import csv, json, html

INPUT = "data/masmoudi_50_PRs.csv"
OUTPUT = "data/prs.jsonl"

with open(INPUT, encoding="utf-8-sig") as f, open(OUTPUT, "w", encoding="utf-8") as out:
    count = 0
    for row in csv.DictReader(f):
        pr_id = row.get("id") or row.get("pr_id")
        text = (
            f"<b>Title:</b> {html.escape(row['title'])}<br><br>"
            f"<a href='{row['html_url']}' target='_blank'>Open PR on GitHub</a><br><br>"
            f"Not sure how to label? <a href='/media/instructions.html' target='_blank'>Read the annotation guidelines</a>"
        )
        out.write(json.dumps({"id": pr_id, "text": text}) + "\n")
        count += 1

print(f"Done: {count} PRs written")
