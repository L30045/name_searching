from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os
import config
import time
import random



#%% class definition
class AutoSearch:
    def __init__(self):
        service = Service(config.webdriver_path)
        self.driver = webdriver.Chrome(service=service)
        # set wait time
        self.wait = WebDriverWait(self.driver, 10)
        # Set random delay between 1-3 seconds to mimic human behavior
        self.random_click = lambda: time.sleep(random.uniform(config.min_click_delay, config.max_click_delay))

    def login(self,username,password):
        self.driver.get(config.target_url)
        # click sign in button
        self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/a[2]')))
        self.random_click()
        self.driver.find_element(By.XPATH, '/html/body/nav/div/a[2]').click()
        
        # input username and password
        self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys(password)
        self.random_click()
        login_button = self.driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[4]/button')
        login_button.click()

    def search_people(self, name):
        # click search icon
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="global-nav-search"]/div/button/span/svg')))
        search_box = self.driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/button/span/svg')
        self.random_click()
        search_box.click()
        # input name
        search_input = self.driver.find_element(By.ID,'global-nav-typeahead')
        search_input.send_keys(name)
        self.random_click()
        search_input.send_keys(Keys.ENTER)
        # apply people filter
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[2]/button')))
        people_filter = self.driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[2]/button')
        self.random_click()
        people_filter.click()
        # get all search results
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'search-results-container')))
        search_results = self.driver.find_elements(By.CLASS_NAME, 'search-results-container')
        # Extract information from each result
        results = []
        for result in search_results[:config.max_search_results]:
            try:
                name = result.find_element(By.CLASS_NAME, 'entity-result__title-text').text
                title = result.find_element(By.CLASS_NAME, 'entity-result__primary-subtitle').text
                location = result.find_element(By.CLASS_NAME, 'entity-result__secondary-subtitle').text
                results.append({
                    'name': name,
                    'title': title, 
                    'location': location
                })
            except:
                continue
                
        return results






    
