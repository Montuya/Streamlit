import streamlit as st

# Set page configuration
st.set_page_config(page_title="My First Streamlit App", page_icon="🌟", layout="centered")

# App title and subtitle
st.title("🌟 Welcome to Your First Streamlit App!")
st.subheader("🚀 Interactive Demo with Live Feedback")

# App description
st.markdown(
    """
    This mini-app demonstrates how **Streamlit** provides real-time interaction with just a few lines of Python.  
    Fill in the inputs below and watch your app respond instantly! 🎯
    """
)

# Input section
st.divider()
st.header("🧾 User Details")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Enter your name:")
with col2:
    age = st.number_input("Enter your age:", min_value=0, step=1)

# Output section
st.divider()
st.header("📣 Response")

if name.strip():
    st.success(f"👋 Hello, **{name}**!")
    st.info(f"🎂 You are **{age}** years old.")
else:
    st.warning("⚠️ Please enter your name to see a personalized message.")

# Footer
st.divider()
st.caption("🔧 Built with Streamlit | ✨ Customize me further!")
