from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def main():
    llm = ChatOpenAI(
        temperature=0.7,
        model="gpt-3.5-turbo"
    )

    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful AI assistant.
        Answer the user clearly and concisely.

        User question: {question}
        """
    )

    chain = LLMChain(
        llm=llm,
        prompt=prompt
    )

    print("🤖 AI Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Bye! 👋")
            break

        response = chain.run(question=user_input)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()
