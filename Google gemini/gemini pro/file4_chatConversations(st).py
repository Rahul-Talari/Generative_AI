# import google.generativeai as genai
# from constants import api_key
# import streamlit as st

# genai.configure(api_key=api_key)
# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])

# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history']=[]

# st.set_page_config(page_title="Q&A Demo")
# st.header("Gemini LLM Application")
# user_input=st.text_input("Input: ",key='input')
# submit=st.button("Ask the Question")

# if submit and input:
#     st.session_state['chat_history'].append(('you',user_input))
#     st.subheader("The response is:")
#     response =chat.send_message(user_input, stream=True)
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(('Bot',chunk.text))

# with st.expander("Chat History"):        
#     for role,text in st.session_state['chat_history']:
#         st.write(f"{role}:{text}")        


import google.generativeai as genai
from constants import api_key
import streamlit as st

# Configure generative AI model and start chat
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Set page configuration
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini_Pro Chatconversation 🤖")
user_input = st.text_input("Input:", key='input')
submit = st.button("Ask the Question")

# Process user input and display response
if submit and user_input:
    st.session_state['chat_history'].append(('you', user_input))
    st.subheader("The response is:")
    
    # Use streamlit's st.spinner for better loading indication
    with st.spinner("Generating response..."):
        response = chat.send_message(user_input, stream=True)
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(('Bot', chunk.text))

# Chat History expander
with st.expander("Chat History"):
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
