from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
import PyPDF2 as pdf
from PIL import Image 
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-1.0-pro')
    response=model.generate_content([input,pdf_content[0],prompt]) #gemini response function when  we insert data bytes
    return response.text


def input_pdf_setup(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text
    
st.set_page_config(page_title="ats website")
st.header("ATS System")
input_text=st.text_area("Job description: ",key="input")
uploaded_file=st.file_uploader("upload your resume ",type="pdf",help="Upload your resume in PDF format")

if uploaded_file is not None:
    st.write("Success")
submit1=st.button("Sumarize my resume")

submit2=st.button("My Skills are good enough for job?")

submit3=st.button("Score my resume")

input_prompt1="""You are an experienced HR manager with tech experience in one of the field of technology 
        such as data science or articial intelligence or web development or fullstack development or software development
        .Your role is to scrutinize the resume on light of the job description provided.Check whether the
        technologies used in projects done by the candidate is suitable for the job.Share your insights on the candidate's suitablility
        for the role from the HR manager perspective Additionally,Offer advice on Enhancing the candidate's skills and identify area of weakness"""
   
input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""
input_prompt2=""" You are an experienced HR manager with tech experience in one of the field of technology 
        such as data science or articial intelligence or web development or fullstack development or software development
        .Your role is to Check whether the technologies used in projects mentioned on the Project or experience section in the resume
        by the candidate is suitable for the job description or not"""
if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")




