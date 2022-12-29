""" comment to code generation web app

"""
# notes on running:  https://docs.streamlit.io/knowledge-base/deploy/remote-start

import streamlit as st
from commenttocodegeneration import generate_code

st.title("Code Generator from Comment")
st.write("Convert a comment into code in any language")

language = st.text_input("Language", "python")
text = st.text_area("Comment", "Calculate the mean distance between an array of points")

if st.button("Generate Code"):
    with st.spinner(text="In progress"):
        code = generate_code(text, language)
        st.code(code)
