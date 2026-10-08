
# python -m streamlit run P3HW2_GreeneJ.py
# python -m pip install streamlit
import streamlit as st

name = st.text_input("Enter employee name: ")
Hrs = st.number_input("Enter hours worked: ")
pay = st.number_input("Enter hourly pay rate: $")

if Hrs > 40:
    print("You had some overtime .")
    OT_Hrs = Hrs - 40
    reg_Hrs = 40
    OT_Pay = (pay * 1.5) * OT_Hrs
    reg_pay = reg_Hrs * pay
    PayDay = reg_pay + OT_Pay

else:
    print("You hit quota .")
    OT_Hrs = 0
    reg_Hrs = Hrs
    OT_Pay = 0
    reg_pay = reg_Hrs * pay
    PayDay = reg_pay + OT_Pay
    
st.write(f"Hours worked: {Hrs:.1f}")
st.write(f"Pay rate: ${pay:.2f}")
st.write(f"Hours worked: {Hrs:.1f}")
st.write(f"Overtime hours: {OT_Hrs:.1f}")
st.write(f"Overtime pay: ${OT_Pay:.2f}")
st.write(f"Regular pay: ${reg_pay:.2f}")
st.write(f"-----------------------------------------------")
st.write(f"Gross pay: ${PayDay:.2f}")

