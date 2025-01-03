#%% import libraries
from auto_search.src import AutoSearch
import getpass
import pandas as pd
from auto_search.config import *
import os

#%% main function
def run_main():
    #%% get username and password
    username = input('Please input your LinkedIn username: ')
    password = getpass.getpass('Please input your LinkedIn password: ')

    #%% initialize AutoSearch class
    auto_search = AutoSearch()
    #%% login
    auto_search.login(username, password)
    print('Login success.')

    #%% search people
    name_list = pd.read_excel(os.path.join(input_path, input_filename))
    search_result = auto_search.search_people(name_list, area=None, company=None)
    search_result.to_excel(os.path.join(output_path, output_filename), index=False)

    return None

#%% additional functions
def check_install():
    print("Install success.")
    return None

#%%
if __name__ == "__main__":
    run_main()
