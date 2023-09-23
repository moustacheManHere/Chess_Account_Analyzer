import streamlit as st
import requests
import json
from datetime import datetime

API_KEY = st.secrets["API_KEY"]

st.write(""" # Chess Account Analyzer
         Please enter your Lichess Username to continue.
         """)
username = st.text_input("username","Contingency_Law")

response = requests.get(f"https://lichess.org/api/user/{username}",headers={"Authorization":f"Bearer {API_KEY}"})

if response.status_code == 200:
    data = response.json()
    if "error" in data:
        st.write("Sorry, Account not found!")
    else:
        joinDate = datetime.utcfromtimestamp(round(data["createdAt"]/1000)).strftime("%Y-%m-%d")
        lastDate = datetime.utcfromtimestamp(round(data["seenAt"]/1000)).strftime("%Y-%m-%d")
        st.write(f""" 
            Account created on: {joinDate}

            Last seen on: {lastDate}
        """)
        st.json(data)
else:
    st.write("Error fetching data. Please check your username and API key.")