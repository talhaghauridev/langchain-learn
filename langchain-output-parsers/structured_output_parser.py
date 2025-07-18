from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import ResponseSchema,StructuredOutputParser
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

schema = [
    ResponseSchema(name="fact_1",description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2",description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3",description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
      template='Give me 5 facts about {topic} \n {format_instruction}',
      input_variables=["topic"],
      partial_variables={"format_instruction":parser.get_format_instructions()}

)
chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
