""" comment to code generation web app
"""
# notes on running:  https://docs.streamlit.io/knowledge-base/deploy/remote-start

import streamlit as st
from imagegenerator import generate_image

st.title("Image Generator")
st.write("Generated Image")

size = st.text_input("Size", "1024x1024")
text = st.text_area("Text", "generate buildful birdimage")

if st.button("Generate Image"):
    with st.spinner(text="In progress"):
        code = generate_image(text, size)
        st.image(code, width=400)
