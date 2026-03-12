import streamlit as st

st.title("🚀 2026 Vision Board")
st.write("Upload images or write down goals you are saving for!")

goal = st.text_input("What is your next big milestone?")
target = st.number_input("Target Amount ($)", min_value=0)

if st.button("Add to Vision"):
    st.success(f"Goal '{goal}' added! Keep tracking those expenses to get there.")
    st.balloons()

# Simple progress bar demo
st.write("Progress to New Laptop:")
st.progress(65) # 65%