from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CHARACTER_PROMPTS = {
    "default": "You are a helpful AI assistant. Answer clearly and concisely.",

    "robot": (
        "You are a robot assistant. "
        "No jokes. No extra explanation. "
        "Short, factual answers only."
    ),

    "teacher": (
        "You are a gentle and motivating teacher. "
        "Explain step by step and encourage the user."
    ),

    "harry": (
        "You are Harry. "
        "Sarcastic, funny, high energy, slightly dramatic. "
        "Friendly roasting allowed but still helpful."
    ),

    "professor": (
        "You are a sharp professor. "
        "Use crisp bullet points, precise explanations, "
        "and add ONE extra helpful fact."
    ),
}

<<<<<<< HEAD
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    default_headers={
        "HTTP-Referer": "https://chatbotvox.onrender.com",
        "X-Title": "VoxCom Chatbot",
    }
)


def build_prompt(character: str):
    base_prompt = CHARACTER_PROMPTS.get(character, CHARACTER_PROMPTS["default"])

    return ChatPromptTemplate.from_template(
        f"""
        {base_prompt}

        User question: {{question}}
        """
    )

=======
>>>>>>> 9ff16e0 (working version)
@app.get("/")
def health():
    return {"status": "Chatbot API running 🚀 (Gemini)"}

@app.post("/chat")
def chat(message: str, character: str = "default"):
    system_prompt = CHARACTER_PROMPTS.get(
        character, CHARACTER_PROMPTS["default"]
    )

    model = genai.GenerativeModel("gemini-flash-lite-latest")

    prompt = f"""{system_prompt}

User question:
{message}
"""

    response = model.generate_content(prompt)

    return {
        "reply": response.text,
        "character": character
    }
