import streamlit as st

st.title("🚀 2026 Vision Board")
st.write("What are we saving for? Define your goals and visualize the future.")

# Create two columns: One for the goal, one for the image
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Current Focus")
    goal_name = st.text_input("Project Name", value="New Gaming Setup")
    target_price = st.number_input("Target Amount ($)", value=1500)
    
    # Let's use a slider to show progress manually for now
    current_saved = st.slider("How much have you saved?", 0, target_price, 450)
    
    # Logic to calculate percentage
    progress = current_saved / target_price
    st.progress(progress)
    st.write(f"**{progress:.0%}** of the way there!")

with col2:
    st.subheader("The Inspiration")
    # You can put a URL to any image here!
    st.image("https://images.unsplash.com/photo-1593305841991-05c297ba4575?auto=format&fit=crop&q=80&w=1000", 
             caption="Visualizing the win.")

st.markdown("---")
st.chat_input("Write a note to your future self...")

st.subheader("🔮 Goal Forecast")
avg_savings = st.number_input("Average monthly savings ($)", value=100)

if avg_savings > 0:
    months_left = (target_price - current_saved) / avg_savings
    st.info(f"At this rate, you will reach your goal in **{months_left:.1f} months**!")
