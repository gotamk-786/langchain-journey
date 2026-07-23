# ============================================
# TYPE 3: FEW SHOT PROMPT TEMPLATE
# Examples de kar AI ko sikhao
# AI khud pattern follow karta hai
# ============================================

from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

# ─── Example 1: Urdu to English Translator ───

# Step 1: Examples do (AI ye pattern seekhega)
examples = [
    {"urdu": "khush",     "english": "happy"},
    {"urdu": "udaas",     "english": "sad"},
    {"urdu": "gussa",     "english": "angry"},
    {"urdu": "thaka hua", "english": "tired"},
]

# Step 2: Har example ka format
example_template = PromptTemplate(
    input_variables=["urdu", "english"],
    template="Urdu: {urdu} -> English: {english}"
)

# Step 3: Few Shot Template
few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_template,
    prefix="Translate Urdu words to English:",
    suffix="Urdu: {input} -> English:",
    input_variables=["input"]
)

# Step 4: Use karo
prompt = few_shot.invoke({"input": "pyara"})
response = model.invoke(prompt)
print("Urdu to English:")
print(response.content)
print("-" * 50)

# ─── Example 2: Sentiment Classifier ───
examples2 = [
    {"review": "Bohat acha product hai!",    "sentiment": "Positive"},
    {"review": "Bilkul bekaar tha.",          "sentiment": "Negative"},
    {"review": "Theek thak hai, kuch khaas nahi.", "sentiment": "Neutral"},
]

example_template2 = PromptTemplate(
    input_variables=["review", "sentiment"],
    template="Review: {review}\nSentiment: {sentiment}"
)

few_shot2 = FewShotPromptTemplate(
    examples=examples2,
    example_prompt=example_template2,
    prefix="Classify the sentiment of these reviews:",
    suffix="Review: {input}\nSentiment:",
    input_variables=["input"]
)

prompt2 = few_shot2.invoke({"input": "Delivery bohat slow thi lekin product acha tha"})
response2 = model.invoke(prompt2)
print("Sentiment Classifier:")
print(response2.content)
