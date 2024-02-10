import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from constants import api_key

def get_vector_store(pdf_docs):
    raw_text = ''
    for pdf_file in pdf_docs:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                raw_text += content

    text_splitter = CharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=1000,
    )
    chunks = text_splitter.split_text(raw_text)

    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001', google_api_key=api_key)
    vector_db = FAISS.from_texts(chunks, embedding=embeddings)
    vector_db.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """Answer the question as detailed as possible from the provided context, make sure to provide all the details,
                        if the answer is not in provided context just say, "answer is not available in the context", don't provide 
                        the wrong answer\n\n
                        Context:\n {context}?\n
                        Question: \n{question}\n
                    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, google_api_key=api_key)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, prompt=prompt, chain_type="stuff")
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001', google_api_key=api_key)
    db = FAISS.load_local("faiss_index", embeddings)
    docs = db.similarity_search(user_question)
    chain = get_conversational_chain()
    result = chain.run(input_documents=docs, question=user_question)
    st.subheader("Result:")
    st.write(result)

def main():
    st.set_page_config("Chat with multiple PDF")
    st.header("Chat with Multiple PDF using Google gemini💁")

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                get_vector_store(pdf_docs)
                st.success("Done")          

    user_question = st.text_input("Ask a question from pdf")
    if user_question:
        user_input(user_question)

if __name__ == "__main__":
    main()
