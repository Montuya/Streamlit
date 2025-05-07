# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:29:14 2025
@author: Administrator
"""

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="centered")

st.title("🌤️ Weather Dashboard")
st.markdown("Get **hourly weather forecasts** and visualize conditions for supported cities using charts.")

# City selector
city_coords = {
    "Manila": (14.5995, 120.9842),
    "Tokyo": (35.6895, 139.6917),
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Paris": (48.8566, 2.3522)
}

city = st.selectbox("🌍 Select a City:", list(city_coords.keys()))
lat, lon = city_coords[city]

# Open-Meteo API URL
api_url = (
    f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
    "&hourly=temperature_2m,precipitation,weathercode,windspeed_10m,relativehumidity_2m"
    "&daily=temperature_2m_max,temperature_2m_min"
    "&timezone=auto"
)

# Fetch weather data
try:
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()
    data = response.json()
    hourly_df = pd.DataFrame(data['hourly'])
    hourly_df['time'] = pd.to_datetime(hourly_df['time'])

    st.success(f"✅ Forecast data for **{city}** loaded successfully.")

    # Raw data viewer
    with st.expander("🧾 Show Raw Forecast Data (Hourly)"):
        st.dataframe(hourly_df.head(24), use_container_width=True)

    # Chart 1: Temperature Line Chart
    st.subheader("📈 Temperature Over Time")
    st.line_chart(hourly_df.set_index('time')['temperature_2m'].head(24), use_container_width=True)

    # Chart 2: Precipitation Bar Chart
    st.subheader("🌧️ Precipitation Levels")
    st.bar_chart(hourly_df.set_index('time')['precipitation'].head(24), use_container_width=True)

    # Chart 3: Wind Speed Area Chart
    st.subheader("💨 Wind Speed Trends")
    st.area_chart(hourly_df.set_index('time')['windspeed_10m'].head(24), use_container_width=True)

    # Chart 4: Humidity Histogram with KDE
    st.subheader("💧 Humidity Distribution")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.set(style="whitegrid")
    sns.histplot(hourly_df['relativehumidity_2m'].head(24), bins=10, kde=True, ax=ax1, color="skyblue")
    ax1.set_xlabel("Relative Humidity (%)")
    ax1.set_title("Humidity Distribution (Next 24 Hours)")
    st.pyplot(fig1)

    # Chart 5: Weather Code Pie Chart
    st.subheader("☁️ Weather Code Frequency")
    weather_counts = hourly_df['weathercode'].head(24).value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    st.pyplot(fig2)

    # Table: Full Forecast
    st.subheader("📋 Forecast Table (Next 24 Hours)")
    st.dataframe(hourly_df.head(24), use_container_width=True)

except requests.exceptions.RequestException as e:
    st.error(f"🚨 Error fetching weather data: {e}")
except Exception as e:
    st.error(f"⚠️ Unexpected error: {e}")
    