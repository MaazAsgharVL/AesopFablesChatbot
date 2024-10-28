# Import necessary libraries
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os
import time

# Define a class to handle document metadata and content
class Document:
    def __init__(self, content, metadata=None):
        self.page_content = content  # Store content of the document
        self.metadata = metadata if metadata is not None else {}  # Store metadata or an empty dictionary if none provided

# Function to read all text files from a directory and create Document objects
def read_text_files(directory):
    documents = []  # List to hold Document objects
    print(f"Looking for text files in {directory}")
    for root, dirs, files in os.walk(directory):  # Traverse directory
        for filename in files:  # Loop through all files found
            if filename.endswith('.txt'):  # Check for text files
                file_path = os.path.join(root, filename)  # Create full path to the file
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:  # Open file for reading
                        content = file.read()
                        if content.strip():  # Check if content is not just whitespace
                            stats = os.stat(file_path)  # Get file stats
                            metadata = {
                                'filename': filename,
                                'filesize': stats.st_size,
                                'last_modified': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime)),
                            }
                            documents.append(Document(content, metadata))  # Create Document and add to list
                            print(f"Read content from {filename} with metadata")
                        else:
                            print(f"File {filename} is empty.")  # Log empty file
                except IOError as e:
                    print(f"Could not read file {filename}: {str(e)}")  # Handle file read errors
    return documents  # Return list of Document objects

# Function to process documents, split content, and save into a vector database
def process_documents(directory):
    documents = read_text_files(directory)  # Read documents
    if not documents:
        print("No documents to process.")  # Check if no documents were read
        return
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500)  # Initialize the text splitter with a specific chunk size
    docs = text_splitter.split_documents(documents)  # Split documents into chunks
    print("Checking for existing vector database...")
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of the script
    db_path = os.path.join(current_dir, "..", "data", "vector_database")  # Define the path for the database

    print("Creating vector_database...")
    vectorstore = Chroma.from_documents(docs, embedding=OpenAIEmbeddings(), persist_directory=db_path)  # Create a vector database from documents
    print("Persist vector_database is created")  # Log the creation of the database