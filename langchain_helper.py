import os

import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    api_key = st.secrets["GROQ_API_KEY"]

llm = ChatGroq(
    groq_api_key=api_key,
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert restaurant branding consultant."),
        (
            "human",
            """Suggest one attractive restaurant name for a {cuisine} restaurant.

Also provide exactly five menu items.

Format:

Restaurant Name:
<name>

Menu Items:
1.
2.
3.
4.
5.
"""
        ),
    ]
)

chain = prompt | llm


def generate_restaurant_name(cuisine):
    response = chain.invoke({"cuisine": cuisine})
    return response.content