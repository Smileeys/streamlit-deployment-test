import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Deployment Test App", page_icon="🚀", layout="wide")

st.title("🚀 Streamlit Deployment Test")
st.write("If you can see this page, your Streamlit deployment is working correctly.")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! 👋")

number = st.slider("Select a number", 1, 100, 50)
st.write(f"You selected: **{number}**")

df = pd.DataFrame({
    "Value": np.random.randint(1, 100, 20)
})

st.subheader("📊 Sample Data")
st.dataframe(df)

st.subheader("📈 Line Chart")
st.line_chart(df)

if st.button("Generate New Data"):
    st.rerun()

st.info("✅ Deployment test successful.")
