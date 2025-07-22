import os
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

def get_transcript_details(url):
    try:
        v_id = url.split("v=")[1].split("&")[0]
        Transcript_text = YouTubeTranscriptApi.get_transcript(v_id)
        transcript = " ".join([i["text"] for i in Transcript_text])
        return transcript
    except Exception as e:
        raise e

def get_summary(text, language):
    if language == "English":
        prompt = "Summarize the following YouTube transcript in a para within 100 words:\n\n"
    elif language == "Hindi":
        prompt = "इस YouTube ट्रांसक्रिप्ट को 100 शब्दों के भीतर एक अनुच्छेद में हिंदी में संक्षेप करें:\n\n"
    elif language == "Telugu":
        prompt = "ఈ YouTube ట్రాన్స్క్రిప్ట్‌ను 100 పదాల లోపు ముఖ్యాంశాలుగా తెలుగులో సంగ్రహించండి:\n\n"
    
    model = genai.GenerativeModel("models/gemini-2.5-pro")
    response = model.generate_content(prompt + text)
    return response.text.strip()

# Streamlit UI
st.title("🎥 YouTube Video Summarizer (Multilingual - Gemini Pro)")

video_url = st.text_input("Enter YouTube Video URL:")

language = st.radio("Choose summary language:", ("English", "Hindi", "Telugu"))

if st.button("Summarize"):
    try:
        transcript_t = get_transcript_details(video_url)
        if transcript_t:
            st.success("Transcript Fetched")
            summary = get_summary(transcript_t, language)
            lang_code = {"English": "en", "Hindi": "hi", "Telugu": "te"}
            obj = gTTS(text=summary, lang=lang_code[language])

            obj.save("b.mp3")
            st.subheader(f"Summary in {language}:")
            st.write(summary)
            audio_file = open('b.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
        else:
            st.warning("Transcript is empty or not available")
    except Exception as e:
        st.error(f"An error occurred: {e}")
