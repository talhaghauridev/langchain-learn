from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",max_tokens=15,temperature=0.9)

result = llm.invoke("Tell one of the famous library of Python")

print(result.content)
print(result.response_metadata)