#!/bin/bash

set -e

rm -r dist/
python setup.py sdist

read -rp "Do you wish release to PYPI? (y/n) " yn
if [[ $yn == "Y" ]] || [[ $yn == "y" ]];then
    twine upload dist/*
fi
