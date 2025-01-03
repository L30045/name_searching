# name_searching
Search people on a given website.

## Requirements
- Python 3.10+
- Selenium
- ChromeDriver (Tested on Windows 11, Have not tested on other OS)

## Data preparation
- Create a xlsx file with the following columns: `name`, `company`, `area`.
- Put the file in the `data` folder.

## Usage
In terminal, run:
```
python -m auto_search
```

## Result
- The result will be summarized in a xlsx file with the following columns: `name`, `title`, `company`, `area`.
- The result will be saved in the `output` folder.

## Note
- The searching process only matches the name.
- In the future, the package will be able to filter by name, company, and area.
- setup_beta.py is a script to automatically setup the package. It is still in beta. Not recommended to use it.




