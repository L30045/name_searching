#%% import libraries
import platform
import os

#%% parameters and paths setting
git_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(git_path, 'data/')
output_path = os.path.join(git_path, 'output/')
input_filename = 'name_list.xlsx'
output_filename = 'company_list_output.xlsx'
target_url = 'https://www.linkedin.com/'

# check platform and select corresponding webdriver
if platform.system() == "Windows":
    webdriver_path = os.path.join(git_path, 'webdriver/chromedriver-win64/chromedriver.exe')
else:
    webdriver_path = os.path.join(git_path, 'webdriver/chromedriver-mac-arm64/chromedriver')
# click delay to mimic human behavior
min_click_delay = 1
max_click_delay = 3
# max search results
max_search_results = 3

