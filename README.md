# Medical Intellect

Medical Intellect is an educational Streamlit application that uses Google's Gemini API to explain content visible in uploaded medical images. It accepts JPG, JPEG, and PNG files and lets users ask a question about the image.

> **Medical safety:** This project is an educational aid, not a medical device. AI-generated explanations can be incomplete or inaccurate. Do not use the output to diagnose, prescribe, or make treatment or emergency decisions. A qualified healthcare professional must interpret medical findings.

## Features

- Upload and preview JPG, JPEG, and PNG images.
- Ask a question about the uploaded image.
- Generate a plain-language explanation with the Gemini API.
- Configure the Gemini API key through an environment file.
- Choose a Gemini model using the optional `GEMINI_MODEL` setting.

## Requirements

- Python 3.10 or newer.
- A Gemini API key.
- The Python packages listed in `requirements.txt`.

## Installation

Clone this repository:

~~~bash
git clone https://github.com/KunalSaxena22/Image-intellect-.git
cd Image-intellect-
~~~

Create a virtual environment and install the runtime dependencies.

**Windows PowerShell:**

~~~powershell
py -3.10 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
~~~

These commands call the virtual environment's Python executable directly, so PowerShell activation is not required.

**macOS / Linux:**

~~~bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
~~~

Create your local environment file:

~~~bash
cp .env.example .env
~~~

On Windows, use `Copy-Item .env.example .env` in PowerShell instead. Open `.env` and set your key:

~~~dotenv
GOOGLE_API_KEY=your_gemini_api_key
# Optional; defaults to gemini-3.8-flash
GEMINI_MODEL=gemini-3.8-flash
~~~

Do not commit your real `.env` file or share your API key.

## Run the app

Run the application from the repository root:

~~~bash
# Windows PowerShell
.\.venv\Scripts\python.exe -m streamlit run vision.py

# macOS / Linux (after activating .venv)
streamlit run vision.py
~~~

Streamlit prints a local URL (normally `http://localhost:8501`) that you can open in your browser.

## How to use

1. Start the Streamlit application.
2. Upload a JPG, JPEG, or PNG image.
3. Enter a specific question about the visible content.
4. Select **Explain this image**.
5. Review the generated explanation and confirm any medical information with a qualified healthcare professional.

Only upload images or documents you are authorized to share. Avoid including unnecessary patient-identifying information.

## Technology

- Python and Streamlit
- Google Gen AI Python SDK (`google-genai`)
- Gemini multimodal models
- Pillow
- python-dotenv

## Contributing

Bug reports and tested pull requests are welcome. Include clear reproduction steps and avoid sharing API keys, private patient information, or identifiable medical images in issues and pull requests.

## Maintainer

Kunal Saxena — [@KunalSaxena22](https://github.com/KunalSaxena22)
