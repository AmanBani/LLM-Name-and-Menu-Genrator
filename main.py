import streamlit as st
import helper

st.title("Resturant Name Genrator")

dish = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "American", "Mexican", "Arabic", "Russian"))


if dish:
    response = helper.resturant_name_and_items(dish)
    if response:
        st.header(response['res_name'].strip())
        menu_items = response['menu_items'].strip().split(",")
        st.write("***Menu Items***")
        for item in menu_items:
            st.write("-", item)