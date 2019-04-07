from setuptools import setup, find_packages

setup(
    name='network_optimization',
    version='1.0',
    url='https://github.com/DrCapa/network_optimization',
    author='Rico Hoffmann',
    author_email='rico.hoffmann@libero.it',
    description='README',
    packages=find_packages(),
    install_requires=['pandas >= 0.23.4', 'pyomo >= 5.6.0',
                      'numpy >= 1.15.2'
                      ]
)
