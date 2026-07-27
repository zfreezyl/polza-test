import csv
import re

CSV_FILE = "tsk4.csv"
CLAUDE_OUTPUT = "claude_output2.txt"
OUTPUT_CSV = "tsk4_personalized.csv"


def main():
    # Read Claude's responses
    with open(CLAUDE_OUTPUT, "r", encoding="utf-8") as f:
        text = f.read()

    # Parse responses
    responses = {}
    pattern = r"COMPANY (\d+):\s*(.+?)(?=COMPANY|\Z)"
    matches = re.findall(pattern, text, re.DOTALL)
    for num, fact in matches:
        responses[int(num)] = fact.strip()

    # Read companies
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Add personalization
    for i, row in enumerate(rows):
        row["Персонализация"] = responses.get(i + 1, "NOT FOUND")

    # Write output
    fieldnames = list(rows[0].keys())
    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Done. Saved to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()