import streamlit as st
import os
import subprocess

USERNAME = st.secrets["USERNAME"]
REPO = st.secrets["REPO"]
TOKEN = st.secrets["GITHUB_TOKEN"]
EMAIL = st.secrets["EMAIL"]

st.title("GitHub Cloud Storage Upload")

folder = st.selectbox(
    "Select folder",
    ["audio","images","video","json"]
)

uploaded_files = st.file_uploader(
    "Upload files",
    accept_multiple_files=True
)

if uploaded_files:

    if not os.path.exists(folder):
        os.makedirs(folder)

    links = []

    for file in uploaded_files:

        path = os.path.join(folder,file.name)

        with open(path,"wb") as f:
            f.write(file.getbuffer())

        cdn = f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO}/{folder}/{file.name}"
        links.append(cdn)

    subprocess.run(["git","config","--global","user.email",EMAIL])
    subprocess.run(["git","config","--global","user.name",USERNAME])

    subprocess.run(["git","add","."])

    subprocess.run(["git","commit","-m","upload assets"],check=False)

    remote = f"https://{USERNAME}:{TOKEN}@github.com/{USERNAME}/{REPO}.git"

    subprocess.run(["git","push",remote,"HEAD:main"])

    st.success("Upload completed")

    st.subheader("Direct Links")

    for link in links:
        st.write(link)
