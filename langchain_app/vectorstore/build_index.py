from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Step 1: Load your PDF/text
loader = PyPDFLoader("data/research.pdf")  # Add your own paper
docs = loader.load()

# Step 2: Chunk the text
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Step 3: Convert to embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Step 4: Store in FAISS
db = FAISS.from_documents(chunks, embeddings)
db.save_local("langchain_app/vectorstore/faiss_store")
