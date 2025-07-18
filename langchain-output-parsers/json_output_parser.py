from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
  repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
      template='Give me 5 facts about {topic} \n {format_instruction}',
      input_variables=["topic"],
      partial_variables={"format_instruction":parser.get_format_instructions()}

)
chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
