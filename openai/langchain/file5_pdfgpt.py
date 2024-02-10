import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from constants import openai_key
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI


# Function to read PDF and split text
def read_and_split_pdf(file_path):
    pdf_reader = PdfReader(file_path)
    raw_text = ''
    for i, page in enumerate(pdf_reader.pages):
        content = page.extract_text()
        if content:
            raw_text += content
    text_splitter = CharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=200,
    )
    texts = text_splitter.split_text(raw_text)
    return texts

# Streamlit app
def main():
    st.title("PDF Text Analysis with LangChain and OpenAI")

    # File upload
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file:
        # Read and split PDF
        texts = read_and_split_pdf(uploaded_file)

        # LangChain setup
        embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
        document_search = FAISS.from_texts(texts, embeddings)
        openai = OpenAI(openai_api_key=openai_key)
        chain = load_qa_chain(openai, chain_type="stuff")

        # Query input
        query = st.text_input("Enter your question:")

        if st.button("Run Analysis"):
            # Similarity search and chain run
            docs = document_search.similarity_search(query)
            result = chain.run(input_documents=docs, question=query)

            # Display result
            st.subheader("Result:")
            st.write(result)

if __name__ == "__main__":
    main()
