# coding: utf-8
from os.path import dirname, join

from setuptools import setup

with open(join(dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='pybeautifier',
    version='0.1.0',
    description='Python beautifier tcp server',
    long_description=long_description,
    url='https://github.com/guyskk/pybeautifier',
    author='guyskk',
    author_email='guyskk@qq.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        "Operating System :: POSIX",
    ],
    keywords='beautifier autopep8 yapf isort',
    install_requires=['python-daemon>=2.1.2'],
    py_modules=["pybeautifier"],
    entry_points={
        'console_scripts': [
            'pybeautifier=pybeautifier:main',
        ],
    },
)
