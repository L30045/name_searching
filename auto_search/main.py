#%% import libraries
from auto_search.src import AutoSearch
import getpass
import pandas as pd
import auto_search.config as config
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
    name_list = pd.read_excel(os.path.join(config.input_path, config.input_filename))
    print(name_list)
    # for name in name_list['name']:
    #     auto_search.search_people(name)

    return None

#%% additional functions
def check_install():
    print("Install success.")
    return None

#%%
if __name__ == "__main__":
    run_main()
