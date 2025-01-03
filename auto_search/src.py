from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os
import auto_search.config as config
import time
import random



#%% class definition
class AutoSearch:
    def __init__(self):
        chrome_options = Options()
        # full screen
        chrome_options.add_argument("--start-maximized")
        # Disable GPU
        chrome_options.add_argument("--disable-gpu")
        # Disable proxy
        chrome_options.add_argument("--no-proxy-server")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        # (Optional) Run in headless mode
        # chrome_options.add_argument("--headless")  # Remove this line if you want to see the browser
        # (Optional) Other useful arguments
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        service = Service(config.webdriver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
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
        # disable remember me
        remember_me = self.driver.find_element(By.ID, 'rememberMeOptIn-checkbox')
        if remember_me.is_selected():
            self.random_click()
            remember_me.send_keys(Keys.SPACE)

        self.random_click()
        login_button = self.driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[4]/button')
        login_button.click()

    def search_people(self, name_list, area=None, company=None):
        output = pd.DataFrame(columns=['name', 'title', 'company', 'area'])
        for n_i in range(len(name_list)):
            name = name_list['name'][n_i]
            area = name_list['area'][n_i]
            company = name_list['company'][n_i]
            # input name
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'search-global-typeahead__input')))
            search_box = self.driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
            search_box.send_keys(name)
            self.random_click()
            search_box.send_keys(Keys.ENTER)
            # apply people filter
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'search-navigation-panel__button')))
            people_filter = self.driver.find_element(By.XPATH, '//*[text()="See all people results"]')
            self.random_click()
            people_filter.click()
            # get all search results
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'search-results-container')))
            search_results_container = self.driver.find_elements(By.CLASS_NAME, 'search-results-container')[0]
            search_results = search_results_container.find_elements(By.CLASS_NAME, 'linked-area.flex-1.cursor-pointer')
            # for each search result, check if the person is the one we are looking for
            for result in search_results[:min(config.max_search_results, len(search_results))]:
                # extract information
                all_info = [x.lower() for x in result.text.split('\n')]
                # check if the person is the one we are looking for
                # check if name is correct
                if name.lower() not in all_info:
                    continue
                # # check if area is correct
                # if area is not None and area.lower() not in all_info:
                #     continue
                # # check if company is correct
                # if company is not None and company.lower() not in all_info:
                #     continue
                # if we find the person, click in and extract information
                self.random_click()
                result.click()
                self.wait.until(EC.presence_of_element_located((By.ID, 'experience')))
                experience = self.driver.find_element(By.XPATH, '//*[@id="profile-content"]/div/div[2]/div/div/main/section[7]')
                # experience = self.driver.find_element(By.XPATH, '//*[text()="Experience"]')
                # get latest experience
                latest_experience = experience.find_element(By.CLASS_NAME,'display-flex.flex-column.full-width').text.split('\n')
                # get latest experience title
                latest_experience_title = latest_experience[0]
                # get latest experience company
                latest_experience_company = latest_experience[2].split('·')[0]
                # get latest experience location
                latest_experience_location = latest_experience[-1].split('·')[0]
                # return the information
                print('Found person')
                latest_info = [name, latest_experience_title, latest_experience_company, latest_experience_location]
                break

            # if no person found, clear search box and add 'not found' to output
            if len(latest_info) == 0:
                print('No person found')
                latest_info = [name,'not found','not found', 'not found']
            # clear search box
            self.driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input').clear()
            output.loc[len(output)] = latest_info
        return output








    
