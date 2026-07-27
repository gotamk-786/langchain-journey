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

for doc in docs:
    doc.page_content = doc.page_content.encode("utf-8", "ignore").decode("utf-8")

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=splitter.split_documents(docs) 


embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



verctorstore=Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)