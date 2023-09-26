from selenium import webdriver
from bs4 import BeautifulSoup as bs

urls = ["https://www.indeed.com/jobs?q=python&l=OR"]

driver = webdriver.Chrome()

def scrape_url(url):
    """
    Scrape a given URL for job postings
    """

    try:
        driver.get(url)
        response = driver.page_source
    except:
        driver.quit()

    soup = bs(response, 'html.parser')
    job_results = soup.find_all('div', class_ = "cardOutline")
    
    print(job_results[0].find('h2'))
    
    
    # soup = bs(response, 'html.parser')
    # print(soup.main.text)

for url in urls:
    scrape_url(url)