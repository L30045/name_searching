#%% import libraries
from auto_search.src import AutoSearch
import getpass

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

    return None

#%% additional functions
def check_install():
    print("Install success.")
    return None

#%%
if __name__ == "__main__":
    run_main()
