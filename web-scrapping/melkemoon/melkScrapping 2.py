from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Initialize WebDriver with options
options = Options()
# Set User-Agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Load the DataFrame containing the links
df = pd.read_csv('D:/bachelor-final-project/data/data.csv')
df = df.dropna(subset=['related_link'])
urls = df['related_link'].unique()

results = []

for url in urls:
    try:
        # Load the URL in Selenium
        driver.get(url)
        time.sleep(3)  # Optional: Wait for page to load, adjust as necessary

        # Check for redirect by examining the final URL
        final_url = driver.current_url
        if final_url != url:
            print(f"Redirected from {url} to {final_url}")

        # Extract the data from the table
        cabinet_element = driver.find_elements(By.CSS_SELECTOR, 'tr:nth-child(6) td:nth-child(1)')
        cabinet = cabinet_element[0].text.strip() if cabinet_element else ''

        result = {
            'url': url,
            'cabinet': cabinet
        }
        results.append(result)

        # Append result to CSV immediately after adding to results
        results_df = pd.DataFrame([result])  # Convert single result to DataFrame
        results_df.to_csv('output.csv', mode='a', encoding='utf-8-sig', header=not pd.io.common.file_exists('output.csv'), index=False)

        time.sleep(3)

    except Exception as e:
        print(f"Error processing {url}: {e}")

# Close the WebDriver
driver.quit()

print("Scraping complete.")
