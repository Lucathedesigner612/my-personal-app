import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("🛡️ Permanent Cloud Vault")

# 1. Establish Connection
conn = st.connection("gsheets", type=GSheetsConnection)

# 2. Read Data
df = conn.read()

st.subheader("Live Data from Google Sheets")
st.dataframe(df, use_container_width=True)

# 3. Add New Data Form
with st.form("add_form"):
    new_cat = st.selectbox("Category", ["Food", "Tech", "Bills"])
    new_amt = st.number_input("Amount", min_value=0.0)
    new_item = st.text_input("What was it?")
    
    if st.form_submit_button("Upload to Cloud"):
        # Create a new row
        new_row = {"Category": new_cat, "Amount": new_amt, "Item": new_item}
        
        # Add to existing data and update the sheet
        updated_df = df.append(new_row, ignore_index=True)
        conn.update(data=updated_df)
        
        st.success("Data written to Google Sheets! It's now permanent.")
        st.balloons()
