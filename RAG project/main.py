from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model=ChatMistralAI(modeel="mistral-small-2503")
result=model.invoke(" what is ali ")

print(result.content)