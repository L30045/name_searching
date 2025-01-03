#%% import libraries
import os
import platform
import getpass

#%% parameters and paths setting
input_path = 'data/'
output_path = 'output/'
input_filename = 'name_list.xlsx'
output_filename = 'company_list_output.xlsx'
target_url = 'https://www.linkedin.com/'
# check platform and select corresponding webdriver
if platform.system() == "Windows":
    webdriver_path = 'webdriver/chromedriver-win64/chromedriver.exe'
else:
    webdriver_path = 'webdriver/chromedriver-mac-arm64/chromedriver'
# click delay to mimic human behavior
min_click_delay = 1
max_click_delay = 3
# max search results
max_search_results = 3

