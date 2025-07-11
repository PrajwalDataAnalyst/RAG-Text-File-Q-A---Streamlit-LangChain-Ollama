import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader

def load_text_document(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".txt":
        loader = TextLoader(file_path=file_path, encoding="utf-8")
    elif ext == ".pdf":
        loader = PyPDFLoader(file_path)
    else:
        raise ValueError("Unsupported file type. Please upload a .txt or .pdf file.")
    
    return loader.load()
