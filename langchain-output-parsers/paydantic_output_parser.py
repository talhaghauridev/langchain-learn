from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
  repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str = Field(description="Name of the person")
    age:int = Field(description="Age of the person")
    city:str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person,)


template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain = template | model | parser

result = chain.invoke({'place':'pakistan'})

print(result)
