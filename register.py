import pypandoc
import os

f = open('README.rst','w+')
f.write(pypandoc.convert('README.md', 'rst'))
f.close()
os.system("python ./setup.py register")
os.remove('README.rst')
