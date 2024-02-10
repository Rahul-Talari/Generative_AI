# conda create -p venv python=3.1 
import streamlit as st
from constants import openai_key
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_models import ChatOpenAI

# Streamlit UI setup
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")


# Initialize ChatOpenAI model
chat = ChatOpenAI(temperature=0.7, openai_api_key=openai_key)
# Initialize session state
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [SystemMessage(content="You are a comedian AI assistant")]
# Function to get model response
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content



input_text = st.text_input("Input: ")
submit = st.button("Ask the question")
# If ask button is clicked
if submit:
    # Get and display the response
    response = get_chatmodel_response(input_text)
    st.subheader("The Response is")
    st.write(response)
