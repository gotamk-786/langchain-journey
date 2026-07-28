from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()
model=ChatMistralAI(model="mistral-small-2503",temperature=1)
result=model.invoke("what is Ai")

print(result.content)
print(result.response_metadata)
print("\n\n")
print(result.usage_metadata)