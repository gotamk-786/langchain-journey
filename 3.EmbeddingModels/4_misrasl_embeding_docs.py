from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=MistralAIEmbeddings(model="mistral-embed"
                              )

documents=[
    "Islamabad is the capital of Pakistan",
    "Lahore is the cultural capital of Pakistan",
    "Karachi is the largest city of Pakistan"
]

result = embedding.embed_documents(documents)

print(str(result))