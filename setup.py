from codecs import open
import os
from setuptools import setup, find_packages
import pypandoc

'''  
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
'''
try:
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r","") # Do not forget this line
except OSError:
    print("Pandoc not found. Long_description conversion failure.")
    import io
    # pandoc is not installed, fallback to using raw contents
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()
        
        
'''
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()
'''

VERSION = '0.0.13'
DESCRIPTION = 'Option stategy visualizer'
LONG_DESCRIPTION = DESCRIPTION
URL = 'https://github.com/abhijith-git/opstrat'

# Setting up
setup(
    name="opstrat",
    version=VERSION,
    author="Abhijith Chandradas",
    author_email="<abhijith.chandradas@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    license='MIT',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=['matplotlib', 
                      'pandas', 
                      'numpy',
                      'seaborn'],
    keywords=['python', 
              'options', 
              'finance', 
              'opstrat', 
              'data visualization', 
              'stock market'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

#Display README.md in PYPI
#https://stackoverflow.com/questions/26737222/how-to-make-pypi-description-markdown-work

