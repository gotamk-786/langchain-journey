from langchain_groq import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4", temperature=1.5, max_completion_tokend=10)
result=model.invoke("What is the capitaL OF PAKISTAN")

print(result.content)