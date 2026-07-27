#load pdf
#split into chunks
#create the embeddings
#store into chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings


load_dotenv()

data = PyPDFLoader(
    r"D:\Langchain\RAG project\document loaders\deeplearning.pdf"
)
docs=data.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=splitter.split_documents(docs) 
chunks = splitter.split_documents(docs)

# strict filter — sirf asli text wale chunks rakhega
good_chunks = []
for c in chunks:
    if isinstance(c.page_content, str) and c.page_content.strip():
        good_chunks.append(c)

chunks = good_chunks
print("Total sahi chunks:", len(chunks))

# check karo koi chunk galat type ka to nahi
for i, c in enumerate(chunks):
    if not isinstance(c.page_content, str):
        print("GALAT chunk index:", i, "type:", type(c.page_content))
# ⬇️ sirf ye ek line add ki hai — khaali chunks nikaal deti hai
chunks=[c for c in chunks if c.page_content and c.page_content.strip()]


embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



verctorstore=Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)