from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model =  ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"]
)

promot2 = PromptTemplate(
 template='Generate a 5 pointer summary from the following text \n {text}',
 input_variables=["text"]
 )

parser = StrOutputParser()

chain = prompt1 | model | parser | promot2 | model | parser

result = chain.invoke("AI replaced human")

print(result)

chain.get_graph().print_ascii()