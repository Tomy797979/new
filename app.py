import streamlit as st
import os
import subprocess

USERNAME = st.secrets["USERNAME"]
REPO = st.secrets["REPO"]
TOKEN = st.secrets["GITHUB_TOKEN"]
EMAIL = st.secrets["EMAIL"]

REPO_DIR = "repo"

st.title("GitHub Cloud Storage Upload")

# Clone repo nếu chưa tồn tại
if not os.path.exists(REPO_DIR):

    clone_url = f"https://{USERNAME}:{TOKEN}@github.com/{USERNAME}/{REPO}.git"

    subprocess.run(["git","clone",clone_url,REPO_DIR])

# chọn folder
folder = st.selectbox(
    "Select folder",
    ["audio","images","video","json"]
)

uploaded_files = st.file_uploader(
    "Upload files",
    accept_multiple_files=True
)

if uploaded_files:

    save_path = os.path.join(REPO_DIR,folder)

    os.makedirs(save_path,exist_ok=True)

    links = []

    for file in uploaded_files:

        file_path = os.path.join(save_path,file.name)

        with open(file_path,"wb") as f:
            f.write(file.getbuffer())

        cdn = f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO}/{folder}/{file.name}"

        links.append(cdn)

    subprocess.run(["git","config","--global","user.email",EMAIL])
    subprocess.run(["git","config","--global","user.name",USERNAME])

    os.chdir(REPO_DIR)

    subprocess.run(["git","add","."])
    subprocess.run(["git","commit","-m","upload assets"],check=False)
    subprocess.run(["git","push"])

    st.success("Upload completed")

    st.subheader("Direct CDN Links")

    for link in links:
        st.write(link)
