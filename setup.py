from codecs import open
import os
from setuptools import setup, find_packages
#import pypandoc

with open('README.md') as readme_file:
    README = readme_file.read()


VERSION = '0.1.4'
DESCRIPTION = 'Option stategy visualizer'
#LONG_DESCRIPTION = DESCRIPTION
URL = 'https://github.com/hashabcd/opstrat'

# Setting up
setup(
    name="opstrat",
    version=VERSION,
    author="Abhijith Chandradas",
    author_email="<abhijith.chandradas@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=README,
    url=URL,
    license='MIT',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=['matplotlib', 
                      'pandas', 
                      'numpy',
                      'seaborn',
                      'yfinance'],
    keywords=['python', 
              'options', 
              'finance', 
              'opstrat', 
              'data visualization', 
              'stock market'],
    classifiers=[
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Financial and Insurance Industry",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Topic :: Scientific/Engineering :: Visualization",
            'Topic :: Scientific/Engineering :: Information Analysis',
            "Topic :: Office/Business :: Financial :: Investment",
            "Topic :: Office/Business :: Financial",
            "Programming Language :: Python :: 3"]
)

#Display README.md in PYPI
#https://stackoverflow.com/questions/26737222/how-to-make-pypi-description-markdown-work

