import streamlit as st

# 1. Setup the Pages
# Make sure the filenames 'page_tracker.py' and 'page_vision.py' 
# match exactly what you uploaded to GitHub!
tracker = st.Page("page_tracker.py", title="Expense Tracker", icon="💰", default=True)
vision = st.Page("page_vision.py", title="Vision Board", icon="🚀")

# 2. Create Navigation
pg = st.navigation([tracker, vision])

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
st.sidebar.title("Welcome, Luca")
st.sidebar.info("System Status: Online 🟢")

password = st.sidebar.text_input("Enter Vault Key", type="password")

if password == "1234": # Change this to your secret key!
    pg.run()
else:
    st.title("🔒 Vault Locked")
    st.info("Please enter the correct key in the sidebar to access your financial data.")
# 3. Run the App
pg.run()


