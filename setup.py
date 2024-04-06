from setuptools import find_packages,setup 
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]: # input parameter tat returns a list
    '''
    this will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj: # open the file with file path and make an object of it
        requirements=file_obj.readline() # reading each line but it will also reaad the endof =line character \n which isnt needed
        requirements=[req.replace("\n","") for req in requirements] # removing \n

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # we dont want "-e ."



setup(
    name='Student_performance_prediction',
    version='0.0.1',
    author='Anushree',
    author_email='anushreelgowda12@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)