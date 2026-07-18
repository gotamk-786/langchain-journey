from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

result = model.invoke("paid api used karni chaiye ya free wali")

print(result.content)