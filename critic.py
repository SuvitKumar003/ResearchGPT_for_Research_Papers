class Critic:
    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def score_summary(self, summary):
        # Simple heuristic: length & presence of keywords
        length_score = min(len(summary.split()) / 50, 1.0)
        keyword_score = 1.0 if 'important' in summary.lower() or 'novel' in summary.lower() else 0.5
        score = (length_score + keyword_score) / 2
        return score

    def filter_papers(self, papers):
        filtered = []
        for p in papers:
            score = self.score_summary(p['summary'])
            if score >= self.threshold:
                filtered.append(p)
        return filtered
