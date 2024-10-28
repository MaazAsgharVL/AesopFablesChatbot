#!/bin/bash

# entrypoint.sh
# Check the input parameter to decide which script to run
case "$1" in
    "rag")
        echo "Running rag.py:"
        python3 rag.py
        ;;
    "chatbot")
        echo "Running chatbot.py:"
        python3 app.py
        ;;  
    "api")
        echo "Running chatbot.py:"
        python3 chatbot_flask_api.py
        ;; 
    "initialize")
        echo "Running rag.py:"
        python3 rag.py
        echo "Running chatbot.py:"
        streamlit run  app.py
        ;;
    "bash")
        bash
        ;;    
    *)
        echo "No specific script requested, running rag.py by default:"
        python3 rag.py
        ;;
esac
