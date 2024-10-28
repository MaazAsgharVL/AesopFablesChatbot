
# Aesop Fables Chatbot

This project is a chatbot designed to interactively share and discuss Aesop's Fables. It uses the OpenAI API to generate responses and is containerized with Docker for streamlined setup and deployment.

## Prerequisites

- **Docker**: Make sure Docker is installed on your system. Refer to the [Docker installation guide](https://docs.docker.com/get-docker/) if needed.
- **OpenAI API Key**: Required to access OpenAI’s language models. 

## Getting Started

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the main project directory:
   ```bash
   cd AesopFablesChatbot/chat_bot-main
   ```

3. **Configure OpenAI API Key**:
   - Open the `r.sh` file.
   - On **line 17**, replace `'API_KEY'` with your actual OpenAI API key:
     ```bash
     -e OPENAI_API_KEY='your_openai_api_key'
     ```

## Project Setup

You'll need to use two terminals for the setup and operation of this chatbot.

### Terminal 1

1. Go to the project directory:
   ```bash
   cd AesopFablesChatbot/chat_bot-main
   ```

2. Set executable permissions and start the setup script:
   ```bash
   chmod +x b.sh
   ./b.sh
   ```

3. Set executable permissions for `r.sh` and start the services:
   ```bash
   chmod +x r.sh
   ./r.sh rag
   ./r.sh api
   ```

### Terminal 2

1. Go to the project directory:
   ```bash
   cd AesopFablesChatbot/chat_bot-main
   ```

2. Set executable permissions for `c.sh` and start it:
   ```bash
   chmod +x c.sh
   ./c.sh
   ```

## Running the Chatbot

After following the setup instructions, the chatbot should be up and running. Access the chatbot and interact with it as per the configured endpoints or user interface setup.

---
