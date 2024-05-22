import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import config
'''

# load the environment variable
load_dotenv()

# access the key
api_key = os.getenv('OPENAI_API_KEY')
'''



def generate_restaurant_name_and_items(cuisine):
    openai_api_key = st.session_state["api_key"]
    if not openai_api_key:
        print("inside if not in langchain_helper function")
        st.info("Please input your OpenAI api key to continue")
        st.stop()

    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food, Suggest a fancy name for this"
    )
    name_chain = LLMChain(llm=llm,
                          prompt=prompt_template_name,
                          output_key='restaurant_name'
                          )

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a commas seperated values"
    )

    food_item_chain = LLMChain(llm=llm,
                               prompt=prompt_template_items,
                               output_key='menu_items'
                               )
    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine':cuisine})

    return response



if __name__  == "__main__":
    print(generate_restaurant_name_and_items("Italian"))