from services.documet_to_db import process_documents

def main():
    # Process documents that were saved from the web scraping
    print("\n\nProcessing documents from raw data...\n")
    process_documents('data/raw_data')

if __name__ == "__main__":
    main()
