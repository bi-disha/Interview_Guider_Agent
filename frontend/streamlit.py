import streamlit as st
from backend.ibm_client import ask_agent

st.set_page_config(page_title="IBM Agentic AI", layout="centered")
st.title("🤖 IBM Agentic AI Chatbot")

if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.text_input("Ask me something:")

if st.button("Send") and user_input:
    response = ask_agent(user_input)
    st.session_state["history"].append(("You", user_input))
    st.session_state["history"].append(("AI", response))

for role, text in st.session_state["history"]:
    st.markdown(f"**{role}:** {text}")
