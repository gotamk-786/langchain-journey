# ============================================
# PARSER
# AI ka jawab check karo aur sahi format mein lo
# Chain = Template | Model | Parser
# ============================================

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv 

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

# ─── Example 1: String Parser — Clean Text ───
# Bina parser ke: AIMessage object milta hai
# Parser ke saath: sirf clean string milti hai

template = ChatPromptTemplate.from_messages([
    ("system", "Tum helpful assistant ho"),
    ("human",  "{sawaal}")
])

parser = StrOutputParser()

# Chain banao: template | model | parser
chain = template | model | parser

response = chain.invoke({"sawaal": "Pakistan ka capital kya hai?"})
print("String Parser Output:")
print(response)         # Clean string — koi metadata nahi
print(type(response))   # <class 'str'>
print("-" * 50)

# ─── Example 2: Chain with Multiple Steps ───
template2 = ChatPromptTemplate.from_messages([
    ("system", "Tum ek {role} ho. Hamesha concise jawab do."),
    ("human",  "{sawaal}")
])

chain2 = template2 | model | parser

# Alag alag roles ke saath
roles = [
    {"role": "doctor",   "sawaal": "Roz kitna paani peena chahiye?"},
    {"role": "teacher",  "sawaal": "Python seekhna chahiye ya JavaScript?"},
    {"role": "chef",     "sawaal": "Biryani mein kya dalna chahiye?"},
]

for r in roles:
    result = chain2.invoke(r)
    print(f"As {r['role']}: {result[:100]}...")
    print()
