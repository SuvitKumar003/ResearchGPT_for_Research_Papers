from flask import Flask, render_template, request
from searcher import Searcher
from summarizer import Summarizer
from critic import Critic
from synthesizer import Synthesizer
from reporter import generate_pdf

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        query = request.form.get("query")
        
        # Initialize agents
        searcher = Searcher(max_results=10)
        summarizer = Summarizer()
        critic = Critic(threshold=0.5)
        synthesizer = Synthesizer()

        papers = searcher.fetch_papers(query)
        for paper in papers:
            paper['summary'] = summarizer.summarize(paper['summary'])
        papers = critic.filter_papers(papers)
        synthesis = synthesizer.synthesize(papers)
        generate_pdf(papers)  # Saves report locally
        
        result = synthesis  # Show synthesis text on web page

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
