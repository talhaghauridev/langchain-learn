from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./langchain-document-loaders/pdfs/dl-curriculum.pdf")


docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)
