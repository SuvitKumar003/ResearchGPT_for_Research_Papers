# researchgpt/main.py

from arxiv_fetcher import fetch_arxiv_papers
from summarizer import summarize_text
from report_generator import generate_pdf_report

def main():
    topic = input("Enter a research topic: ")

    print(f"\n🔍 Fetching papers on '{topic}'...")
    papers = fetch_arxiv_papers(topic, max_results=5)

    print(f"🧠 Summarizing {len(papers)} papers...\n")
    for paper in papers:
        print(f"→ Summarizing: {paper['title']}")
        paper['summary'] = summarize_text(paper['summary'])

    print("📝 Generating PDF report...")
    generate_pdf_report(papers)

    print("\n✅ Done! Your research summary is saved as 'researchgpt_report.pdf'.")

if __name__ == "__main__":
    main()
