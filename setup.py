import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = ['urllib3']

setup(name='pyredpen',
      version='0.0.1',
      description='RedPen client',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Java",
        ],
      author='Takahiro Yoshimura',
      author_email='altakey@gmail.com',
      url='https://github.com/taky/pyredpen',
      keywords='natural language processing japanese english correction',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      entry_points = {'console_scripts':['validate = redpen.shell:validate']}
      )
