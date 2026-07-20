from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model=ChatMistralAI(model="mistral-small-2603",temperature=0.5)
response=model.invoke("what is ai/ml")
print(response.content)