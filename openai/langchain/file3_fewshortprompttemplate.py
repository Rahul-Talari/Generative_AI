import streamlit as st
from langchain_openai import OpenAI  # Update import statement
from constants import openai_key
from langchain.chains import LLMChain
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

st.title('Antonym Finder')

examples = [
    {"word": "happy", "antonym": "Sad"},
    {"word": "up", "antonym": "down"},
    {"word": "right", "antonym": "left"}
]
example_prompt = PromptTemplate(
    input_variables=["word", "antonym"], template="Word: {word} Antonym: {antonym}"
)
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix='Give the antonym of every input',
    suffix="word: {input}",
    input_variables=["input"],
)

llm = OpenAI(temperature=0.7, openai_api_key=openai_key)
chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit UI
word_input = st.text_input("Enter the word:")
if st.button("Find Antonym"):
    if word_input:
        result = chain.invoke({'input': word_input})
        st.write(f"Antonym for '{word_input}': {result['text']}")
    else:
        st.warning("Please enter a word.")
