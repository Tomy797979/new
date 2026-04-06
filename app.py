import streamlit as st
import base64
from github import Github

st.title("GitHub Cloud Storage")

USERNAME = st.secrets["USERNAME"]
REPO = st.secrets["REPO"]
TOKEN = st.secrets["GITHUB_TOKEN"]

g = Github(TOKEN)
repo = g.get_user(USERNAME).get_repo(REPO)

folder = st.selectbox(
    "Select folder",
    ["audio","images","video"]
)

uploaded_files = st.file_uploader(
    "Upload files",
    accept_multiple_files=True
)

if uploaded_files:

    links = []

    for file in uploaded_files:

        content = file.read()

        path = f"{folder}/{file.name}"

        try:
            repo.create_file(path,"upload",content)
        except:
            file_data = repo.get_contents(path)
            repo.update_file(path,"update",content,file_data.sha)

        cdn = f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO}/{folder}/{file.name}"

        links.append(cdn)

    st.success("Upload completed!")

    st.subheader("CDN Links")

    for link in links:
        st.code(link)
