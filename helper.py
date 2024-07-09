from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

api_key = "AIzaSyDJIOoxpdNIGEGXG_MjjBej6MMhfvPVJVg"

llm = GooglePalm(google_api_key=api_key,temperature=0.9)

def resturant_name_and_items(cuisine):
    api_key = "AIzaSyDJIOoxpdNIGEGXG_MjjBej6MMhfvPVJVg"
    llm = GooglePalm(google_api_key=api_key, temperature=0.9)

    prompt_template_name = PromptTemplate(
        input_variables=['dish'],
        template="I want to open a {dish} Restaurant, suggest me the best name for it. Return only one name."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="res_name")

    prompt_template_menu = PromptTemplate(
        input_variables=['res_name'],
        template="Suggest me menu items for {res_name}. Return them as comma separated."
    )
    resturant_chain = LLMChain(llm=llm, prompt=prompt_template_menu, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, resturant_chain],
        input_variables=['dish'],
        output_variables=['res_name', 'menu_items']
    )

    response = chain({'dish': cuisine})
    return response
