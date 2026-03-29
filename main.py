from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import pandas as pd

# Define browser and action setup
PATH = 'C:\Program Files (x86)\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# Define URL Target
linkedin_url = 'https://www.linkedin.com/jobs/search/?currentJobId=4250092828&keywords=data%20scientist&origin=JOB_COLLECTION_PAGE_SEARCH_BUTTON&refresh=true'

# Action Step
driver.maximize_window()
driver.get(linkedin_url)

# Determine how many jobs we want to scrape, and calculate how many time we need to scroll down
no_off_jobs = 100

# int(driver.find_element_by_css_selector("h1 > span"), get_attribute("innertText"))
n_scroll = int(no_off_jobs/25)+1
print(n_scroll)
i= 1
driver.execute_script("return document.body.scrollHeight") # scroll to top
while i <= n_scroll:
    driver.execute_script("return document.body.scrollHeight")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # Scroll to the bottom of page
    time.sleep(3)
    i = i + 1
    try :
        button = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/section[2]/button')
        time.sleep(2)
        button.click()
        time.sleep(1)
        print("load more click")
    except:
        driver.execute_script("return document.body.scrollHight")
        time.sleep(3)
print("Total Jobs : ")
jobs= driver.find_element(By.CLASS_NAME,"jobs_search_result").find_element(By.TAG_NAME,'11') # Return a list 
print(len(jobs))