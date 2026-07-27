import csv

CSV_FILE = "collection.csv"
OUTPUT_FILE = "prompts_for_claude.txt"


def main():
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        for i, row in enumerate(rows):
            company = row.get("Company Name", row.get("Компания", ""))
            website = row.get("Website", row.get("Сайт", ""))

            prompt = f"""
--- COMPANY {i+1} ---
Company: {company}
Website: {website}

Write 1-2 short sentences in Russian that personalize a cold email for this company.
It must be factual, based on what the company actually does.
Focus on: their product, niche, or something specific about their business.
Example: "Заметил, что Pilot PRO помогает автоматизировать бизнес-процессы для логистических компаний."

Return in this exact format:
COMPANY {i+1}: [your personalization text here]
"""
            out.write(prompt)

    print(f"Done. Open {OUTPUT_FILE} and paste into Claude.")
    print("After Claude responds, save it as claude_output.txt and run step2.py")


if __name__ == "__main__":
    main()