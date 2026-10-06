import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Create Gemini model
model = genai.GenerativeModel("models/gemini-3.8-flash")


def generate_legal_document(
    document_type,
    parties,
    terms,
    effective_date
):
    prompt = f"""
You are a legal document drafting assistant.

Create a professional draft of the following legal document.

Document Type: {document_type}
Parties: {parties}
Important Terms: {terms}
Effective Date: {effective_date}

Requirements:
- Use clear and professional legal language.
- Organize the document with suitable headings and sections.
- Include the information provided by the user.
- Do not invent important personal or legal facts.
- Return only the document draft.
- Add a note that the document should be reviewed by a qualified legal professional before use.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating document: {str(e)}"
