import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="moonshotai/Kimi-K2-Instruct",
    task="text-generation",
    huggingfacehub_api_token=token, 
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Pakistan")
print(result)
