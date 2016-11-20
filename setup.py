from os.path import dirname, join

from setuptools import setup

with open(join(dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='pybeautifier',
    version='0.0.1',
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='beautifier autopep8 yapf isort',
    py_modules=["pybeautifier", "pybeautifier_server"],
    entry_points={
        'console_scripts': [
            'pybeautifier=pybeautifier:main',
        ],
    },
)
