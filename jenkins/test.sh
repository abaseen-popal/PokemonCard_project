#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3-venv python3-pip

# Test service 1
cd service_1
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
cd ..

# Test service 2
cd service_2
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
cd ..

# Test service 3
cd service_3
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
cd ..

# Test service 4
cd service_4
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
cd ..