import os
from dotenv import load_dotenv


from langchain_ollama.llms import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# load

# from langchain_openai import ChatOpenAI
load_dotenv()


## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are not a helpful assistant. Please respond to the question asked in a sarcastic way, try to give wrong answer only."),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain Demo With Gemma Model")
input_text=st.text_input("What question you have in mind?")


## Ollama Llama2 model
llm=OllamaLLM(model="llama3.2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

response = ""

if st.button("Enter"):
    if input_text:
        st.write(chain.invoke({"question":input_text}))
    else:
        response = ""


