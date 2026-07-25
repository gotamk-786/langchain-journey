from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

data=PyPDFLoader(
     r"D:\Langchain\RAG project\document loaders\GRU.pdf"
)

docs=data.load()
splitter=TokenTextSplitter(

    chunk_size=100,
    chunk_overlap=10
)
chunks=splitter.split_documents(docs)
print(len(chunks))
print()
print(chunks[1].page_content)