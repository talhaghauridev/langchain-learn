from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

os.environ['HF_HOME'] = 'D:/huggingface_cache'

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Python is a famous library",
    "Python is use in various fields"
    "Numpy is the famous library of Python",
]

result = embeddings.embed_documents(documents)

print(result)