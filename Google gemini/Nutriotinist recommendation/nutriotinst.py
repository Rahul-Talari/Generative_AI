
### Health Management APP
from constants import api_key
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=api_key)

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input_prompt,image):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    image_data=input_image_setup(uploaded_file)

submit=st.button("Tell me the total calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
Finally you can also mention whether the food is healthy or not and also mention the 
percentage split of the ratio of carbohydrates,fats,fibers,sugars,and other important things important in our diet.
"""
## If submit button is clicked
if submit:
    response=get_gemini_repsonse(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)

input=st.text_input("Ask Question: ",key="input")
submit=st.button("get")
if submit:
    response=get_gemini_repsonse(input,image_data)
    st.subheader("The Response is")
    st.write(response)
