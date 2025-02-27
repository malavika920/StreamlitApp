import pandas as pd
import streamlit as st
import time

# App Title
st.title("🎵 What Songs Were Popular When I Was in High School?")

st.markdown("""
Maybe you want to rediscover the top songs from your high school days. Or maybe you just don't want to mess with making your own playlist.  

Use this tool to find a pre-generated playlist of every song that made the Top 10 in the US for the years you select.  

Originally appeared on [Datafantic.com](https://www.datafantic.com/what-songs-were-popular-when-i-was-in-high-school).
""")

# Load dataset
df = pd.read_csv("playlists.csv")

# Year selection
years = list(range(1958, 2023))

# Stylish columns for year selection
col1, col2 = st.columns(2)

with col1:
    start_year = st.selectbox("Start Year", years, index=years.index(1995))

with col2:
    end_year = st.selectbox("End Year", years, index=years.index(2010))

# Form for better UI
with st.form("playlist_form"):
    st.write("Click the button below to generate your playlist!")
    submit_button = st.form_submit_button("Get My Playlist 🎶")

# Processing Logic
if submit_button:
    with st.spinner("Fetching your playlist... ⏳"):
        time.sleep(2)  # Simulate a delay for loading
        
        if start_year > end_year:
            st.warning("⚠ Start year cannot be greater than end year. Please adjust your selection.")
        else:
            playlist_name = f"Top US Singles: {start_year}" if start_year == end_year else f"Top US Singles: {start_year}-{end_year}"

            playlist_data = df[df['name'] == playlist_name]

            if not playlist_data.empty:
                playlist = playlist_data.iloc[0].to_dict()
                st.success(f"### Your Spotify Playlist: [{playlist['name']}]({playlist['link']})")
                st.balloons()  # Celebrate success with balloons 🎉
            else:
                st.error("Oops! It looks like we didn't create that playlist yet. Try selecting a range of 1-20 years.")