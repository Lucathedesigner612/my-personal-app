import streamlit as st
import pandas as pd
import os

# Define the file
DB_FILE = "spending_data.csv"

# Check if file exists and has content
if os.path.exists(DB_FILE) and os.path.getsize(DB_FILE) > 0:
    df = pd.read_csv(DB_FILE)
else:
    # If file is empty or missing, create a temporary empty display
    df = pd.DataFrame(columns=["Category", "Amount", "Item"])

# Now the rest of your app won't crash!
st.title("🛡️ Financial Command Center")

if df.empty:
    st.info("Your vault is currently empty. Add your first expense in the 'Add Entry' tab!")
else:
    # Your metrics and charts code goes here...
    st.write("Data loaded successfully!")


st.markdown("---")
st.subheader("📥 Backup Your Data")

# Convert the current dataframe to a CSV string
csv_data = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Expenses as CSV",
    data=csv_data,
    file_name="my_vault_backup.csv",
    mime="text/csv",
)
