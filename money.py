import streamlit as st  # Importing the streamlit library for creating the app
import random  # Importing the random module for generating random numbers
import time  # Importing the time module for simulating a delay
import requests  # Importing requests module to make HTTP requests to an API

# Set the title of the Streamlit app
st.title("Money-Making-Machine")

# Function that simulates generating random money between 1 and 100
def money_machine():
    return random.randint(1,100)

# Subheader to give context for the "money generation" feature
st.subheader("Instant Cash Generator")

# Button that triggers the generation of random money when clicked
if st.button("Generate Money"):
    st.write("Counting Your Money....")  # Message to show that money is being counted
    time.sleep(2)  # Simulate a 2-second delay (like counting or processing)
    amount = money_machine()  # Call the money_machine function to get the random amount
    st.success(f"You Made ${amount}! ")  # Display the amount made as a success message

# Function that fetches side hustle ideas from an API
def fetch_side_hustle():
    try:
        # Making a GET request to the local API to fetch side hustle ideas
        response = requests.get("http://127.0.0.1:8000/side_hustle")
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            hustles  = response.json()  # Parse the JSON response to get the hustles
            return hustles["side_hustle"]  # Return the side hustle idea
        else:
            return("Freelancing")  # Return a default side hustle if API request fails
    except:
        # Return a fallback message if an exception occurs during the API request
        return("Something went Wrong!")

# Subheader to introduce the side hustle feature
st.subheader(" Side Hustle Ideas")

# Button that triggers the generation of side hustle ideas when clicked
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()  # Call the fetch_side_hustle function to get the idea
    st.success(idea)  # Display the fetched side hustle idea as a success message
