# ============================================
# TYPE 1: STRING PROMPT TEMPLATE
# Sabse aasaan — sirf ek sawaal, koi role nahi
# ============================================

from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

# ─── Basic — Ek Variable ───
template1 = PromptTemplate(
    template="Mujhe {topic} ke baare mein batao",
    input_variables=["topic"]
)

prompt = template1.invoke({"topic": "Machine Learning"})
response = model.invoke(prompt)
print("Basic Example:")
print(response.content)
print("-" * 50)

# ─── Multiple Variables ───
template2 = PromptTemplate(
    template="{topic} ko {style} style mein {length} mein samjhao",
    input_variables=["topic", "style", "length"]
)

prompt = template2.invoke({
    "topic":  "Python",
    "style":  "simple",
    "length": "2 lines mein"
})
response = model.invoke(prompt)
print("Multiple Variables Example:")
print(response.content)
