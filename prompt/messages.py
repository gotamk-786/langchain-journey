from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model=ChatMistralAI(model="mistral-small-2503", temperature=0)

history=[SystemMessage(content="ap aik biology teacher h ap humein btaao ge kaisa kaisa karty achy se ")]


while True:
    x=input("You: ")
    if x=="0":
        break
    history.append(HumanMessage(content=x))
    result=model.invoke(history)
    history.append(AIMessage(content=result.content))
    print("AI :",result.content)


