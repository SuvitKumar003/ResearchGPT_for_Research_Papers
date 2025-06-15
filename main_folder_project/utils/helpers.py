import os
import requests
from PyPDF2 import PdfReader

def download_pdf(pdf_url, save_path="downloads"):
    os.makedirs(save_path, exist_ok=True)
    filename = os.path.join(save_path, pdf_url.split("/")[-1] + ".pdf")
    r = requests.get(pdf_url)
    with open(filename, 'wb') as f:
        f.write(r.content)
    return filename

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
