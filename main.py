import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from langchain_core.runnables import RunnablePassthrough

from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate

from retriever.retrieval import Retriever

from utils.model_loader import ModelLoader

from prompt_library.prompt import PROMPT_TEMPLATES
   