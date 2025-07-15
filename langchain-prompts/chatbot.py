from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = [SystemMessage(content="You are a helpful AI assistant.")]

print("💬 Start chatting with the AI (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in {"exit", "quit"}:
        print("👋 Exiting chat.")
        break
    elif not user_input:
        print("Please enter a message.")
        continue 

    chat_history.append(HumanMessage(content=user_input))

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))

    print("AI:", response.content)

print("\n📝 Chat Summary:")
for msg in chat_history[1:]: 
    role = "You" if isinstance(msg, HumanMessage) else "AI"
    print(f"{role}: {msg.content}")
