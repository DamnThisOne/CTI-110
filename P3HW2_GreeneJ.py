
# python -m streamlit run P3HW2_GreeneJ.py
# python -m pip install streamlit
import streamlit as st

name = st.text_input("Enter employee name: ")
Hrs = st.number_input("Enter hours worked: ")
pay = st.number_input("Enter hourly pay rate: $")