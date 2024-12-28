import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler
from reasoning_agent import get_reasoning_agent

groq_api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")
agent = get_reasoning_agent(groq_api_key)

st.title("🦜 Logical Reasoning Agent")
st.write("Ask any logical reasoning question.")

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm an intelligent and logical agent. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input=st.chat_input(placeholder="Enter your question here...")

if user_input and groq_api_key:
    st.session_state.messages.append({"role":"user","content":user_input})
    st.chat_message("user").write(user_input)
    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response = agent.invoke({"input": st.session_state.messages}, callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant',"content":response["output"]})
        st.write(response["output"])
else:
    st.warning("Please enter both, your Groq API key and question.")
