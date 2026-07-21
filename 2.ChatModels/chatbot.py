from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503", temperature=0.5)

message = [
    SystemMessage(content="You are a Funny AI agent")
]

print("CHoose you mode")
print("1.Angry mode")
print("2.Sad mode")
print("3.Funny mode")

choice=input("Please ,Enter your choose")

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."
print("--- Welcome Chatbot | type 0 to exit ---")

while True:
    prompt = input("You: ")
    if prompt == "0":
        break
    message.append(HumanMessage(content=prompt))
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot:", response.content)







#1. SystemMessage
# AI ko instructions deta hai — "tu kaisa behave kare"
# Jaise teacher ko school rules batana
# Ye user nahi, AI nahi — ye RULES hain
# Sirf ek baar shuru mein dete hain

#stemMessage(content="You are a funny AI assistant")
# matlab: AI mazakiya andaaz mein baat kare


#2. HumanMessage
# User jo bhi type kare — wo HumanMessage hota hai
# Jab aap kuch likho — wo is wrapper mein jaata hai
# AI ko pata chalta hai ke ye INSAAN ne kaha hai

#HumanMessage(content="Pakistan ka capital kya hai?")
# matlab: user ne ye sawaal pucha


#3. AIMessage
# AI ka jawab — jo model ne diya
# Hum ise save karte hain taake AI ko
# pichli conversation yaad rahe

#AIMessage(content="Islamabad hai Pakistan ka capital")
# matlab: AI ne ye jawab diya — yaad rakhna hai\



##messages = [
 #   SystemMessage(content="Tu funny AI hai"),  # Rule
  #  HumanMessage(content="Mera naam kya hai?"),# User
   # AIMessage(content="Mujhe nahi pata bhai!"),# AI jawab
    # HumanMessage(content="Joke sunao"),        # User dobara
#]
# List badhti jaati hai — poori history yaad rehti hai!
# List badhti jaati hai — poori history yaad rehti hai!