from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

print("Step 1")

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1,
)

loader = TextLoader(
    r"D:\Langchain\RAG project\document loaders\notes.txt"
)

print("Step 2")

docs = loader.load()

chunks = splitter.split_documents(docs)


print("Step 3")
print(len(chunks))
for i in chunks:
    print(i.page_content)
    print()
    print()