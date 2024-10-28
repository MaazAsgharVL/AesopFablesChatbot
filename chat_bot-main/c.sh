#!/bin/bash

# Container name
CONTAINER_NAME="aesopfablescontainer"

# Check if the container is running
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    # Execute the command inside the running container
    docker exec -it $CONTAINER_NAME /bin/bash -c "streamlit run /app/app.py"
else
    echo "Container $CONTAINER_NAME is not running."
fi
