import streamlit as st
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_community.llms import OpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from constants import openai_key, ASTRA_DB_APPLICATION_TOKEN, ASTRA_DB_ID
import cassio

# Initialize Streamlit app
st.title("QA Demo using Streamlit")

# File uploader for PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Function to process and display answers
def process_question(query_text, astra_vector_index, astra_vector_store, llm):
    st.write(f"QUESTION: \"%s\"" % query_text)
    answer = astra_vector_index.query(query_text, llm=llm).strip()
    st.write("ANSWER: \"%s\"\n" % answer)

    st.write("FIRST DOCUMENTS BY RELEVANCE:")
    for doc, score in astra_vector_store.similarity_search_with_score(query_text, k=4):
        st.write("    [%0.4f] \"%s ...\"" % (score, doc.page_content[:84]))

# Process PDF file if uploaded
if uploaded_file is not None:
    raw_text = ''
    pdf_reader = PdfReader(uploaded_file)
    for i, page in enumerate(pdf_reader.pages):
        content = page.extract_text()
        if content:
            raw_text += content

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=400,
        chunk_overlap=200,
    )
    texts = text_splitter.split_text(raw_text)

    # Initialization
    llm = OpenAI(openai_api_key=openai_key, temperature=0.7)
    embedding = OpenAIEmbeddings(openai_api_key=openai_key)

    cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

    astra_vector_store = None  # Initialize astra_vector_store

    if astra_vector_store is None:
        astra_vector_store = Cassandra(
            embedding=embedding,
            table_name="qa_mini_demo",
            session=None,
            keyspace=None,
        )
    else:
        # Drop existing vectors
        astra_vector_store.drop_table()

    astra_vector_store.add_texts(texts)
    st.write(f"Inserted {len(texts)} headlines.")
    astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

    # Streamlit app
    query_text = st.text_input("Enter your question:")
    if st.button("Ask"):
        if query_text.lower() == "quit":
            st.stop()

        if query_text == "":
            st.warning("Please enter a question.")
        else:
            process_question(query_text, astra_vector_index, astra_vector_store, llm)
