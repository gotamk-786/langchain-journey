from langchain_community.document_loaders import TextLoader

print("Step 1")

loader = TextLoader(
    r"D:\Langchain\RAG project\document loaders\text_loader.txt"
)

print("Step 2")

docs = loader.load()

print("Step 3")

print(docs[0])  #this  is 1 documnet has metadasta and pagecontent