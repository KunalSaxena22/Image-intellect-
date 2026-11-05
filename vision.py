"""Streamlit application for educational medical-image explanations."""

import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

load_dotenv()

DEFAULT_MODEL = "gemini-3.8-flash"
ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png"}

SYSTEM_PROMPT = """
You help users understand the visible contents of medical images and documents
for educational purposes. Answer the user's question in clear, cautious language.
Do not diagnose a condition, prescribe medication, or recommend treatment.
Distinguish visible observations from uncertainty, and explain when image quality
or missing context limits the answer. Remind users that a qualified healthcare
professional must interpret medical findings and make care decisions.
"""


def input_image_setup(uploaded_file):
    """Convert a Streamlit upload into a Gemini image part."""
    if uploaded_file is None:
        raise ValueError("Please upload a JPG, JPEG, or PNG image.")

    mime_type = getattr(uploaded_file, "type", None)
    if mime_type not in ALLOWED_IMAGE_TYPES:
        raise ValueError("Unsupported image type. Please upload a JPG or PNG file.")

    image_bytes = uploaded_file.getvalue()
    if not image_bytes:
        raise ValueError("The uploaded image is empty.")

    return types.Part.from_bytes(data=image_bytes, mime_type=mime_type)


def get_gemini_response(input_text, image_part, prompt=SYSTEM_PROMPT):
    """Generate an educational explanation using the Gemini Developer API."""
    api_key = os.getenv("GOOGLE_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY is not set. Add your Gemini API key to the .env file."
        )

    model_name = os.getenv("GEMINI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model_name,
        contents=[prompt, input_text, image_part],
    )

    response_text = getattr(response, "text", None)
    if not response_text:
        raise RuntimeError(
            "Gemini returned no text. Try another image or a more specific question."
        )

    return response_text


# Streamlit page
st.set_page_config(page_title="Medical Intellect", layout="wide")

with st.sidebar:
    st.title("About")
    st.info(
        "Medical Intellect explains content in uploaded medical images for "
        "educational purposes. It is not a diagnostic tool and cannot replace "
        "a qualified healthcare professional."
    )
    st.caption(
        "Only upload images or documents you are authorized to share. "
        "Avoid including unnecessary personal or patient-identifying information."
    )

st.title("Medical Intellect")
st.subheader("AI-assisted medical image explanations")
st.warning(
    "For education only — do not use this application to diagnose, treat, or "
    "make urgent healthcare decisions. AI-generated responses can be inaccurate."
)

input_text = st.text_input(
    "What would you like to understand about the image?",
    key="input",
    placeholder="For example: Explain the visible labels in this report.",
)
uploaded_file = st.file_uploader(
    "Upload a medical image",
    type=["jpg", "jpeg", "png"],
    help="Supported formats: JPG, JPEG, and PNG.",
)

if uploaded_file is not None:
    try:
        preview = Image.open(uploaded_file)
        preview.verify()
        uploaded_file.seek(0)
        st.image(
            Image.open(uploaded_file),
            caption="Uploaded image",
            use_container_width=True,
        )
        uploaded_file.seek(0)
    except Exception:
        st.error("The uploaded file could not be read as a valid image.")

if st.button("Explain this image", key="submit"):
    if uploaded_file is None or not input_text.strip():
        st.error("Please upload an image and enter a question.")
    else:
        try:
            image_part = input_image_setup(uploaded_file)
            with st.spinner("Generating an explanation..."):
                response = get_gemini_response(input_text.strip(), image_part)
            st.subheader("Educational explanation")
            st.write(response)
        except Exception as error:
            st.error(f"Unable to generate an explanation: {error}")

st.info(
    "Upload an image and ask a question to get a plain-language explanation. "
    "Always confirm medical findings with a qualified healthcare professional."
)
st.caption("Built by Kunal Saxena · Educational project")
