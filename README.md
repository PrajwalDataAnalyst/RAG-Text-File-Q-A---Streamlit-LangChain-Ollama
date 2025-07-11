# 🧠 Local RAG App – Ask Questions from Your Text File

This project is a simple **RAG (Retrieval-Augmented Generation)** chatbot that lets users **upload their own `.txt` or '.pdf' file** and ask natural language questions based on the content of that file.

Built using:
- 🔗 LangChain
- 🧠 FAISS for vector storage
- 🤖 Ollama's Mistral model for LLM responses
- 🎈 Streamlit for the user interface

---

## ✨ Features

- 📁 Upload any `.txt` file with your own knowledge base
- 🧩 The app splits the document into chunks automatically
- 🧠 Embeds the chunks into vector format for similarity search
- 🔍 Finds the most relevant chunks based on your question
- 💬 Sends the context + your query to a local LLM (Mistral) to generate grounded answers
- 🖥️ Runs completely locally with **no API calls** to external cloud services

---

## 🔄 How It Works (Flow)

1. **User uploads a `.txt` file** from the Streamlit interface.
2. The file is loaded and **split into smaller text chunks** using `RecursiveCharacterTextSplitter`.
3. Each chunk is **converted into a vector (embedding)** using `OllamaEmbeddings` with the `mistral` model.
4. The chunks are stored in a **FAISS vector database**.
5. When a user types a question:
   - The app **searches the most relevant chunks** using vector similarity.
   - The **top results are passed as context** into the LLM.
   - The **LLM (Mistral)** generates a natural language answer.
6. The answer is displayed in the Streamlit interface like a chatbot response.

---

## 🧪 Technologies Used

| Tool       | Purpose                            |
|------------|-------------------------------------|
| Streamlit  | Frontend UI                         |
| LangChain  | Chaining RAG logic                  |
| FAISS      | Vector similarity search            |
| Ollama     | Runs local Mistral model            |
| Python     | Backend logic                       |

---

## 🚀 How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/PrajwalDataAnalyst/RAG-Text-File-Q-A---Streamlit-LangChain-Ollama.git
cd RAG-Text-File-Q-A---Streamlit-LangChain-Ollama

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows


3. Install Dependencies
    pip install -r requirements.txt

4. Start the Streamlit App
streamlit run app.py

🙋‍♂️ FAQ
Q: Can I upload any text file?
Yes, the app accepts any .txt file with readable content.

Q: What models does this use?
It uses Mistral locally through Ollama, but can be extended to other LLMs.

Q: Does this require internet?
Only for installing dependencies. After that, it runs completely offline.


⭐️ Star the Repo
If this project helps you, give it a ⭐️ to show support!


