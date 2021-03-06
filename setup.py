# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from thummer.meta import VERSION


setup(name='django-thummer',
    author='Matt Austin', author_email='mail@mattaustin.me.uk',
    url='https://github.com/MattAustin/django-thummer',
    description='A website screenshot and thumbnailing app for Django.',
    long_description=open('README.rst').read(),
    version=str(VERSION),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django', 'python-dateutil>=2.0',
        'pyvirtualdisplay>=0.1.0', 'selenium>=2.20.0',
        'sorl-thumbnail>=11.12'],
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
    ],
)

