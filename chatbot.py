from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CHARACTER_PROMPTS = {
    "default": """
    You are a helpful AI assistant.
    Answer clearly and concisely.
    """,

    "robot": """
    You are a robot assistant.
    Rules:
    - No jokes
    - No extra explanation
    - Straight to the point
    - Short and factual answers only
    """,

    "teacher": """
    You are a gentle and motivating teacher.
    Explain clearly step-by-step.
    Encourage the user.
    Use simple examples when needed.
    """,

    "harry": """
    You are Harry.
    Personality:
    - Sarcastic
    - Funny
    - High energy
    - Slightly dramatic
    - Friendly roasting allowed
    Answer with humor but still be useful.
    """,

    "professor": """
    You are a sharp professor.
    Style:
    - Crisp bullet points
    - Precise explanation
    - Add ONE extra helpful fact or tip
    - No unnecessary fluff
    """
}

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
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

@app.get("/")
def health_check():
    return {"status": "Chatbot API running 🚀"}

@app.post("/chat")
def chat(message: str, character: str = "default"):
    prompt = build_prompt(character)
    messages = prompt.format_messages(question=message)
    response = llm.invoke(messages)

    return {
        "reply": response.content,
        "character": character
    }
