ldflajfolasjd
# Pokemon Card Evaluation Web App
## Contents
* [Brief](#brief)
   * [Scope of Project ](#Scope-of-project)
   * [My Approach](#my-approach)
* [Architecture](#architecture)
   * [Database Structure](#database-structure)
   * [CI/CD Pipeline](#CI/CD-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-End Design](#front-end-design)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)



## Brief

 We have been asked to create an application with the overall objective of having CRUD application with the utilisation of supporting tools, methodologies and technologies which uses the modules that we have covered during the training to creat a CI/CD pipeline. 

### Scope of Project

These are the requirements for the project as it follows:
* A Trello board with full expansion on user stories, use cases, and tasks needed to be complete the project
* Clear documentation from a design phase describing the architecture used for the project, including a detailed Risk Assessment 
* The application needs to be fully integrated with using the branch feature within GitHub, which will be built through CI server and deployed to a cloud-based virtual machine.
* If a change is made to the code base, then the webhook integrated into GitHub will be used, so that jenkins recreates and deploys the changed application
* Project should follow service oriented architecture 
* The project is deployed using containerisation and an orchestration tool
* Creation of an Ansible playbook that will provision the environment which is required for the application to run. 
* The use of nginx as a proxy load balancer 

### My Approach 
To achieve the requirements, I decided to create a web app which generates pokemon cards with the name of the pokemon, the type, the PSA value and the evaluation price of the card. This is achieved through the four services created by docker containerisation. The desire to create this web app was because I was fascinated with the economics of pokemon cards. The functionalities of services are:
#### Service 1
* Storing information in SQL of the pokemon card storing:
    * *Pokemon Name*
    * *PSA*
    * *Evaluation price*
* Front-end development 
    * *Shows the value generated from service 2, service 3 and service 4*
    * *Use of index.html as a front-end*
* Docker file to containerise service 1

#### Service 2
* Generate a Random Pokemon 
* Send information to service 1 and 4
* Docker file to containerise service 2

#### Service 3
* Generate a Random PSA 
* Send information to service 1 and 4
* Docker file to containerise service 3

#### Service 4
* Recieve Information from service 2 and 3 
    * *Use the information to assign an evalution value*
    * *Send information back to service 1 to be shown in the front-end* 
* Docker file to containerise service 4

![COMP][componet]


## Architecture 
### Database Structure 
Below I have included an ER diagram which showcases the structure of the database used for the web app. In regards to the ER diagram, it shows all the necessary components implemented in the SQL database.
The project did not have an emphasis on the database therefore it was only necessary to create only one table as it is enough to complete the application. 
 
![ERD][erd1]

### CI/CD Pipeline

#### Initial Pipeline
![CI][ciPipe]
Initially, the pipeline was created with limited use as it was mainly done for testing and learning. The first pipeline is a combination of the first project with the addition of docker to containerise the application which was refactored to fit the specification of the project. 


### Pipeline Progression
![CI][ciPipe2]
When the pipeline was progressing through continuous integration to continuous deployment, orchestration tool was added such as Ansible for the creation and management of the swarm hosting the containers. 

### Role of GitHub
Github is used as a source code management tool when code is pushed from development to different branches of GitHub for different features of the application. It is the starting and essential part of the pipeline as it hosts all of the instructions for the different tools used. A webhook is inserted so Github can communicate with Jenkins whenever there is a change in the repository to automate the start of a build. Below shows the image of all the branches that were created when trying to complete the project as initially the project started with the main and development branch. 
![GIT][gitbranch]

### Role of Jenkins
The role of Jenkins is that it is an automation server, which is used in the current project to automate testing, building, delivering and deploying the application. Jenkins has different changes, starting with pulling the information from the Github repository. After that, the first task that Jenkins pipeline performs is running the test followed by, build & push, config management, deploy and post actions respectively. This is seen in the image below showing the successful build of the application.
![JEN][jenkins_stage]

As you can that there was progression from unstable build to a stable one. This was mainly because some tests did not pass and jenkins was informed of that, prompting the user that there might be some issues. To resolve the issue of the unstable build, more tests were written and code was refractored to get a pass value when conducting the tests which is the reason why the recent build was registered as stable. 

### Role of Docker & Docker-compose
The role of docker was to containersie the application to encapsulate everything that the application needs to run, which allows the application to be easily moved to different environments. The role of docker-compose was to run multiple containers and making it easier to configure the containers with the use of only one file.

### Role of Ansible 
Ansible is an open-source software provisioning, configuration management, and application-deployment tool. For the proposed project we use the ansible play book to create a docker swarm which has the manager, worker and nginx virtual machines connected.Ansible installs docker within the worker and manger node to run the docker-compose file which contains the application. The role of the Nginx is to be a load blancer and act as a reverse proxy making the swarm safe as it add another layer of safety. 



## Project Tracking
For the project tracking I have used the Trello board which can be accessed through here.(https://trello.com/b/l8N6EQ8l/pokemon-card-project)
![TRELL][trello]

The Trello board contains:
* *Backlog* In which all of the cards are initially added when the requirements gathering is done. This allows the cards to progress from backlog to being done, which is a movement from left to right. 

* *User Stories* A user story looks at the requirements in the view of the client to better the web app to meet client satisfaction.

* *To-Do* This is where an element is being considered to be implemented 
* *Doing* This is where an element is being built, when code has been written for it .
* *Testing* After an element is completed it is then moved to testing, to see if the element works as intended. 
* *Done* After a review if the element is considered to be finished it is then moved to the done section. 


## Risk Assessment
The full risk assessment can be found by clicking on this link:(https://docs.google.com/document/d/12_SSrU0dpaW754nMieaN5lIhmecfGiWq7A7hjq-EDbQ/edit?usp=sharing)

### Risk Assessment 
![risk][risk1]
![risk][risk2]
![risk][risk3]

## Testing
After the application was created, it was moved to the testing stage in which pytest was used for the unit test in Jenkins. When conducting the unit test there was coverage of 100% of the code in all of the services. 
![unit][unit_test1]
When conducting the test on service 1 it was initially difficult to get 100% coverage and test the functionalities as the test relied upon the information from service 2, service 3 and service 4. Therefor, in service 1 testing mock test was used to act as the different services feeding the information in, to test service 1. 
![unit][unit_test2]
The second service was tested to see if the correct pokemon was given and the correct information was returned. It was checked by ussing the assert statement. 
![unit][unit_test3]
With the service 3 test above, the test is used to check if the correct random value is returned and checked through the assert statement.
![unit][unit_test4]
With the service 4 test above, it checks when the information is given from service 2 and service 3 that the correct evaluation value is assigned. By having a 100% coverage it does not mean the application is unbreakable or fully functional. There could be external factors that could lead to the application having a crash and not running as intended. However, pytest does give a good gauge on the stability of the application. 

## Front-End Design
The front end design does not have any CSS styling as it was not deemed necessary as there was more emphasis on the functionalities of the web app rather than the look of it.

![HP][home_page]


## Known Issues
There are no known issues related to the web app. It runs as intended 
## Future Improvements
There are many imporvements to be made for this web app to become a fully functioning application:
* Add more pokemon cards
* Add user logins to store the values personally and compare with other people
* users can view each other's cards 

## Authors
Abaseen Popal

## Acknowledgements
* QA Community 
* Harry Volker



[erd1]: https://i.imgur.com/xOM34SI.png
[erd2]: https://i.imgur.com/pBEegGz.png
[ciPipe]: https://i.imgur.com/ZePjK1G.png
[ciPipe2]: https://i.imgur.com/4R0VGQg.png
[gitbranch]: https://i.imgur.com/P7FwZMs.png
[jenkins_stage]: https://i.imgur.com/RXCVXjD.png
[componet]: https://i.imgur.com/P8jOGeD.png
[trello]: https://i.imgur.com/jU63B5u.png
[risk1]: https://i.imgur.com/xiIWjdr.png
[risk2]: https://i.imgur.com/ad6pVAv.png
[risk3]: https://i.imgur.com/4N2Xe8o.png
[home_page]:https://i.imgur.com/sV2V1Hy.png
[unit_test1]: https://i.imgur.com/u8bwJc2.png
[unit_test2]: https://i.imgur.com/fmJwrRG.png
[unit_test3]: https://i.imgur.com/kCAAasc.png
[unit_test4]: https://i.imgur.com/SQIXT3w.png


