from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

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

template=ChatPromptTemplate.from_messages([
    ("system", "yopu are a AI that sumarizes the text"),
    ("human","{data}")
])

model=ChatMistralAI(model="mistral-small-2503")

prompt=template.format_messages(data=docs[0].page_content)
result=model.invoke(prompt)

print(result.content)