from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.prompts import PromptTemplate

def build_qa_chain(documents):
    embeddings = OpenAIEmbeddings()

    # Vector store for the knowledge base documents
    vector_store = Chroma.from_documents(documents, embeddings, persist_directory="db")
    retriever = vector_store.as_retriever()

    # Use summary-based memory to reduce token usage
    memory = ConversationSummaryMemory(
        llm=OpenAI(temperature=0),
        memory_key="chat_history",
        return_messages=True
    )
    
    # Custom prompt to preserve currency format
    custom_prompt = PromptTemplate.from_template("""
    You are an AI assistant at an aesthetics clinic.
    Answer the question using only the provided context below.

    Make sure to:
    - Keep all currency symbols like €, $, £ in their correct form (do not use unicode escapes).
    - Respond concisely and professionally.

    Context:
    {context}

    Question:
    {question}
    """)
    
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=OpenAI(temperature=0.3),
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": custom_prompt}
    )

    return qa_chain
