# researchgpt/arxiv_fetcher.py

import requests
import xml.etree.ElementTree as ET

def fetch_arxiv_papers(topic, max_results=5):
    base_url = "http://export.arxiv.org/api/query?"
    search_query = f"search_query=all:{topic}&start=0&max_results={max_results}"

    response = requests.get(base_url + search_query)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from arXiv API.")

    root = ET.fromstring(response.content)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}

    papers = []
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip()
        summary = entry.find('atom:summary', ns).text.strip()
        link = entry.find('atom:id', ns).text.strip()

        papers.append({
            'title': title,
            'summary': summary,
            'link': link
        })

    return papers