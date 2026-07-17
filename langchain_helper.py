from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model="llama3.2",
    temperature=0.7
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert restaurant branding consultant."
        ),
        (
            "human",
            """
Suggest one attractive restaurant name for a {cuisine} restaurant.

Then provide exactly five menu items.

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
    response = chain.invoke(
        {
            "cuisine": cuisine
        }
    )
    return response.content