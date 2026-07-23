# ============================================
# TYPE 2: CHAT PROMPT TEMPLATE
# System + Human — Proper role ke saath
# Industry mein 90% yahi use hota hai
# ============================================

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

# ─── Basic — System + Human ───
template = ChatPromptTemplate.from_messages([
    ("system", "Tum ek {role} ho"),   # AI ka role
    ("human",  "{sawaal}")             # User ka sawaal
])

prompt = template.invoke({
    "role":   "funny comedian",
    "sawaal": "Pakistan ke baare mein joke sunao"
})

response = model.invoke(prompt)
print("Basic Chat Prompt:")
print(response.content)
print("-" * 50)

# ─── Advanced — Multiple System Instructions ───
template2 = ChatPromptTemplate.from_messages([
    ("system", """Tum ek expert {subject} teacher ho.
     Hamesha simple examples se samjhao.
     Jawab {language} mein do."""),
    ("human", "{sawaal}")
])

prompt2 = template2.invoke({
    "subject":  "Python",
    "language": "Roman Urdu",
    "sawaal":   "Loop kya hota hai?"
})

response2 = model.invoke(prompt2)
print("Advanced Chat Prompt:")
print(response2.content)
