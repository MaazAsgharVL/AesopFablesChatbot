#!/bin/bash

# Define the container name
CONTAINER_NAME="aesopfablescontainer"

# Check if the container already exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    # Stop the existing container
    docker stop $CONTAINER_NAME
    # Remove the existing container
    docker rm $CONTAINER_NAME
    # echo "Removed existing container: $CONTAINER_NAME"
fi

# Run a new container
docker run -it --name $CONTAINER_NAME \
  -e OPENAI_API_KEY='YOUR_API_KEY' \
  -v $(pwd)/../aesopfables_bot_data/:/app/data/ \
  -v $(pwd)/../chat_bot-main/chat_history:/app/chat_history \
  -p 8501:8501 \
  -p 5000:5000 \
  aesopfables "$@"
