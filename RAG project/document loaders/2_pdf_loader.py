from langchain_community.document_loaders import PyPDFLoader


data=PyPDFLoader(
     r"D:\Langchain\RAG project\document loaders\GRU.pdf"
)

docs=data.load()
print(len(docs))