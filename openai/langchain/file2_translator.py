# Multiple inputs and the application is a language converter.

import time
import streamlit as st
from constants import openai_key
from langchain_openai import OpenAI  # Update import statement
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

st.title("OpenAI Search")
sentence_to_translate = st.text_input("Enter the sentence to translate:")
target_language = st.text_input("Enter the target language:")

llm = OpenAI(openai_api_key=openai_key, temperature=0.7)  # Update instantiation
prompt = PromptTemplate(input_variables=['sentence', 'language'],
                        template="Translate this sentence {sentence} into {language}")
chain = LLMChain(llm=llm, prompt=prompt)

# Translate button
if st.button("Translate"):
    with st.spinner("Translating..."):
        result = chain.invoke({'sentence': sentence_to_translate, 'language': target_language})
        st.success(result)
