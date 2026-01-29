from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os
from openpyxl import Workbook

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

driver.get("https://www.amazon.in/")

# Search laptops
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("laptops")
search_box.send_keys(Keys.RETURN)

all_laptops = []

data_folder = ".venv/data"

if not os.path.exists(data_folder):
    os.makedirs(data_folder)


for page in range(1, 11):
    print(f"\nScraping Page {page}")

    # wait till products load
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "puis-card-container")))
    time.sleep(2)

    # Get full page HTML
    html = driver.page_source

    # Save HTML to file
    file_path = f"{data_folder}/page_{page}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Saved HTML for Page {page}")

    # Parse the saved file instead of live page
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    products = soup.find_all("div", class_="puis-card-container")


    for product in products:
        # Title
        title_tag = product.find("h2")
        title = title_tag.text.strip() if title_tag else "N/A"

        # Price
        price_tag = product.find("span", class_="a-price-whole")
        price = price_tag.text.strip() if price_tag else "N/A"

        # Link
        link_tag = product.find("a", href=True)
        link = "https://www.amazon.in" + link_tag["href"] if link_tag else "N/A"

        all_laptops.append({
            "Title": title,
            "Price": price,
            "Link": link
        })

    # Go to next page
    try:
        next_button = driver.find_element(By.XPATH, "//a[contains(@class,'s-pagination-next')]")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)
    except:
        print("No more pages.")
        break

driver.quit()

print(f"\nTotal laptops scraped: {len(all_laptops)}")

for laptop in all_laptops[:10]:
    print(laptop)


wb = Workbook()
ws = wb.active
ws.title = "Amazon Laptops"

ws.append(["Title", "Price", "Link"])

for laptop in all_laptops:
    ws.append([laptop["Title"], laptop["Price"], laptop["Link"]])

wb.save("amazon_laptops.xlsx")
print("Excel file created!")
