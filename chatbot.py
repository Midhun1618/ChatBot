from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

def main():
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
        - Add ONE extra helpful fact or tip related to the topic
        - No unnecessary fluff
        """
    }

    llm = ChatOpenAI(
        model="openai/gpt-3.5-turbo",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENAI_API_KEY")

    )

    character = input("Choose character (default/robot/teacher/harry/professor): ").lower()

    def get_prompt(character):
        base_prompt = CHARACTER_PROMPTS.get(character, CHARACTER_PROMPTS["default"])

        return ChatPromptTemplate.from_template(
            f"""
            {base_prompt}

            User question: {{question}}
            """
        )


    print("🤖 AI Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Bye! 👋")
            break

        prompt = get_prompt(character)
        messages = prompt.format_messages(question=user_input)
        response = llm.invoke(messages)

        print(f"Bot: {response.content}\n")

if __name__ == "__main__":
    main()