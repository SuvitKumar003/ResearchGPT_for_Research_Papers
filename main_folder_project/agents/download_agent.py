import requests, os

def download_agent(state) -> dict:
    os.makedirs("downloads", exist_ok=True)
    pdf_paths = []
    for url in state["papers"]:
        r = requests.get(url)
        path = os.path.join("downloads", os.path.basename(url))
        open(path, "wb").write(r.content)
        pdf_paths.append(path)
    return {"pdf_paths": pdf_paths}
