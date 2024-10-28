from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize the WebDriver (for Chrome in headless mode)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Create the folder 'aesopfables.com' if it doesn't exist
output_folder = '../data/scraper4'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Step 1: Open the main page
driver.get("https://www.aesopfables.com/")

# Function to create a text file and copy content
def scrape_fable(content_xpath, next_button_xpath, file_name_xpath):
    try:
        # Extract the fable title and content
        title = driver.find_element(By.XPATH, file_name_xpath).text
        driver.find_element(By.XPATH, file_name_xpath).click()
        time.sleep(2)
        content = driver.find_element(By.XPATH, content_xpath).text

        # Clean the title to create a valid file name
        file_name = title.replace(" ", "_").replace("/", "_") + ".txt"
        file_path = os.path.join(output_folder, file_name)

        # Save the fable in a text file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"{content}")
            print(f"Saved: {file_name}")

        # Click to go back to the main page
        driver.find_element(By.XPATH, next_button_xpath).click()
        time.sleep(2)

        return 1

    except Exception as e:
        return 0

# Loop to scrape multiple fables
def scrape_all_fables(start_link_row, start_file_row, max_link_row):
    link_row = start_link_row
    file_row = start_file_row
    while link_row <= max_link_row:
        driver.get("https://www.aesopfables.com/")
        time.sleep(5)
        # The XPath to the fable link (to click and navigate to fable page)
        fable_link_xpath = f"/html/body/ul/center/p[3]/table/tbody/tr[{link_row}]/td[1]/a"
        # Click the link to open the fable page
        driver.find_element(By.XPATH, fable_link_xpath).click()
        time.sleep(2)

        while True:
            file_name_xpath = f"/html/body/ul/center/p[3]/table/tbody/tr[{file_row}]/td[1]/a"
            # The XPath to the fable content
            fable_content_xpath = "/html/body/ul/center/table/tbody/tr/td/font/pre"
            # The XPath for the "Back" button
            next_button_xpath = "/html/body/ul/center/p[2]/a"

            if not scrape_fable(fable_content_xpath, next_button_xpath, file_name_xpath):
                print(f"Reached end of fables for link_row {link_row}")
                file_row = 2
                link_row += 1 
                break

            # Increment file row
            file_row += 1

# Start scraping with the logic provided
scrape_all_fables(2, 7, 5)  # link rows start at 2 and end at 5, file row starts at 7

# Close the browser
driver.quit()
