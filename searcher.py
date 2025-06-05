import requests

class Searcher:
    def __init__(self, max_results=10):
        self.max_results = max_results

    def fetch_papers(self, query):
        base_url = 'http://export.arxiv.org/api/query?'
        search_query = f'search_query=all:{query}&start=0&max_results={self.max_results}'
        url = base_url + search_query
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch papers: {response.status_code}")

        import xml.etree.ElementTree as ET
        root = ET.fromstring(response.content)

        papers = []
        ns = {'arxiv': 'http://www.w3.org/2005/Atom'}
        entries = root.findall('arxiv:entry', ns)
        for entry in entries:
            title = entry.find('arxiv:title', ns).text.strip().replace('\n', ' ')
            summary = entry.find('arxiv:summary', ns).text.strip().replace('\n', ' ')
            link = entry.find('arxiv:id', ns).text if entry.find('arxiv:id', ns) is not None else ''
            papers.append({'title': title, 'summary': summary, 'link': link})
        return papers
