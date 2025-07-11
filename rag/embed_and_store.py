from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from config.ollama_config import get_embedding_model

def build_vector_store(doc):
    text_split=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
    text_split=text_split.split_documents(doc)


    embedding=get_embedding_model()
    vectorstore =FAISS.from_documents(text_split,embedding=embedding)

    return vectorstore 