FROM python:3.10 AS allergy_bot_2.0

WORKDIR /app

# Copy the entrypoint script first and set the permissions
COPY entrypoint.sh /app/entrypoint.sh
RUN mkdir -p /app/data/
RUN chmod +x /app/entrypoint.sh


# Install Python packages
RUN pip3 install --upgrade pip
# Install Python packages directly in the Dockerfile
RUN pip3 install beautifulsoup4 
RUN pip3 install requests
RUN pip3 install langchain
RUN pip3 install langchain_community
RUN pip3 install langchain_openai
RUN pip3 install python-dotenv
RUN pip3 install streamlit
RUN pip3 install langchain_experimental
RUN pip3 install langchain_chroma
RUN pip3 install pdfminer.six
RUN pip3 install Flask


# Now copy the rest of the application code
ADD . /app

EXPOSE 5000 8501

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Default command (can be overridden by passing a parameter)
CMD [""]
