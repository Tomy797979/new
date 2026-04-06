
import streamlit as st
import os
import subprocess

st.title("GitHub Cloud Storage Upload")

USERNAME = st.secrets.get("USERNAME", "YOUR_GITHUB_USERNAME")
REPO = st.secrets.get("REPO", "YOUR_REPO_NAME")
BRANCH = "main"

folders = ["audio","images","video","json"]
folder = st.selectbox("Select storage folder", folders)

uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)

if uploaded_files:
    if not os.path.exists(folder):
        os.makedirs(folder)

    links = []

    for file in uploaded_files:
        filepath = os.path.join(folder, file.name)

        with open(filepath, "wb") as f:
            f.write(file.getbuffer())

        cdn_link = f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO}/{folder}/{file.name}"
        links.append(cdn_link)

    try:
        subprocess.run(["git","add","."], check=True)
        subprocess.run(["git","commit","-m","upload assets"], check=True)
        subprocess.run(["git","push"], check=True)
        st.success("Upload completed and pushed to GitHub")
    except Exception as e:
        st.error("Git push failed. Make sure GitHub token is configured.")
        st.exception(e)

    st.subheader("Direct CDN Links")
    for l in links:
        st.write(l)
