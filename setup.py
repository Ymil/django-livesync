import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django3-livesync',
    version='1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='TODO',
    long_description=README,
    url='https://github.com/Ymil/django-livesync',
    author='Fabio Gibson',
    author_email='fabiogibson.rj@gmail.com',
    install_requires=['watchdog>=2.*', 'tornado>=6.*', 'websocket-client>=1',],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
