import streamlit as st
import pandas as pd
import numpy as np

st.title('BUDGET - ENSSAT')

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
EM1 = st.text_input("Rent: \n")
EM2 = st.text_input("Rental Caution: \n")
EM3 = st.text_input("Ticket: \n")
EM4 = st.text_input("Other: \n")

st.write('DAILY LIVING')
EM1 = st.text_input("Rent: \n")
EM2 = st.text_input("Rental Caution: \n")
EM3 = st.text_input("Ticket: \n")
EM4 = st.text_input("Other: \n")

st.write('ENTERTAINMENT')
EM1 = st.text_input("Rent: \n")
EM2 = st.text_input("Rental Caution: \n")
EM3 = st.text_input("Ticket: \n")
EM4 = st.text_input("Other: \n")

st.write('HEALTH')
EM1 = st.text_input("Rent: \n")
EM2 = st.text_input("Rental Caution: \n")
EM3 = st.text_input("Ticket: \n")
EM4 = st.text_input("Other: \n")