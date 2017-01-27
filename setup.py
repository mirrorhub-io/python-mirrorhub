'''setup file to install the mirrorhub module'''
from setuptools import setup

setup(name='mirrorhub',
      version='0.1.0',
      description='Module to interact with Mirrorhub.io',
      author='Markus Freitag',
      author_email='fmarkus@mailbox.org',
      license='MIT',
      packages=['mirrorhub'],
      scripts=['bin/init_client.py'],
      install_required=['jinja2'],
      zip_safe=False)
