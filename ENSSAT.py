import streamlit as st
import pandas as pd
import numpy as np

st.title('BUDGET - ENSSAT')

date = st.date_input("Date: \n")

st.subheader('INCOME')
I1 = st.text_input("Principle Income: \n")
I2 = st.text_input("Other: \n")

st.subheader('EXPENSES')

st.write('MANDATORY')
EM1 = st.text_input("Rent: \n")
EM2 = st.text_input("Rental Caution: \n")
EM3 = st.text_input("Ticket: \n")
EM4 = st.text_input("Other: \n")

st.write('TRANSPORTATION')
ET4 = st.text_input("Other: \n")

st.write('DAILY LIVING')

ED4 = st.text_input("Other: \n")

st.write('ENTERTAINMENT')
EE4 = st.text_input("Other: \n")

st.write('HEALTH')
EH4 = st.text_input("Other: \n")
