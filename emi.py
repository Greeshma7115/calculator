import streamlit as st
st.header('EMI Calculator')
st.subheader('Enter the loan details to calculate the EMI')
p=st.number_input('Enter the principal amount')
t=st.number_input('Enter the tenure in years')
r=st.number_input('Enter the rate of interest')
if st.button('Calculate EMI'):
    i=(p*t*r)/100
    st.write(f'The interest is: {i}')