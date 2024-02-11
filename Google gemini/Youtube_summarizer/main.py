import streamlit as st
from constants import api_key
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-pro")

def youtue_transcriber(youtube_link):
    try:
        video_id=youtube_link.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)
        transcript=""
        for i in transcript_text:
            transcript+=" "+i["text"]
        return transcript
    except Exception as e:
        raise e
        
def get_gemini_response(transcribe,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcribe)
    return response.text

prompt="""You are Yotube video summarizer. You will be taking the transcript text
          and summarizing the entire video and providing the important summary in
          points within 250 words. Please provide the summary of the text given here:
       """
        
st.set_page_config("Youtube Summarizer")
st.header("Youtube Summarizer using Gemini PRO🚀")
st.subheader("YouTube Transcript to Detailed Notes Converter")
youtube_link=st.text_input("Enter YouTube Video Link")

if youtube_link:
    video_id=youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
if st.button("Summarize"):
    with st.spinner("Summarizing..."):
        transcript_text=youtue_transcriber(youtube_link)
        if transcript_text:
            summary=get_gemini_response(transcript_text,prompt)
            st.write(summary)
            st.markdown("<p style='text-align:center;'>------Summary----------</p>", unsafe_allow_html=True)

    