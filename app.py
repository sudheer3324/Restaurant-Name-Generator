import streamlit as st

from langchain_helper import generate_restaurant_name

st.set_page_config(
    page_title="Restaurant Name Generator",
    page_icon="🍽",
    layout="centered"
)

st.title("🍽 Restaurant Name Generator")

st.write("Generate restaurant names using Groq + LangChain")

cuisine = st.sidebar.selectbox(
    "Choose Cuisine",
    [
        "Indian",
        "Chinese",
        "Italian",
        "Mexican",
        "Thai",
        "Japanese",
        "American",
        "Arabic",
        "Korean"
    ]
)

if st.button("Generate"):

    with st.spinner("Generating..."):

        result = generate_restaurant_name(cuisine)

    st.success("Generated Successfully!")

    st.markdown(result)