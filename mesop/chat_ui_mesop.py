import google.generativeai as genai
from typing import List
import os

# Configure the API key (ensure this is handled securely in production)
genai.configure(api_key="XXX")  # Replace with your actual key

import mesop as me
import mesop.labs as mel

generation_config = {
    "temperature": 0.5,
    "max_output_tokens": 1000000,  # Updated key name
    "top_p": 1,
    "top_k": 1,
}

# Create the model (no need for 'name' argument)
model = genai.GenerativeModel(generation_config=generation_config)

@me.page(
    path="/chat",
    title="SIA 63",
    stylesheets=["https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"],
)

def page():
    mel.chat(transform, title="SIA 63", bot_user="SIA 63")

def transform(input: str, history: List[mel.ChatMessage]):
    response = model.generate_text(prompt=input)  # Use generate_text() directly
    yield response.result  # Return the generated text
