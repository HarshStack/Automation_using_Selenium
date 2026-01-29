🛒 Amazon Laptop Scraper using Selenium & BeautifulSoup
This project is an automation-based web scraping pipeline that collects laptop listings from Amazon search results.
It combines browser automation and HTML parsing to extract structured product data and store it in Excel format.


Features:-
Opens Amazon automatically using Selenium
Searches for "Laptops"
Navigates through 20 search result pages
Saves raw HTML pages for each page
Parses product details from saved HTML

Extracts:
Product Title
Price
Product Link
Exports all results into an Excel file

Tech Stack:-
Tool	Purpose
Python	Core programming
Selenium	Browser automation
BeautifulSoup	HTML parsing
OpenPyXL	Excel file creation

📂 Project Structure
amazon-selenium-scraper/

│
├── main.py           
├── README.md         
├── requirements.txt   
├── .gitignore         
└── data/              

⚙️ How It Works
Selenium opens Amazon and performs a laptop search
Each results page HTML is saved locally
BeautifulSoup parses the saved HTML files
Laptop data is extracted
Data is exported to amazon_laptops.xlsx

How to Run:-
pip install -r requirements.txt
python main.py

Output:-
The script generates:
amazon_laptops.xlsx

Containing:
Title	Price	Link

⚠️ Note
This project is built for educational purposes to demonstrate automation and data extraction techniques.
Website structures may change, and scraping may be restricted by site policies.

Skills Demonstrated:-
Web Automation
Data Extraction
HTML Parsing
File Handling
Data Pipeline Workflow
