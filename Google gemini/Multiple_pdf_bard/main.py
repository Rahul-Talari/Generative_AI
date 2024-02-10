import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS


import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from constants import api_key


genai.configure(api_key=api_key)

pdf_reader = PdfReader()
raw_text = ''
for page in pdf_reader.pages:
    content = page.extract_text()
    if content:
        raw_text += content
    text_splitter = CharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=1000,
    )
chunks = text_splitter.split_text(raw_text)
embeddings=GoogleGenerativeAIEmbeddings(model='models/embedding-001')
vector_store=FAISS.from_texts(chunks,embedding=embeddings)

prompt_template="""
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
model=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.7)
prompt=PromptTemplate(template=prompt_template,input_variables=["context","question"])
chain=load_qa_chain(model,prompt=prompt,chain_type="stuff")
query = st.text_input("Enter your question:")

docs = vectore_store.similarity_search(query)
result = chain.run(input_documents=docs, question=query)
st.subheader("Result:")
st.write(result)