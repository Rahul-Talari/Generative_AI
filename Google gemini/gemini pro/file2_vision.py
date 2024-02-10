import streamlit as st
import google.generativeai as genai
from constants import api_key
from PIL import Image

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(question,image):
    if(input!=""):
        response=model.generate_content([question,image])
    else :
        response=model.generate_content(image)    
    return response.text

st.set_page_config(page_title="Gemini image Demo")
st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key=input)
upload_file=st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded image",use_column_width=True)


submit=st.button("Tell me about the image")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is:")
    st.write(response)