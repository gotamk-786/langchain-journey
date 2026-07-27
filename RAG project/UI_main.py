import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

st.title("📄 RAG Chatbot — Upload PDF and Ask Questions")

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
llm = ChatMistralAI(model="mistral-small-2503")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
    ),
    (
        "human",
        """Context:
{context}

Question:
{question}
"""
    )
])

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file and st.button("Create Vectorstore"):
    with st.spinner("Reading PDF and building vectorstore..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        docs = PyPDFLoader(tmp_path).load()

        for doc in docs:
            doc.page_content = doc.page_content.encode("utf-8", "ignore").decode("utf-8")

        chunks = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        ).split_documents(docs)

        st.session_state.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model
        )

        os.remove(tmp_path)

    st.success("Vectorstore ready! Ask your questions below.")

if st.session_state.vectorstore:
    question = st.text_input("Ask a question about the PDF:")

    if question:
        retriever = st.session_state.vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.5}
        )

        docs = retriever.invoke(question)
        context = "\n\n".join(doc.page_content for doc in docs)

        final_prompt = prompt.invoke({"context": context, "question": question})
        response = llm.invoke(final_prompt)

        st.write("### Answer")
        st.write(response.content)
