import streamlit as st

# Define your pages
tracker = st.Page("page_tracker.py", title="Money", icon="💰")
vision = st.Page("page_vision.py", title="Vision", icon="🚀")
new_idea = st.Page("page_new.py", title="New Project", icon="🌟") # Added this!

# Update Navigation
pg = st.navigation([tracker, vision, new_idea])
pg.run()

