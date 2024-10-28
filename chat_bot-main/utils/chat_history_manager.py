import json
import os
import hashlib
from datetime import datetime

# Define the directory for chat history
CHAT_HISTORY_DIR = "chat_history"

# Create the directory if it does not exist
os.makedirs(CHAT_HISTORY_DIR, exist_ok=True)

def generate_filename(api_key):
    """Generate a unique filename based on the hash of the API key and a timestamp."""
    api_key_hash = hashlib.sha256(api_key.encode()).hexdigest()  # Create a SHA-256 hash of the API key
    return os.path.join(CHAT_HISTORY_DIR, f"session_{datetime.now().strftime('%Y:%m:%d::%H:%M:%S')}_{api_key_hash}.json")

def load_chat_history(api_key):
    """Load chat history from a JSON file for a specific API key."""
    api_key_hash = hashlib.sha256(api_key.encode()).hexdigest()  # Hash the API key to find existing files
    
    # Check if any file exists that matches the pattern for this API key
    for file in os.listdir(CHAT_HISTORY_DIR):
        if file.startswith("session_") and api_key_hash in file:
            with open(os.path.join(CHAT_HISTORY_DIR, file), 'r') as f:
                return json.load(f)
    
    return []  # Return an empty list if no matching file is found

def save_chat_history(api_key, chat_history):
    """Save chat history to a JSON file for a specific API key."""
    api_key_hash = hashlib.sha256(api_key.encode()).hexdigest()  # Hash the API key to find existing files
    
    # Check if a file already exists for this API key
    existing_file = None
    for file in os.listdir(CHAT_HISTORY_DIR):
        if file.startswith("session_") and api_key_hash in file:
            existing_file = file  # Store the name of the existing file
            break  # Exit loop once found

    if existing_file:
        print(f"Chat history file already exists for API key: {api_key}. Appending new messages.")
        
        # Save the updated chat history back to the same file
        with open(os.path.join(CHAT_HISTORY_DIR, existing_file), 'w') as f:
            json.dump(chat_history, f)
        
        print(f"Chat history updated in {existing_file}")
    else:
        # Generate filename with timestamp and hash since no existing file was found
        chat_history_file = generate_filename(api_key)

        # Save the chat history to the corresponding new file
        with open(chat_history_file, 'w') as f:
            json.dump(chat_history, f)
        
        print(f"Chat history saved to {chat_history_file}")

