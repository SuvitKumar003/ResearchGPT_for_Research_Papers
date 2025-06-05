# researchgpt/report_generator.py

from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "ResearchGPT Summary Report", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generate_pdf_report(papers, file_path="researchgpt_report.pdf"):
    pdf = PDFReport()
    pdf.add_page()

    for i, paper in enumerate(papers):
        pdf.chapter_title(f"{i+1}. {paper['title']}")
        pdf.chapter_body(f"Link: {paper['link']}\n\nSummary:\n{paper['summary']}\n")

    pdf.output(file_path)
