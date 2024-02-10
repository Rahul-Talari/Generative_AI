from langchain_community.llms import OpenAI
from constants import openai_key
import streamlit as st

def QA(question):
    llm=OpenAI(openai_api_key=openai_key,temperature=0.7,model_name="text-davinci-003")
    response=llm(question)
    return response

st.set_page_config(page_title="Q&A demo")
st.header("Langchain Application")
input=st.text_input("Search the topic you want")
response=QA(input)
submit=st.button("Ask a question")


if submit:
    st.subheader("The response is:")
    st.write(response)