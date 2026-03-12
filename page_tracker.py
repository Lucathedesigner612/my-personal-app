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
# --- TOP ROW: UPGRADED METRICS ---
total_spent = df['Amount'].sum()
# This finds the category with the highest total spend
if not df.empty:
    highest_cat = df.groupby("Category")["Amount"].sum().idxmax()
else:
    highest_cat = "N/A"

col1, col2, col3 = st.columns(3)

# Metric 1: Total Spending
# Example: If your budget is $500
budget = 500
difference = budget - total_spent

col1.metric(
    label="Remaining Budget", 
    value=f"${difference}", 
    delta=f"{difference} vs Goal",
    delta_color="normal" # "normal" makes positive green, "inverse" makes positive red
)

# Metric 2: The "Top Drain" (Where the money goes most)
col2.metric(label="🔍 Top Drain", value=highest_cat)

# Metric 3: Transaction Count
col3.metric(label="📝 Entries", value=len(df))
# Set a limit for 'Fun' spending
FUN_LIMIT = 200.0
fun_spent = df[df['Category'] == 'Fun']['Amount'].sum()

if fun_spent > FUN_LIMIT:
    st.error(f"🚨 Budget Alert: You've spent ${fun_spent} on Fun! Limit is ${FUN_LIMIT}.")
else:
    st.success(f"✅ Budget Check: You have ${FUN_LIMIT - fun_spent} left for Fun.")


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




