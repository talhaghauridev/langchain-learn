from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate   
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
import os

load_dotenv()
print(os.curdir)
model =  ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

loader = TextLoader("./langchain-document-loaders/circket.txt",encoding="utf-8")


prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=["poem"]
)

