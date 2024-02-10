#Integrate your openAI API code

from constants import openai_key
from langchain_openai import OpenAI  # Update import statement
import streamlit as st
from langchain import PromptTemplate
llm=OpenAI(openai_api_key=openai_key,temperature=0.8)

st.title('Langchain with OPENAI API')
input_text=st.text_input("Search the topic you want")
if input_text:
    st.write(llm.invoke(input_text))