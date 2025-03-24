import streamlit as st
import random
import time 
import requests


st.title("Money-Making-Machine")

def money_machine():
    return random.randint(1,100)
st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting Your Money....")
    time.sleep(2)
    amount = money_machine()
    st.success(f"You Made ${amount}! ")

def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustle")
        if response.status_code == 200:
            hustles  = response.json()
            return hustles["side_hustle"]
        else:
            return("Freelancing")
    except:
            return("Something went Wrong!")
st.subheader(" Side Hustle Ideas")
if st.button("Generate Hustle"):
        idea = fetch_side_hustle()
        st.success(idea)
    
 
