from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os 
from PIL import Image
import pdf2image 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text
def input_pdf_setup(uploaded_file):
    images=pdf2image.convert_from_bytes(uploaded_file.read())
    first=images[0]
    img_byte_arr=io.BytesIO()
    first.save(img_byte_arr,format='JPEG')
    img_byte_arr=img_byte_arr.getvalue()
