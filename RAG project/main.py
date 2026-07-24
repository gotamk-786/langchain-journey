from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


data = TextLoader(
    r"D:\Langchain\RAG project\document loaders\notes.txt"
)
docs=data.load()
template=ChatPromptTemplate.from_messages([
    ("system", "yopu are a AI that sumarizes the text"),
    ("human","{data}")
])

model=ChatMistralAI(model="mistral-small-2503")

prompt=template.format_messages(data=docs[0].page_content)
result=model.invoke(prompt)

print(result.content)