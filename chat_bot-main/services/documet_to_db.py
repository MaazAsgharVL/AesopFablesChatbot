# Import necessary libraries
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os

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
                            # Create metadata with filename and other details
                            metadata = {'filename': filename}
                            # Create a Document object with the full content of the file
                            document = Document(content=content, metadata=metadata)
                            documents.append(document)  # Add to list of documents
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
                    
    return documents

# Function to convert documents into embeddings and save to vector database
def save_to_vector_database(documents):
    # Initialize embeddings and Chroma vector store
    embeddings = OpenAIEmbeddings()  # Using the default embeddings function without an explicit API key
    vectorstore = Chroma(persist_directory="data/vector_database", embedding_function=embeddings)

    # Process each document, add it to the vector store
    for document in documents:
        vectorstore.add_texts(texts=[document.page_content], metadatas=[document.metadata])
    
    # Save the vectorstore to disk (persist data)
    vectorstore.persist()
    print("Data saved to vector database.")

# Main function to execute the complete workflow
def main():
    raw_data_directory = 'data/raw_data'  # Path to the directory with raw text files

    # Step 1: Read text files and create documents
    documents = read_text_files(raw_data_directory)
    print(f"Total documents processed: {len(documents)}")

    # Step 2: Save documents to the vector database
    save_to_vector_database(documents)

if __name__ == "__main__":
    main()
