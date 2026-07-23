# ============================================
# REAL PROJECT 2: RESEARCH PAPER EXPLAINER
# Streamlit UI + Chat Prompt + Chain + Parser
# Run: streamlit run 7_research_paper_explainer.py
# ============================================

import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# ─── Page Config ───
st.set_page_config(page_title="Research Paper Explainer", page_icon="📄")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }
.stSelectbox label { color: #c4b5fd !important; font-weight: bold !important; }
[data-testid="stSelectbox"] > div > div {
    background: #1e1b4b !important;
    border: 2px solid #7c3aed !important;
    border-radius: 12px !important;
    color: white !important;
}
.stButton button {
    background: linear-gradient(90deg, #7c3aed, #2563eb) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    font-weight: bold !important;
    width: 100% !important;
    padding: 12px !important;
}
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─── Header ───
st.markdown("""
<div style='text-align:center; padding:20px; background:linear-gradient(90deg,#7c3aed,#2563eb); border-radius:16px; margin-bottom:20px;'>
    <h1 style='color:white; margin:0;'>📄 Research Paper Explainer</h1>
    <p style='color:#c4b5fd; margin:5px 0 0;'>Powered by Groq + LangChain</p>
</div>
""", unsafe_allow_html=True)

# ─── UI Inputs ───
paper_input = st.selectbox("Select Research Paper Name", [
    "Select...",
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"
])

style_input = st.selectbox("Select Explanation Style", [
    "Beginner-Friendly",
    "Technical",
    "Code-Oriented",
    "Mathematical"
])

length_input = st.selectbox("Select Explanation Length", [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)"
])

# ─── Template ───
template = ChatPromptTemplate.from_messages([
    ("system", """You are an expert at explaining research papers.
     Your task is to summarize clearly based on given specifications.

     1. Mathematical Details:
        - Include relevant equations if present.
        - Explain math using simple, intuitive code snippets where applicable.

     2. Analogies:
        - Use relatable analogies to simplify complex ideas.

     If certain information is not available, respond with:
     "Insufficient information available" instead of guessing.

     Ensure the summary is clear, accurate, and aligned with the style and length."""),

    ("human", """Please summarize the research paper titled {paper_input}
     with the following specifications:
     Explanation Style: {style_input}
     Explanation Length: {length_input}""")
])

# ─── Chain ───
model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)
parser = StrOutputParser()
chain = template | model | parser

# ─── Button ───
if st.button("Explain This Paper!"):
    if paper_input == "Select...":
        st.warning("Pehle paper select karo!")
    else:
        with st.spinner("Samajh raha hoon..."):
            response = chain.invoke({
                "paper_input":  paper_input,
                "style_input":  style_input,
                "length_input": length_input
            })
        st.success("Ye raha explanation:")
        st.write(response)
