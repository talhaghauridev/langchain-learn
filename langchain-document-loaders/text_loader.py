from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=["poem"],
)

loader = TextLoader("./langchain-document-loaders/circket.txt", encoding="utf-8")

docs = loader.load()

print(type(docs))
print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | parser

result = chain.invoke({"poem": docs[0].page_content})

print("AI Result: ", result)
