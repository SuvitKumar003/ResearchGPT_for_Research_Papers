# vectorstore/query_index.py
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def search_query(user_query):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    
    vectorstore = FAISS.load_local(
        r"D:\OneDrive\Desktop\ResearchGPT_for_Research_Papers\langchain_app\vectorstore\faiss_store",
        embeddings,
        allow_dangerous_deserialization=True
    )

    results = vectorstore.similarity_search(user_query, k=3)
    return [res.page_content for res in results]
