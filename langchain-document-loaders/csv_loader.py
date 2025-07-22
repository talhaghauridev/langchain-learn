from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="./langchain-document-loaders/social_network_ads.csv")

docs = loader.load()


for document in docs:
    print(document.metadata)

print(len(docs))
