import streamlit as st
import pandas as pd
import os

st.title("📊 Excel Ledger System")

EXCEL_FILE = "spending_data.xlsx"

# 1. Load the Excel File
try:
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
    else:
        # Create a blank Excel file if it doesn't exist
        df = pd.DataFrame(columns=["Category", "Amount", "Item"])
        df.to_excel(EXCEL_FILE, index=False)
except Exception as e:
    st.error(f"Excel Error: {e}")
    df = pd.DataFrame(columns=["Category", "Amount", "Item"])

# 2. Display Metrics
if not df.empty:
    st.metric("Total Spent", f"${df['Amount'].sum():,.2f}")
    st.dataframe(df, use_container_width=True)

# 3. Add Entry Form
with st.form("excel_form"):
    cat = st.selectbox("Category", ["Food", "Tech", "Fun"])
    amt = st.number_input("Amount", min_value=0.0)
    note = st.text_input("Note")
    
    if st.form_submit_button("Save to Excel"):
        new_row = pd.DataFrame([[cat, amt, note]], columns=["Category", "Amount", "Item"])
        # Append and Save
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        st.success("Entry added to Excel file!")
        st.rerun()
