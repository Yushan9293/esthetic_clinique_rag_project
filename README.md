# 💉 Esthetic Clinique RAG Chatbot

A smart GPT-4-powered chatbot built for aesthetic & skincare clinics.  
It uses LangChain’s `ConversationalRetrievalChain` to answer natural language questions about treatments, pricing, aftercare, and more — with memory.

---

## 🚀 What It Does

- 🤖 Conversational chatbot for aesthetic treatment FAQs
- 🔍 Retrieves answers from structured JSON data (prices, numbing, aftercare, etc.)
- 🧠 Remembers previous messages using LangChain `ConversationalRetrievalChain`
- 🧴 Streamlit UI with full chat history display
- ⚡ Powered by OpenAI GPT-4, Chroma, and LangChain

---

## 📂 Project Structure

```

esthetic\_clinique\_rag\_project/
├── app.py                     # Streamlit frontend UI
├── .env                       # OpenAI API key (not tracked)
├── requirements.txt           # Python dependencies
├── backend/
│   ├── loader.py              # Load aesthetic treatment data
│   └── qa\_chain.py            # Build conversational RAG chain
└── data/
└── aesthetic\_treatments\_final.json

````

---

## 📦 Tech Stack

- [LangChain](https://github.com/langchain-ai/langchain)
- [Chroma](https://www.trychroma.com/)
- [OpenAI](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)
- [Python-dotenv](https://github.com/theskumar/python-dotenv)

---

## 🔧 Installation

### 1. Clone project

```bash
git clone https://github.com/YOUR_USERNAME/esthetic_clinique_rag_project
cd esthetic_clinique_rag_project
````

### 2. Create virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-openai-key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then go to `http://localhost:8501` in your browser.

---

## 💬 Example Questions

```text
What is the price of Thermage for full face?
Can I wear makeup after microneedling?
Does HIFU require numbing cream?
How often should I get laser hair removal?
```

---


## 📘 Use Cases

* Aesthetic clinic website assistants
* Virtual consultation tools for skincare
* Internal staff tools to lookup treatment details
* RAG chatbot showcase for LLM development portfolio

---

## 📄 License

MIT License

Copyright (c) 2025 Yushan Lin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell    
copies of the Software, and to permit persons to whom the Software is        
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in    
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE.

---

🧠 This project is published for **educational and demonstration purposes**.  
Please contact the author for commercial or customized usage.


---



