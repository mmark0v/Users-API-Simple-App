#!/bin/bash

virtualenv --version

if [ $? != 0 ]
then
	echo "No virtualenv installed. RUN: pip install virtualenv"
	exit 1
fi

virtualenv .env && source .env/bin/activate && pip install -r requirements.txt
