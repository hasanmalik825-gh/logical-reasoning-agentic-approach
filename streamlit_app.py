import streamlit as st
from reasoning_agent import get_reasoning_agent

groq_api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")
agent = get_reasoning_agent(groq_api_key)

st.title("Logical Reasoning Agent")
st.write("Ask any logical reasoning question.")
user_input = st.text_input("Enter your question:")

if st.button("Ask Intelligent Agent"):
    if not groq_api_key or not user_input:
        st.warning("Please enter both, your Groq API key and question.")
    else:
        st.info("Thinking...")
        response = agent.invoke({"input": user_input})
        st.success("Done!")
        with st.expander("Agentic Response", expanded=True):
            st.write(response["output"])