# image intellect

from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Image Demo", layout="wide")

# Sidebar with an "About" section
with st.sidebar:
    st.title("About")
    st.info("""
        **Medical Intellect** is an AI-powered application for medical image analysis.
        
        **How it works:**
        1. **Input Prompt**: Enter a textual prompt that describes what you want the AI to do.
        2. **Upload Image**: Upload a medical image (e.g., x-ray, MRI, medical document).
        3. **Get Response**: Click the "Tell me about the image" button to get a detailed analysis based on the input prompt and image.
        
        **Powered by Google Generative AI:**
        This application utilizes the Gemini model from Google's Generative AI API to analyze the input image and provide accurate responses based on the prompt.
    """)

# Page title and header
st.title("Medical Intellect")
st.subheader("AI-powered Medical Image Analysis")

# Input prompt and image uploader
input_text = st.text_input("Enter your prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], help="Upload a medical image for analysis")

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Define input prompt
input_prompt = """
     you are an expert in medical field 
     you will recieve input images of medical as invoices &
     you will have to answer questions based on the input image with accuracy
"""

# Create a two-column layout for better alignment
col1, col2 = st.columns([2, 1])

with col1:
    if st.button("Tell me about the image", key="submit"):
        if uploaded_file is not None and input_text.strip():
            try:
                # Display progress message
                with st.spinner("Generating response..."):
                    image_data = input_image_setup(uploaded_file)
                    response = get_gemini_response(input_text, image_data, input_prompt)
                
                # Display the response
                st.success("The Response is:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please provide both an input prompt and an image.")

with col2:
    st.info("Upload an image and enter a prompt to get started. The AI will analyze the image and provide relevant information.")

# Footer for additional information or credits
st.markdown("This project is intended for educational purposes and is currently in the testing phase.")
st.markdown("Built by Kunal Saxena.")










# # # image intellect

# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env.

# import streamlit as st
# import os
# import pathlib
# import textwrap
# from PIL import Image


# import google.generativeai as genai
# # 

# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Function to load OpenAI model and get respones

# def get_gemini_response(input,image,prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input,image[0],prompt])
#     return response.text
    

# def input_image_setup(uploaded_file):
#     # Check if a file has been uploaded
#     if uploaded_file is not None:
#         # Read the file into bytes
#         bytes_data = uploaded_file.getvalue()

#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
#                 "data": bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError("No file uploaded")


# ##initialize our streamlit app

# st.set_page_config(page_title="Gemini Image Demo")

# st.header("Medical Intellect")
# input=st.text_input("Input Prompt: ",key="input")
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# image=""   
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
    
#     st.image(image, caption="Uploaded Image.", use_column_width=True)


# submit=st.button("Tell me about the image")

# input_prompt = """
#             #    You are an expert in understanding invoices.
#             #    You will receive input images as invoices &
#             #    you will have to answer questions based on the input image
                 
            
#             you are an expert in medical field 
#             you will recieve input images of medical as invoices &
#             you will have to answer questions based on the input image with accuracy
#                """

# ## If ask button is clicked

# if submit:
#     image_data = input_image_setup(uploaded_file)
#     response=get_gemini_response(input_prompt,image_data,input)
#     st.subheader("The Response is")
#     st.write(response)