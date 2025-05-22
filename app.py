# app.py (with memory-aware chain)
import streamlit as st
from dotenv import load_dotenv
from backend.loader import load_documents
from backend.qa_chain import build_qa_chain

load_dotenv()

st.set_page_config(page_title="💉 MedSpa RAG Chatbot")
st.title("💬 Ask our AI Aesthetic Assistant")

# Session memory init
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

@st.cache_resource
def init_chain():
    docs = load_documents("data/aesthetic_treatments_final.json")
    return build_qa_chain(docs)

qa_chain = init_chain()

# Input box
query = st.text_input(
    "What would you like to know about our treatments?",
    placeholder="e.g., Can I wear makeup after microneedling?"
)

if query:
    with st.spinner("Thinking..."):
        result = qa_chain({"question": query})
        answer = result["answer"]
        # Save to history
        st.session_state.chat_history.append((query, answer))

# 💬 Display chat history
if st.session_state.chat_history:
    st.markdown("---")
    for q, a in reversed(st.session_state.chat_history):
        st.markdown(f"**🧍 You:** {q}")
        st.markdown(f"**🧴 Assistant:** {a}")
        st.markdown("---")
