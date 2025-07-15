from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",dimensions=10)

documents = [
    "The Eiffel Tower is an iron lattice tower located in Paris, France.",
    "Mount Everest is Earth's highest mountain above sea level, located in the Himalayas.",
    "The Great Barrier Reef is the world's largest coral reef system, off the coast of Queensland, Australia."
]

query = 'tell me about Everest'

docs_embeddings = embeddings.embed_documents(documents)
query_embeddings = embeddings.embed_query(query)

scores =cosine_similarity([query_embeddings],docs_embeddings)[0]
index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(scores)
print(query)
print(documents[index])
print("similarity score is:", score)