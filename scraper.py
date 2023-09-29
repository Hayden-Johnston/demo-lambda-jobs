from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

urls = ["https://www.indeed.com/jobs?q=python&l=OR&sc=0kf%3Aexplvl%28ENTRY_LEVEL%29%3B&vjk=d9e3f761d0e2ce81",
        "https://www.indeed.com/jobs?q=python&l=remote&sc=0kf%3Aexplvl%28ENTRY_LEVEL%29%3B&vjk=d9e3f761d0e2ce81"]

driver = webdriver.Chrome()

"""
Parse functions must perform these operations for each page of listings:
- get all html on page
- parse for title
- parse for link
- click button to next page
- WAIT a few seconds
- repeat until next button does not exist
"""

def get_page(url):
    """
    Get page with Selenium web driver
    """
    try:
        driver.get(url)
        response = driver.page_source
        return response
    except:
        print("Error loading page")
        driver.quit()

def parse_indeed(soup):
    """
    Parse Indeed.com html for job postings
    """

    #initialize job_results and all_jobs
    job_results = soup.find_all('div', class_ = "cardOutline")
    all_jobs = []

    def parse(results):
        """
        Helper function to parse job postings
        """
        for job in results:
            job_data = job.find('h2')
            job_title = job_data.find('span')
            job_link = job_data.find('a')
            title = job_title.get('title')
            link = job_link.get('href')
            all_jobs.append((title, "https://www.indeed.com" + link))
        return all_jobs
        
    # find next page button
    nav = soup.find('nav')
    button = nav.find_all('a')
    print(button)
    for i in button:
        print(i)
    while button is not None:
        # while button exists, parse the page and click the button
        parse(job_results)
        #button.click()
        time.sleep(5)
        button = soup.find('a', class_='css-akk0a e8ju0x50')
        response = driver.page_source
        soup = bs(response, 'html.parser')
        job_results = soup.find_all('div', class_ = "cardOutline")
    print(parse(job_results))

def scrape_url(url):
    """
    Scrape a given URL for job postings
    """
    soup = bs(get_page(url), 'html.parser')
    if "indeed" in url:
        parse_indeed(soup)
    if "glassdoor" in url:
        pass
    if "monster" in url:
        pass

for url in urls:
    scrape_url(url)



