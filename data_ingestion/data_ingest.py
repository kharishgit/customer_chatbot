from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_converter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["ASTRA_DB_API_ENDPOINT"] = ASTRA_DB_API_ENDPOINT
os.environ["ASTRA_DB_APPLICATION_TOKEN"] = ASTRA_DB_APPLICATION_TOKEN
os.environ["ASTRA_DB_KEYSPACE"] = ASTRA_DB_KEYSPACE

class ingest_data:
    def __init__(self):
        print("Initializing")
        self.embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        self.data_converter = data_converter()
    def data_ingestion(self,status):
        vstore = AstraDBVectorStore(
            embedding = self.embeddings,
            collection_name = 'chatbotecomm',
            token = ASTRA_DB_APPLICATION_TOKEN,
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            namespace = ASTRA_DB_KEYSPACE
            )
        storage = status
        if storage == None:
            docs = self.data_converter.data_trasformation()
            inserted_ids = vstore.add_documents(docs)
        else:
            return vstore
        return vstore,inserted_ids


if __name__ == '__main__':
    data_ingestion = ingest_data()
    vstore = data_ingestion.data_ingestion("Not None")
    # print(inserted_ids)
    result = vstore.similarity_search("Can you tell me the low budget phone")
    for res in result:
        print(f"{res.page_content}**{res.metadata}")