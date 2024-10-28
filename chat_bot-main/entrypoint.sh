#!/bin/bash

# entrypoint.sh
# Check the input parameter to decide which script to run
case "$1" in
    "rag")
        echo "Running rag.py:"
        python3 rag.py
        ;;
    "chat")
        echo "Running app.py:"
        python3 app.py
        ;;  
    "api")
        echo "Running chatbot_flask_api.py:"
        python3 chatbot_flask_api.py
        ;; 
    "init")
        echo "Running rag.py:"
        python3 rag.py
        echo "Running chatbot_flask_api.py:"
        streamlit run  chatbot_flask_api.py
        ;;
    "scrape")
        echo "Running Scraper 1:"
        python3 scrapers/scraper1.py
        echo "Running Scraper 2:"
        python3 scrapers/scraper2.py
        echo "Running Scraper 3:"
        python3 scrapers/scraper3.py
        echo "Running Scraper 4:"
        python3 scrapers/scraper4.py
        echo "Cleaning text files:"
        python3 utils/clean_names.py
        echo "Removing duplicate files:"
        python3 utils/move_files.py
        ;;
    "bash")
        bash
        ;;    
    *)
        echo "No specific script requested, running rag.py by default:"
        python3 rag.py
        ;;
esac
