'''
Created on 18/02/2014

@author: Edgar Zamora Gomez
'''
from setuptools import setup

import server_twisted

setup(name='twisted',
      version=server_twisted.version,
      description='StackSync API WEB module for OpenStack Swift',
      author='AST Research Group',
      author_email='edgar.zamora@urv.cat',
      url='',
      packages=['server_twisted'],
      requires=['api.v2(==2.0)'])
