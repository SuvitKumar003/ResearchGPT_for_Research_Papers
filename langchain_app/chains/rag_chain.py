from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader

# Load your saved FAISS index
def get_relevant_docs(query: str) -> str:
    db = FAISS.load_local("langchain_app/vectorstore/faiss_store", HuggingFaceEmbeddings())
    docs = db.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in docs])
