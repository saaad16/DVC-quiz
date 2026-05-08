import csv

with open("data/sample.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

processed = [r for r in rows if int(r["score"]) > 80]

with open("processed.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id","name","score"])
    writer.writeheader()
    writer.writerows(processed)

print(f"Processed {len(processed)} of {len(rows)} rows")
