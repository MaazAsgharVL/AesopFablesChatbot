import streamlit as st
from utils.chat_history_manager import load_chat_history, save_chat_history
import requests

def run_UI(api_key):
    st.title("AESOP'S FABLES BOT")
    st.markdown(
            """
            <style>
            .user-msg {
                background-color: gray;
                padding: 10px;
                border-radius: 10px;
                text-align: right;
                width: fit-content;
                float: right;
                clear: both;
                margin: 5px 0;
            }
            .bot-msg {
                padding: 10px;
                border-radius: 10px;
                text-align: left;
                width: fit-content;
                float: left;
                clear: both;
                margin: 5px 0;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    
    # Load existing chat history if not already in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = load_chat_history(api_key)  # Load existing chat history

    # Display existing chat history
    for message in st.session_state.chat_history:
        # Display user message with a label
        st.markdown(
            f"<div class='user-msg'>{message['user']}</div>",
            unsafe_allow_html=True,
        )
        st.write("")  # Add an empty line for spacing

        # Display bot message with a label
        st.markdown(
            f"<div class='bot-msg'>{message['bot']}</div>",
            unsafe_allow_html=True,
        )
        st.write("") 

    query = st.chat_input("Enter your message here:")

    if query and api_key:
        # Send request to Flask backend with API key
        response = requests.post(
            "http://localhost:5000/chat",
            json={"query": query, "api_key": api_key}
        )

        if response.status_code == 200:
            # Get the bot's response from the JSON
            bot_response = response.json().get("response")
            st.session_state.chat_history.append({"user": query, "bot": bot_response})
            
            # Save updated chat history
            save_chat_history(api_key, st.session_state.chat_history)
            
            # Display the new messages in the same way as before
            st.markdown(
                f"<div class='user-msg'>{query}</div>",
                unsafe_allow_html=True,
            )
            st.write("")  # Add an empty line for spacing

            st.markdown(
                f"<div class='bot-msg'>{bot_response}</div>",
                unsafe_allow_html=True,
            )
            st.write("") 
             
        else:
            st.error("Failed to send message.")

def main():
    # Check if the API key is already stored in session state
    if 'api_key' not in st.session_state:
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        if api_key:
            st.session_state['api_key'] = api_key  # Store it in session state
            st.success("API Key stored in session!")
            
            # Load chat history immediately after entering the API key
            st.session_state.chat_history = load_chat_history(api_key)
    
    # Run the chatbot if the API key is available
    if 'api_key' in st.session_state and st.session_state['api_key']:
        run_UI(st.session_state['api_key'])  # Pass the api_key here
    else:
        st.info("Please enter your OpenAI API key to start the chatbot.")

if __name__ == "__main__":
    print("Chatbot is ready to go...")
    main()