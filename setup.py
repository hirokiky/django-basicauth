import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='django-basicauth',
    version='0.5.2',
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    url='https://github.com/hirokiky/django-basicauth/',
    license='MIT',
    description="Basic auth utilities for Django.",
    long_description=README + '\n\n' + CHANGES,
    packages=['basicauth'],
    install_requires=['Django>=1.11'],
    include_package_data=True,
    test_suite="tests",
    zip_safe=False,
)
