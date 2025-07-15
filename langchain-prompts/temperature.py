from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.9)

result = llm.invoke("Write a five line poem on circket")

print(result.content)