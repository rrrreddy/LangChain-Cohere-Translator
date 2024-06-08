from typing import List

#import for prompts
from langchain_core.prompts import ChatPromptTemplate
#import for model 
from langchain_cohere import ChatCohere
# import for output parsing
from langchain_core.output_parsers import StrOutputParser
import os
import getpass
from langserve import add_routes

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

load_dotenv()

os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "langchain-cohere-translator"


# 1. Creating Prompt Template

system_template = "Translate the following message/question asked from english into {language} in english language:"

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}")
    ]
)


# 2. invoking model

model = ChatCohere(model="command-r")

# 3. Output Parsing

parser  = StrOutputParser()

# building chain - runnable sequence

chain  = prompt_template | model | parser



# App defination

app = FastAPI(
    title= "langchain-cohere server",
    version= "0.1",
    description= "A simple langchain-cohere API server using LangChain's runnable interface",
)

# Adding chain route

add_routes(
    app,
    chain,
    path="/cohere-translator", 
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

