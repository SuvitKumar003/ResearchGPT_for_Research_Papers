from fpdf import FPDF

class Reporter(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Multi-Agent ResearchGPT Report", 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, 0, 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generate_pdf(papers, file_path="multi_agent_report.pdf"):
    pdf = Reporter()
    pdf.add_page()
    for paper in papers:
        pdf.chapter_title(paper['title'])
        pdf.chapter_body(f"Link: {paper['link']}\n\nSummary:\n{paper['summary']}")
    pdf.output(file_path)
