import streamlit as st
import pandas as pd

st.title("🛡️ Financial Command Center")

# Load data
df = pd.read_csv("spending_data.csv")

# --- TOP ROW: KPI METRICS ---
total_spent = df['Amount'].sum()
highest_cat = df.groupby("Category")["Amount"].sum().idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("Total Outflow", f"${total_spent:,.2f}", delta="-2% vs Last Week")
col2.metric("Top Category", highest_cat)
col3.metric("Entries", len(df))

st.markdown("---")

# --- MIDDLE ROW: TABS FOR VIEWS ---
tab1, tab2, tab3 = st.tabs(["📈 Visuals", "🗒️ Raw Data", "➕ Add Entry"])

with tab1:
    st.subheader("Spending Trends")
    # Use an area chart for a more modern look
    chart_data = df.groupby("Category")["Amount"].sum()
    st.area_chart(chart_data)

with tab2:
    st.dataframe(df, use_container_width=True)

with tab3:
    # Move the input form here so it doesn't clutter the sidebar
    with st.form("entry_form"):
        item = st.text_input("Transaction Name")
        amt = st.number_input("Amount", min_value=0.0)
        cat = st.selectbox("Type", ["Food", "Tech", "Bills", "Fun"])
        submitted = st.form_submit_button("Log Transaction")
        if submitted:
            # Add saving logic here
            st.success("Log Updated!")
