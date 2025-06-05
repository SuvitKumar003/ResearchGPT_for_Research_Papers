from searcher import Searcher
from summarizer import Summarizer
from critic import Critic
from synthesizer import Synthesizer
from reporter import generate_pdf

def main():
    query = input("Enter research topic: ")

    searcher = Searcher(max_results=10)
    summarizer = Summarizer()
    critic = Critic(threshold=0.5)
    synthesizer = Synthesizer()

    print(f"Searching papers for '{query}'...")
    papers = searcher.fetch_papers(query)

    print(f"Summarizing papers...")
    for paper in papers:
        paper['summary'] = summarizer.summarize(paper['summary'])

    print(f"Filtering papers...")
    papers = critic.filter_papers(papers)

    print(f"Synthesizing summaries...")
    synthesis = synthesizer.synthesize(papers)

    print(f"Generating report...")
    generate_pdf(papers)

    print("\nReport generated: multi_agent_report.pdf")
    print("\nSynthesis Preview:\n", synthesis[:500], "...")

if __name__ == "__main__":
    main()
