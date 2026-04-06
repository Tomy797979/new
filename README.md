
# GitHub Cloud Storage Upload Tool (Streamlit)

Simple web tool to upload files to your GitHub repository and automatically generate CDN links.

## Features
- Upload multiple files
- Organize by folder (audio / images / video / json)
- Automatically pushes to GitHub
- Generates CDN links using jsDelivr

CDN format:
https://cdn.jsdelivr.net/gh/USERNAME/REPO/PATH

Example:
https://cdn.jsdelivr.net/gh/username/ai-assets-storage/audio/prayer.mp3

## Deploy on Streamlit Cloud

1. Upload these files to a GitHub repository.
2. Go to https://share.streamlit.io
3. Deploy the repo.
4. Set secrets:

USERNAME = your github username  
REPO = your repo name

Then upload files from the web UI.

## Folder structure

audio/  
images/  
video/  
json/

