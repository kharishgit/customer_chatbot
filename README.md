Customer Chatbot
A FastAPI-based chatbot that answers customer queries about products using a retrieval-augmented generation (RAG) pipeline. The chatbot processes product reviews from a dataset, stores them in an AstraDB vector store, and uses Google Generative AI embeddings to retrieve relevant information. The frontend provides a simple chat interface for users to interact with the bot.
Table of Contents

Features
Project Structure
Prerequisites
Setup
Running the Application
Usage
Data Ingestion
Configuration
Contributing
License

Features

Product Query Handling: Answers user queries about products (e.g., "Can you suggest a good budget laptop?") based on product reviews.
RAG Pipeline: Uses LangChain to retrieve relevant documents from an AstraDB vector store and generate responses with an LLM.
FastAPI Backend: Provides a RESTful API with a /get endpoint for chat interactions.
Web Interface: A simple HTML-based chat interface styled with CSS.
Scalable Vector Store: Stores product review embeddings in AstraDB for efficient retrieval.
Configurable: Supports configuration via a config.yaml file and environment variables.

Project Structure
customer_chatbot/
├── main.py                   # FastAPI application entry point
├── retriever/
│   └── retrieval.py          # Document retrieval using AstraDBVectorStore
├── utils/
│   └── model_loader.py       # Loads embedding models and LLM
├── config/
│   ├── config_loader.py      # Loads configuration from config.yaml
│   └── config.yaml           # Configuration file (e.g., collection name, retriever settings)
├── data/
│   └── flipkart_product_review.csv  # Dataset with product reviews
├── data_ingestion/
│   └── injection_pipeline.py # Data ingestion pipeline for AstraDB
├── prompt_library/
│   └── prompt.py             # Prompt templates for the chatbot
├── static/
│   └── style.css             # CSS for the chat interface
├── templates/
│   └── chat.html             # HTML template for the chat interface
├── .env                      # Environment variables (not tracked in Git)
├── README.md                 # Project documentation
└── .gitignore                # Git ignore file

Prerequisites

Python: Version 3.10 or higher.
Conda: For managing the Python environment.
AstraDB Account: Required for the vector store. Sign up at DataStax AstraDB.
Google Cloud API Key: Required for Google Generative AI embeddings. Obtain from Google Cloud Console.
Dataset: A CSV file (flipkart_product_review.csv) with columns product_title, rating, summary, and review.

Setup

Clone the Repository:
git clone https://github.com/kharishgit/customer_chatbot.git
cd customer_chatbot


Create and Activate Conda Environment:
conda create -n chatbot python=3.10
conda activate chatbot


Install Dependencies:Install the required Python packages using pip:
pip install fastapi uvicorn langchain langchain-astradb langchain-google-genai python-dotenv pandas pyyaml jinja2

Alternatively, if you have a requirements.txt file, run:
pip install -r requirements.txt


Set Up Environment Variables:Create a .env file in the project root and add the following:
GOOGLE_API_KEY=<your-google-api-key>
ASTRA_DB_API_ENDPOINT=<your-astra-db-api-endpoint>
ASTRA_DB_APPLICATION_TOKEN=<your-astra-db-token>
ASTRA_DB_KEYSPACE=<your-astra-db-keyspace>

Replace the placeholders with your actual credentials. Do not commit the .env file to Git.

Prepare the Dataset:Ensure the data/flipkart_product_review.csv file is in the data/ directory. The CSV should have the following columns:

product_title: Name of the product.
rating: Product rating (e.g., 4.5).
summary: Summary of the review.
review: Full review text.


Configure the Application:Verify the config.yaml file in the config/ directory. It should include:
astra_db:
  collection_name: chatbotecomm
retriever:
  top_k: 3

Adjust the collection_name and top_k as needed.


Running the Application

Ingest Data (Optional):If the AstraDB vector store is not yet populated, run the data ingestion pipeline to load product reviews:
python data_ingestion/injection_pipeline.py

This script transforms the CSV data into LangChain Document objects and stores them in AstraDB.

Start the FastAPI Server:Run the application using Uvicorn:
uvicorn main:app --reload --port 8001


--reload: Enables auto-reload for development.
--port 8001: Runs the server on port 8001.


Access the Chat Interface:Open a browser and navigate to:
http://127.0.0.1:8001

This loads the chat interface (chat.html) where you can enter queries.


Usage

Chat Interface:
Enter a query (e.g., "Can you suggest a good budget laptop?") in the chat interface.
The chatbot retrieves relevant product reviews from AstraDB and generates a response using the RAG pipeline.


API Endpoint:
Send a POST request to the /get endpoint to interact with the chatbot programmatically:curl -X POST -F "msg=What are the best headphones?" http://127.0.0.1:8001/get


The response will be the chatbot’s answer based on the retrieved reviews.



Data Ingestion
The data_ingestion/injection_pipeline.py script handles the ingestion of product reviews into AstraDB:

Reads flipkart_product_review.csv.
Transforms reviews into LangChain Document objects with metadata (product name, rating, summary).
Embeds documents using Google Generative AI (models/embedding-001).
Stores embeddings in an AstraDB vector store (chatbotecomm collection).

To re-run ingestion (e.g., after updating the CSV):
python data_ingestion/injection_pipeline.py

Configuration

Environment Variables (.env):
GOOGLE_API_KEY: For Google Generative AI embeddings.
ASTRA_DB_API_ENDPOINT: AstraDB API endpoint URL.
ASTRA_DB_APPLICATION_TOKEN: AstraDB authentication token.
ASTRA_DB_KEYSPACE: AstraDB keyspace (e.g., default_keyspace).


Config File (config.yaml):
astra_db.collection_name: Name of the AstraDB collection (e.g., chatbotecomm).
retriever.top_k: Number of documents to retrieve for each query (default: 3).



Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make changes and commit (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

Please ensure your code follows the project’s style and includes tests where applicable.
License
This project is licensed under the MIT License. See the LICENSE file for details.
