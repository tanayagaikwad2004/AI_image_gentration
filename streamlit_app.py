# streamlit_app.py
import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

st.title("Stable Diffusion — VS Code Demo")

prompt = st.text_input("Enter prompt", value="A colorful fantasy landscape")
steps = st.slider("Steps", 10, 50, 30)
if st.button("Generate"):
    with st.spinner("Generating..."):
        resp = requests.post("http://localhost:8000/generate", json={"prompt": prompt})
        data = resp.json()
        img = Image.open(BytesIO(base64.b64decode(data["image_base64"])))
        st.image(img, caption="Generated image", use_column_width=True)
