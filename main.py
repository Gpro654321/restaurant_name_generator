import os

import streamlit as st

from langchain_helper import generate_restaurant_name_and_items
import config



# the sidebar code
with st.sidebar:
    api_key = st.text_input(
        "Input openai key",
        key="openai_input",
        value="Input openai key here",
        type="password"
    )

st.session_state['api_key'] = api_key

# title anc its caption
st.title("Restaurant Name Generator")
st.caption("Generate Restaurant Names with OpenAI")

# selectbox for the type of cuisine selection
cuisine = st.selectbox(
        "Pick a Cuisine",
        options = config.restaurant_types,

    )

# if the cuisine is NOT the default "-"
if cuisine != "-":

    #if the user has input his / her key
    if not api_key:
        print("Inside if not api_key")
        print(api_key)
        st.info("Please input your OpenAI api key to continue")
        st.stop()

    print("after if not api_key")
    print(api_key)
    try:
        response = generate_restaurant_name_and_items(cuisine)
        st.header(response['restaurant_name'].strip())
        menu_items = response['menu_items'].strip().split(",")
        st.write("**Menu Items**")
        for item in menu_items:
            st.write(item)

    except:
        st.info("Input correct API key")