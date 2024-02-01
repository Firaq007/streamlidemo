import streamlit as st
import os

# Title of the app
st.title("Medicine Remainder")

# Directory containing videos
video_dir = "videos"
medicine_files = os.listdir(video_dir)

# Dropdown to select a video
selected_video = st.selectbox("medicine name", medicine_files)

# Display the selected video
video_path = os.path.join(video_dir, selected_video)
st.video(video_path)
