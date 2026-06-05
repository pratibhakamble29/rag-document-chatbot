import streamlit as st
from utils.loader import load_pdf
from utils.splitter import split_text
from utils.vectorstore import create_vectorstore
from utils.retriever import retrieve_answer

st.title("📄 RAG Document Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

vectorstore = None

if uploaded_file:

    text = load_pdf(uploaded_file)

    chunks = split_text(text)

    vectorstore = create_vectorstore(chunks)

    st.success("PDF uploaded successfully!")

    st.success("Vector Database Created!")

    st.write(f"Number of Chunks: {len(chunks)}")

    st.subheader("First Chunk")

    st.text_area(
        "Chunk Preview",
        chunks[0],
        height=300
    )

question = st.text_input("Ask a question")

if st.button("Ask"):

    if uploaded_file and question and vectorstore:

        st.write("Ask button clicked ✅")

        answer = retrieve_answer(
            vectorstore,
            question
        )

        st.subheader("Answer")

        st.write(answer)

    else:

        st.warning(
            "Please upload a PDF and enter a question."
        )