import streamlit as st
import json
from datetime import datetime
from time import sleep

# Load Q&A data
with open("qa_data.json", "r") as file:
    qa_data = json.load(file)

# Helper function to get the answer from the dataset
def get_answer(user_input):
    for item in qa_data["questions"]:
        if user_input.lower() in item["question"].lower():
            return item["answer"]
    return "I'm sorry, I couldn't find an answer to your question."

# Set Streamlit page config
st.set_page_config(page_title="My Chatbot", page_icon="🤖", layout="centered")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.title("🤖 Simple Chatbot")

# Chat UI container
chat_container = st.container()

# Display past messages
with chat_container:
    for msg in st.session_state.chat_history:
        role = "🧑 You" if msg["role"] == "user" else "🤖 Bot"
        st.markdown(f"**{role}:** {msg['message']}")

# Input field at the bottom
user_input = st.text_input("Type your message...", key="input")

# When user sends a message
if user_input:
    st.session_state.chat_history.append({"role": "user", "message": user_input})

    with st.spinner("Bot is typing..."):
        sleep(1)  # Simulate thinking time
        answer = get_answer(user_input)

    st.session_state.chat_history.append({"role": "bot", "message": answer})

    # Rerun to display new messages
    st.experimental_rerun()
