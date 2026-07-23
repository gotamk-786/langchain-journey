from dotenv import load_dotenv
import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Select...",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (Detailed Explanation)"
    ]
)

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert at explaining research papers.

Your task is to summarize the given research paper.

Rules:
- Explain according to the requested explanation style.
- Follow the requested explanation length.
- Include mathematical equations if applicable.
- Use analogies where useful.
- Do not hallucinate.
- If information is unavailable, say "Insufficient information available."
"""
        ),
        (
            "human",
            """
Research Paper:
{paper_input}

Explanation Style:
{style_input}

Explanation Length:
{length_input}
"""
        )
    ]
)

if st.button("Summarize"):

    if paper_input == "Select...":
        st.warning("Please select a research paper.")
    else:

        prompt = template.invoke(
            {
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input
            }
        )

        result = model.invoke(prompt)

        st.write(result.content)