from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    llm = ChatOpenAI(
        model="openai/gpt-3.5-turbo",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENAI_API_KEY")
    )


    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful AI assistant.
        Answer the user clearly and concisely.

        User question: {question}
        """
    )

    print("🤖 AI Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Bye! 👋")
            break

        messages = prompt.format_messages(question=user_input)
        response = llm.invoke(messages)

        print(f"Bot: {response.content}\n")

if __name__ == "__main__":
    main()
