import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("Available models and supported methods:\n")

for model in genai.list_models():
    print(f"Model: {model.name}")
    print(f"  Supported methods: {model.supported_generation_methods}")
    print("-" * 50)
