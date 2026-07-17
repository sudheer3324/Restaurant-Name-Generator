import streamlit as st
from langchain_helper import generate_restaurant_name

st.set_page_config(
    page_title="Restaurant Name Generator",
    page_icon="🍽"
)

st.title("🍽 Restaurant Name Generator")

st.write("Generate restaurant names and menu ideas using Llama 3.2")

cuisine = st.sidebar.selectbox(
    "Choose Cuisine",
    (
        "Indian",
        "Chinese",
        "Italian",
        "Mexican",
        "Thai",
        "Japanese",
        "American",
        "Korean",
        "Arabic"
    )
)

if st.button("Generate"):

    with st.spinner("Generating..."):

        result = generate_restaurant_name(cuisine)

    st.success("Done!")

    st.markdown(result)