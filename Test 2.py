import streamlit as st
time == "100000000"

def print_x_block(times):
    x_row = "X" * 10000000  # Much smaller row
    for _ in range(times):
        st.text(x_row)

st.title("X Printer 3000 🚀")

if st.button("Unleash the Xs"):
    print("your cooked womp womp maka maka")
    for _ in range(time):
        print_x_block(10000000)  # Reasonable number of rows

