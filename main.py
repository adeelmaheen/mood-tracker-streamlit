import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# Initialize session state for storing moods
if 'mood_data' not in st.session_state:
    st.session_state.mood_data = pd.DataFrame(columns=['Date', 'Mood', 'Notes'])

st.title("🌿 Mood Tracker App")

# Input for mood tracking
today = datetime.date.today()
st.subheader(f"Log your mood for {today}")
mood = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Neutral", "Excited", "Angry", "Stressed", "Relaxed"])  
notes = st.text_area("Any additional notes?")
if st.button("Save Mood"):
    new_entry = pd.DataFrame({"Date": [today], "Mood": [mood], "Notes": [notes]})
    st.session_state.mood_data = pd.concat([st.session_state.mood_data, new_entry], ignore_index=True)
    st.success("Mood logged successfully!")

# Display past moods
st.subheader("📅 Mood History")
st.dataframe(st.session_state.mood_data)

# Mood visualization
if not st.session_state.mood_data.empty:
    st.subheader("📊 Mood Trend")
    mood_counts = st.session_state.mood_data['Mood'].value_counts()
    fig, ax = plt.subplots()
    mood_counts.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_ylabel("Count")
    ax.set_xlabel("Mood")
    ax.set_title("Mood Distribution")
    st.pyplot(fig)

st.sidebar.header("Navigation")
st.sidebar.write("Use this app to track and analyze your mood patterns over time.")
