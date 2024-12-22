## Import necessary Libraries
from setuptools import find_packages, setup
from typing import List

## Constants
HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    """ 
    this function will return the list of requirements
    """
    requirements=[]
    
    # Read the requirements file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove the new line from character for requriements
        requirements=[req.replace('\n', "") for req in requirements]
        # Remove the empty string from the list 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements


## Setup the packages and packages details
setup(
name="mlproject",  # Name of the package 
version="0.0.1",   # Version of the package
author="Ashwin",   # Author of the package
author_email="ashwinmehta1234500@gmail.com",  # Author email
packages=find_packages(),   # automatically find the packages for the project
install_requires = get_requirements("requirements.txt") # Get the requriements for the file dependencies.
)