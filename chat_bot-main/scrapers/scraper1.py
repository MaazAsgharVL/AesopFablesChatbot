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
folder_path = "../data/scraper1"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Function to scrape a single page and save text
def scrape_and_save():
    try:
        # Extract title from the <h1> tag
        title_element = driver.find_element(By.TAG_NAME, "h1")
        title_text = title_element.text
        
        # Stop if the title is "The End"
        if title_text.strip() == "The End":
            print("Reached 'The End'. Stopping...")
            return False
        
        # Create a text file in the 'txt_files' folder with the title as the name
        file_name = f"{title_text}.txt"
        file_name = file_name.replace(" ", "_").replace("/", "_")  # Sanitize file name
        file_path = os.path.join(folder_path, file_name)  # Create the full path inside the txt_files folder
        with open(file_path, "w", encoding="utf-8") as file:
            # Extract page text
            page_text = driver.find_element(By.ID, "page").text
            file.write(page_text)
            print(f"Saved content to {file_path}")

        # Click the next button
        next_button = driver.find_element(By.ID, "nextButtonFooter")
        next_button.click()
        time.sleep(2)  # Wait for the next page to load
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Open the website
driver.get("https://read.gov/aesop/002.html")

# Loop through pages until "The End" is found
while scrape_and_save():
    pass

# Close the browser
driver.quit()
