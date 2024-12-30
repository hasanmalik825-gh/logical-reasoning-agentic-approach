import streamlit as st
from reasoning_agent import get_reasoning_agent

groq_api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")
agent = get_reasoning_agent(groq_api_key)

st.title("🦜 Logical Reasoning Agent")
st.write("Ask any logical reasoning question.")

user_input=st.chat_input(placeholder="Enter your question here...")

if user_input and groq_api_key:
    st.write(user_input)
    st.info("Thinking...")
    response = agent.invoke({"input": user_input})
    st.success("Done!")
    with st.expander("Agentic Response", expanded=True):
        st.write(response["output"])
else:
    st.warning("Please enter both, your Groq API key and question.")
