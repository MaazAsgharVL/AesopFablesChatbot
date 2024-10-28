from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options  # Import Options
import os
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize the WebDriver (for Chrome in headless mode)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Create the folder if it doesn't exist
folder_path = "../data/scraper2"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Function to clean the title and remove any "Illustrated by" or similar text
def clean_title(title):
    # Split the title by "Illustrated by" or other phrases and take the first part
    if "Illustrated by" in title:
        title = title.split("Illustrated by")[0].strip()
    elif "Written by" in title:
        title = title.split("Written by")[0].strip()
    return title

# Function to scrape a single page and save text
def scrape_and_save(n):
    try:
        # Construct the URL with the current 'n' value
        url = f"https://www.umass.edu/aesop/content.php?n={n}&i=1"
        driver.get(url)
        
        # Extract title from the <h1> tag
        title_element = driver.find_element(By.TAG_NAME, "h1")
        title_text = clean_title(title_element.text)
        
        # Stop if the title is empty (before "Illustrated by")
        if not title_text:
            print(f"No valid title found. Stopping at n={n}")
            return False

        # Check if a file with the same title already exists
        file_name = f"{title_text}.txt"
        file_name = file_name.replace(" ", "_").replace("/", "_")  # Sanitize file name
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.exists(file_path):
            print(f"File {file_name} already exists. Skipping to next page.")
            return True  # Skip to the next page

        # Extract text from the <td> tag with class 'content'
        content_element = driver.find_element(By.CLASS_NAME, "content")
        page_text = content_element.text
        
        # Check if the text has fewer than 15 words and skip if so
        if len(page_text.split()) < 15:
            print(f"Text on page n={n} has fewer than 15 words. Skipping.")
            return True

        # Create the file and save the content
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(page_text)
            print(f"Saved content to {file_name}")

        return True  # Move to the next page

    except Exception as e:
        print(f"An error occurred at n={n}: {e}")
        return False

# Start from 'n=0' and keep increasing until no valid title is found
n = 0
while scrape_and_save(n):
    n += 1
    time.sleep(2)  # Wait for the next page to load

# Close the browser
driver.quit()
