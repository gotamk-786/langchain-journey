import streamlit as st

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    ToolMessage
)

from agents import llm_with_tools, tools


st.set_page_config(
    page_title="City Intelligence System",
    page_icon="🌍",
    layout="wide"
)

# ---------------- Sidebar ----------------

with st.sidebar:
    st.title("🌍 City Intelligence")
    st.markdown("---")

    st.markdown("### Available Tools")

    st.success("🌦 Weather Tool")
    st.success("📰 News Tool")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# ---------------- Title ----------------

st.title("🌍 City Intelligence System")

st.caption(
    "Ask about weather or latest news of any city or country."
)


# ---------------- Memory ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------- Show Chat History ----------------

for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)


# ---------------- Chat Input ----------------

prompt = st.chat_input("Ask something...")


if prompt:

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        thinking = st.empty()
        thinking.info("🤖 Thinking...")

        while True:

            result = llm_with_tools.invoke(
                st.session_state.messages
            )

            st.session_state.messages.append(result)

            if result.tool_calls:

                for tool_call in result.tool_calls:

                    tool_name = tool_call["name"]

                    thinking.info(
                        f"🔧 Using tool: {tool_name}"
                    )

                    tool_result = tools[tool_name].invoke(
                        tool_call["args"]
                    )

                    st.session_state.messages.append(
                        ToolMessage(
                            content=tool_result,
                            tool_call_id=tool_call["id"]
                        )
                    )

            else:

                thinking.empty()

                st.write(result.content)

                st.session_state.messages.append(
                    AIMessage(content=result.content)
                )

                break