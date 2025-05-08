from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function will return a list of requirements'''
    with open(file_path) as f:
        requirements = [line.strip() for line in f.readlines()]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="MLProject1",
    version='1.0.0',
    author="Bhagat Singh",
    author_email="3836bhagatsingh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('./requirements.txt')
)
