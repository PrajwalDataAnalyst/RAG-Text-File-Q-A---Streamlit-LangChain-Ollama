import streamlit as st
from loaders.text_loader import load_text_document
from utils.file_handler import save_uploaded_file
from rag.embed_and_store import build_vector_store
from rag.retriever import get_top_result

st.title("📄 RAG Text File Q&A - Streamlit + LangChain + Ollama")

uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])

if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)
    docs = load_text_document(file_path)
    vectorstore = build_vector_store(docs)

    st.success("✅ Document processed. Ask a question!")

    query = st.text_input("💬 Your question:")
    if query:
        answer = get_top_result(vectorstore, query)
        st.subheader("📌 Answer:")
        st.write(answer)
