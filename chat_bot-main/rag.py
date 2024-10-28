from services.scraper import process_urls_from_csv
from services.documet_to_db import process_documents
from services.pdf_to_text import process_pdf_files

def main():
    # Process documents that were saved from the web scraping
    print("\n\nProcessing documents from raw data...\n")
    process_documents('data/raw_data')

if __name__ == "__main__":
    main()
