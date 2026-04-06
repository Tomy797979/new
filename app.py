import streamlit as st
from github import Github

st.title("GitHub Cloud Storage Upload")

USERNAME = st.secrets["USERNAME"]
REPO_NAME = st.secrets["REPO"]
TOKEN = st.secrets["GITHUB_TOKEN"]

g = Github(TOKEN)
repo = g.get_user(USERNAME).get_repo(REPO_NAME)

folder = st.selectbox(
    "Select folder",
    ["audio","video","images"]
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
            repo.create_file(
                path,
                "upload file",
                content
            )

        except Exception as e:

            st.error(f"File already exists: {file.name}")
            continue

        cdn = f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO_NAME}/{folder}/{file.name}"

        links.append(cdn)

    if links:

        st.success("Upload completed")

        st.subheader("Direct CDN Links")

        for link in links:
            st.code(link)
