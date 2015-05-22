import pypandoc
import os

f = open('README.rst','wb')
f.write(pypandoc.convert('README.md', 'rst').encode('utf-8'))
f.close()
os.system("python ./setup.py register")
os.remove('README.rst')
