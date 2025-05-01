import streamlit as st
from sentence_transformers import SentenceTransformer, util
import json

# Load the SentenceTransformer model (DistilBERT-based)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAQ data from JSON
with open('qa_data.json', 'r') as f:
    qa_pairs = json.load(f)

# Extract questions and encode them
questions = [item['question'] for item in qa_pairs]
question_embeddings = model.encode(questions)

# Streamlit UI
st.set_page_config(page_title="University Support Chatbot", layout="centered")
st.title("🎓 University Student Support Chatbot")
st.write("Ask me anything about exams, registration, results, and more!")

user_input = st.text_input("Your Question:")

if user_input:
    # Encode the user input
    user_embedding = model.encode(user_input)

    # Compute similarity with FAQ questions
    similarities = util.cos_sim(user_embedding, question_embeddings)[0]
    best_match_idx = similarities.argmax()
    best_score = similarities[best_match_idx].item()

    # Show result based on threshold
    if best_score > 0.6:
        answer = qa_pairs[best_match_idx]['answer']
        st.success(f"📢 Answer: {answer}")
    else:
        st.error("🤖 Sorry, I couldn't understand your question.")
