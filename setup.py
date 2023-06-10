from setuptools import find_packages,setup
from typing import List


Hypen_E_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    
    if Hypen_E_dot in requirements:
        requirements.remove(Hypen_E_dot)   
        
    return requirements

setup(
    name = 'DiamondPricePrediction',
    version = '0.0.1',
    author = 'Prajwal',
    author_email = 'prajwalkuhite50@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)