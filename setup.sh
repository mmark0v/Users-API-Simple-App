#!/bin/bash

virtualenv --version > /dev/null

if [ $? != 0 ]
then
	echo -e "No virtualenv installed. Installing virtualenv...\n\n"
	sleep 3
	pip3 install virtualenv
fi

virtualenv .env && source .env/bin/activate && pip install -r requirements.txt

echo -e "\n\n\n *** Setup Completed! You can run the app now: ./app.py"
