import streamlit as st
import time
from constants import openai_key
from langchain_openai import OpenAI  # Update import statement
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory



st.title('Person Information Explorer')
input_text = st.text_input("Search the topic you want")

llm = OpenAI(openai_api_key=openai_key, temperature=0.8)

# First Prompt: Gathering information about the person
first_input_prompt = PromptTemplate(input_variables=['name'], template="Tell me about {name}. What is their background, profession, or notable achievements?")
person_memory=ConversationBufferMemory(input_key='name')
chain1 = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person',memory=person_memory)


# Second Prompt: Inquiring about the date of birth
second_input_prompt = PromptTemplate(input_variables=['person'], template="When was {person} born?")
dob_memory=ConversationBufferMemory(input_key='person')
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob',memory=dob_memory)

# Third Prompt: Exploring events in the same year
third_input_prompt = PromptTemplate(input_variables=['dob'], template="Mention 5 significant events that happened in the year {dob}.")
descr_memory=ConversationBufferMemory(input_key='dob')
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description',memory=descr_memory)

# Fourth Prompt: Reusing the name information
fourth_input_prompt = PromptTemplate(input_variables=['name', 'description'], template="Provide additional details about {name} based on the events mentioned earlier in the year {dob}.")
info_memory=ConversationBufferMemory(input_key='dob')
chain4 = LLMChain(llm=llm, prompt=fourth_input_prompt, verbose=True, output_key='additional_info',memory=info_memory)


# Creating the Sequential Chain
parent_chain = SequentialChain(chains=[chain1, chain2, chain3, chain4], input_variables=['name'],
                                output_variables=['person', 'dob', 'description', 'additional_info'],
                                verbose=True)

# Handling user input and executing the chain
if input_text:
    try:
        result = parent_chain({'name': input_text})
        st.write(result)
        with st.expander('Person Name'): 
              st.info(person_memory.buffer)
        with st.expander('Date of Birth'):
              st.info(dob_memory.buffer)      
        with st.expander('Major Events'): 
              st.info(descr_memory.buffer)
        with st.expander('Additional events'): 
              st.info(info_memory.buffer)
    except Exception as e:
        if "429" in str(e):
            st.warning("Rate limit reached. Waiting for 20 seconds and retrying...")
            time.sleep(20)
            result = parent_chain({'name': input_text})
            st.write(result)
        else:
            st.error(f"An error occurred: {e}")
