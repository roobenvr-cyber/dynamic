import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

VECTOR_DB = "vectorstore"

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=VECTOR_DB,
    embedding_function=embedding
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

NEW_DOC_FOLDER = "data/new_docs"

def update_database():

    files = os.listdir(NEW_DOC_FOLDER)

    for file in files:

        path = os.path.join(NEW_DOC_FOLDER, file)

        loader = TextLoader(path)

        docs = loader.load()

        chunks = splitter.split_documents(docs)

        db.add_documents(chunks)

        os.remove(path)

    db.persist()

    print("Vector database updated successfully.")
