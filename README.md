# name_searching
Search people on a given website.

## Requirements
- Python 3.10+
- Selenium
- ChromeDriver (Tested on Windows 11, Have not tested on other OS)

## Installation
- Clone the repository and navigate to the folder.

### setup the environment
```
conda env create -f env.yaml
conda activate test-env
```

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
- The searching process only matches `name`.
- In the future, the package will be able to filter by `name`, `company`, `area`.




