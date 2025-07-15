from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",dimensions=10)

documents = [
    "Python is a famous library",
    "Python is use in various fields"
    "Numpy is the famous library of Python",
]

result = embeddings.embed_documents(documents)

print(str(result))