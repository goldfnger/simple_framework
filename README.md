## Project description
Automation framework for cms Opencart.  
Currently supported only local run of tests, but could be extended to run them remotely on Selenoid.  

### List of required pre-installed utilities
* Python3 - to run tests
* Docker Desktop - to build, run and manage docker containers
* Allure - to generate report

### How to run Opencart
* Docker Desktop should be running
* go to root directory of project
* in terminal run a command
  * docker-compose up -d
  
If you made any changes to docker-compose.yml and want to make sure that they are applied use following commands
```
docker-compose down - will also remove containers

Delete all volumes:
docker volume rm $(docker volume ls -q)

Run containers:
docker-compose up -d
```
## Project preparation
* Clone project
* Set and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
* Update pip and install project requirements
```
pip install -U pip
pip install -r requirements.txt
```
* Run Opencart container from terminal or Docker Dekstop

## To run tests locally
From project root using console or IDE terminal run a command:
```
pytest --local --tester='your value'

full command looks like:
pytest --local  --url=your_ip --browser-name=(firefox/chrome) -m marker -n 2
```
Here are options which u can use:  
* -n - allow to set how many threads would be used to speed up test run, if key is not set - by default would in run in a single thread.
* --local - to run tests locally.
* --url - host adress where Opencart is located. e.g. localhost or 127.0.0.1 
* --browser-name - to set a browser for tests. by default is set chrome, but firefox is supported also.
* -m - marker for group of tests. you can find marker names in tests or pyproject.toml

## To generate test report
use command
```
allure generate -c ; allure open
```
