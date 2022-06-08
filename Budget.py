import streamlit as st
import pandas as pd
import numpy as np

st.title('Budget - Lennion')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

st.subheader('Income')
stock_name = st.text_input("sskndjjsns: \n")

st.subheader('Expenses')
st.write('somesomsosmosmsmosm')
other = st.text_input("Other: \n")
