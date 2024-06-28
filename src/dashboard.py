"""
https://docs.streamlit.io/get-started/fundamentals/main-concepts
"""
from src.scrape_forbes_fintech_50 import construct_fintech_50_dataframe
import streamlit as st


st.set_page_config(page_title="Analytics Dashboard Portfolio")


st.markdown('''
            # Analytics Dashboard Portfolio

            Welcome to my dashboard of various web scraping and data engineering projects. 
            I wanted to find a suitable visualization tool that would serve as an endpoint 
            for the various API data results I've been playing around with. 

            The dashboard is hosted by streamlit, which has fairly intuitive and modern applications. 
            

            -----------

''')

df = construct_fintech_50_dataframe()
st.write('## Forbes Fintech 50!')
st.write('''
            The purpose of this table was to identify the top payments and finance industries
            in order to support my job hunt. 

            I used beautiful soup and a handful of other libraries to accomplish 
            parsing data from the article I found with the following information.

            -----------

''')

st.write(df)

# SIDE BAR NAV
st.sidebar.header("Navigation")
