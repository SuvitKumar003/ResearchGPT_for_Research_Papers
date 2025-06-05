class Synthesizer:
    def synthesize(self, papers):
        combined = "Synthesis of key ideas:\n\n"
        for i, paper in enumerate(papers, 1):
            combined += f"{i}. {paper['title']}:\n{paper['summary']}\n\n"
        return combined
