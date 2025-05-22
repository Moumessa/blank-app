import streamlit as st
import pandas as pd

st.title("🎈 My new Test app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


"""
# My first app
Here's our first attempt at using data to create a table:
"""


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
