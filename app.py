import os
import streamlit as st
import google.generativeai as gpt
from functions import*
#from dotenv import load_dotenv

# Load environment variables
#load_dotenv()
API_KEY = st.secrets["general"]["api_key"]

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":robot_face:",  # Favicon emoji
    layout="wide",  # Page layout option
)

#API_KEY = os.getenv("API_KEY")

# Set up Google Gemini-Pro AI model
#gpt.configure(api_key="AIzaSyD2FgcE0rqCciGRzQngqQrwhxuZKgMj-Zg")
gpt.configure(api_key=API_KEY)

model = gpt.GenerativeModel('gemini-pro')

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("🤖 Chat with Ritik chat bot")

# Display the chat history
for msg in st.session_state.chat_session.history:
    with st.chat_message(map_role(msg["role"])):
        st.markdown(msg["content"])

# Input field for user's message
user_input = st.chat_input("Ask Gemini-Pro...")
if user_input:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_input)

    # Send user's message to Gemini and get the response
    gemini_response = fetch_gemini_response(user_input)

    # Display Gemini's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response)

    # Add user and assistant messages to the chat history
    st.session_state.chat_session.history.append({"role": "user", "content": user_input})
    st.session_state.chat_session.history.append({"role": "model", "content": gemini_response})