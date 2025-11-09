import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def create_chatbot():
    """
    Creates a chatbot using the Gemini API.

    Returns:
        GenerativeModel: A Gemini chatbot instance.
    """
    