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





    
