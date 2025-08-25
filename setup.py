from setuptools import find_packages,setup
from typing import List

def get_requirements (file_path:str)->List[str]:
    #to get list of dependencies 

    hyphen_cmd = '-e .'

    requirements = []
    with open(file_path) as file_obj:# resd file object
        requirements = file_obj.readlines() #read lines from file object
        requirements = [req.replace("/n", "")for req in requirements] #remove /n from text

    if hyphen_cmd in requirements:
        requirements.remove(hyphen_cmd)
    

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Janhavi',
    author_email = 'janhavikhurkhuriya@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirement.txt')

)