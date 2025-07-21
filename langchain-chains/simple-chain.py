from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model =  ChatGoogleGenerativeAI(model="gemini-2.0-flash")


prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke("circket")

print(result)

chain.get_graph().print_ascii()