import streamlit as st

def print_x_block(times):
    x_row = "XXXXX" * 1000000  # Much smaller row
    for _ in range(times):
        st.text(x_row)

st.title("X Printer 3000 🚀")

if st.button("Unleash the Xs"):
    print("your cooked womp womp maka maka")
    print_x_block(1000000)  # Reasonable number of rows

