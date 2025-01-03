from setuptools import setup, find_packages
import subprocess
import sys

# Check if package is already installed using pip list

installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'list']).decode()
if 'auto_search' in installed_packages:
    response = input('auto_search package is already installed. Do you want to reinstall? (y/n): ')
    if response.lower() != 'y':
        print('Installation cancelled.')
        sys.exit()
setup(
    name='auto_search',
    version='0.1.0', 
    author='Chi-Yuan Chang',
    author_email='chiyuan30045+github@gmail.com',
    description="Auto search for the people's profile.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chiyuan30045/name_searching',
    packages=find_packages(),
    install_requires=[
        # Dependencies are listed here
        'selenium>=4.1.0',
        'pandas>=1.3.5',
        'setuptools>=42.0.0',  # Added for pkg_resources
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'install_check=auto_search.main:check_install',
        ],
    },
)