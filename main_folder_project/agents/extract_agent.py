from PyPDF2 import PdfReader

def extract_agent(state) -> dict:
    texts = []
    for pdf in state["pdf_paths"]:
        reader = PdfReader(pdf)
        txt = "".join(page.extract_text() or "" for page in reader.pages)
        texts.append(txt[:2000])
    return {"texts": texts}
