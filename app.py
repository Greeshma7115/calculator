import streamlit as st
from calc import *
st.header('Calculator')
st.write('This is app for calculator')
num1 = st.number_input('Enter the first number')
num2 = st.number_input('Enter the second number')
operator = st.selectbox('Select an operator', ['+', '-', '*', '/', '**', '%'])
if st.button('Calculate'):
    try:
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        elif operator == '**':
            result = power(num1, num2)
        elif operator == '%':
            result = modulus(num1, num2)
        st.success(f"{result}")
    except ValueError as e:
        st.error(f"Error: {e}. Please try again.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}. Please try again.")
