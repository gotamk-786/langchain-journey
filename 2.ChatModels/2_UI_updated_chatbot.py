import streamlit as st
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(page_title="Molai AI Chatbot", page_icon="🤖")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }
.stChatMessage { background: rgba(124,58,237,0.15) !important; border: 1px solid rgba(124,58,237,0.3) !important; border-radius: 12px !important; }
.stChatMessage p { color: #e0e7ff !important; }
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; padding:20px; background:linear-gradient(90deg,#7c3aed,#2563eb); border-radius:16px; margin-bottom:20px;'>
    <h1 style='color:white; margin:0;'>🤖 Molai AI Chatbot</h1>
    <p style='color:#c4b5fd; margin:5px 0 0;'>Powered by Mistral AI</p>
</div>
""", unsafe_allow_html=True)

# ─── Mode Selection (input() ki jagah selectbox) ───
choice = st.selectbox("Choose your mode:", ["1. Angry Mode 😠", "2. Funny Mode 😂", "3. Sad Mode 😢"])

if "1" in choice:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif "2" in choice:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif "3" in choice:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

# ─── Aap Ka Original Code ───
model = ChatMistralAI(model="mistral-small-2503", temperature=0.5)

if "message" not in st.session_state or st.session_state.get("last_mode") != choice:
    st.session_state.message = [SystemMessage(content=mode)]
    st.session_state.last_mode = choice

# Purani chat dikhao
for msg in st.session_state.message:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

prompt = st.chat_input("You: ")

if prompt:
    st.session_state.message.append(HumanMessage(content=prompt))
    response = model.invoke(st.session_state.message)
    st.session_state.message.append(AIMessage(content=response.content))

    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write(response.content)