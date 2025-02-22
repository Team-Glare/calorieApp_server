https://ncsu.zoom.us/rec/share/CNF2zaJt9LmGBn8Th5oQkC5gRwh7CtANJ4T3ss__BUTH0_77HYDxxvDYIEJ-xry0.7LsEsX3jtU2T1Q_9?startTime=1638606669000

[![GitHub license](https://img.shields.io/github/license/Team-Glare/calorieApp_server)](https://github.com/Team-Glare/calorieApp_server/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/429486727.svg)](https://zenodo.org/badge/latestdoi/429486727)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://app.travis-ci.com/atharva1996/calorieApp_server.svg?branch=main)](https://app.travis-ci.com/atharva1996/calorieApp_server)
[![codecov](https://codecov.io/gh/Team-Glare/calorieApp_server/branch/main/graph/badge.svg?token=myVYbaJLaw)](https://codecov.io/gh/Team-Glare/calorieApp_server)
[![Super Linter](https://github.com/Team-Glare/calorieApp_server/actions/workflows/super-linter.yml/badge.svg)](https://github.com/Team-Glare/calorieApp_server/actions/workflows/super-linter.yml)
![GitHub issues](https://img.shields.io/github/issues/Team-Glare/calorieApp_server)
![last commit](https://img.shields.io/github/last-commit/Team-Glare/calorieApp_server)
![total lines](https://img.shields.io/tokei/lines/github/Team-Glare/calorieApp_server)



# BurnOut

![WhatsApp Image 2021-09-28 at 2 48 00 PM](https://user-images.githubusercontent.com/25662536/135546154-cfae1d2e-439a-4edc-b0bb-57f693ef5a83.jpeg)

BurnOut is an easy to use application that keeps track of a user's daily calories - gained and burnt. It can help the user to set goals such as weight loss or gain. Users can edit their profile by entering their height, weight, goal and targeted-weight. Users can enroll into numerous programs involving fitness such as yoga classes and workout sessions. They can also connect with their friends by sending a friend-request and share their progress. This document provides a major perspective for the users to understand and take up the project as an Open source software and add on multiple features before releasing to the market. This repo aids the developers in understanding the code and acts as a reference point for continuing the project. 

## Improvements:

* Written unit tests with proper mocking and increased the code coverage from 56% to 98%
* Deployed local mongo server to MongoAtlas
* Added Linter and Code formatter in the CI pipeline
* Added Software Documentation
* Improved Contributing.md

# Table of Contents  

- [Why use BurnOut?](#why-use-burnout)
- [Implementation](#implementation)
- [TechStack Used for the Development of Project:](#techstack-used-for-the-development-of-project)
- [Core Functionalities of the Application:](#core-functionalities)
  - [Register](#register)
  - [Login](#login)
  - [Set User Profile](#set-user-profile)
  - [Enter Calories in and burnt](#enter-calories-in-and-burnt)
  - [Check History](#check-history)
  - [User History Plot](#user-history-plot)
  - [Adding Friends](#adding-friends)
  - [Enrolling into several programs](#enrolling-into-several-programs)
- [Steps for Execution:](#steps-for-execution)
- [Source Code](#source-code)
- [Future Scope](#future-scope)
- [Team Members](#team-members)
- [Contribution](#contribution)
- [License](#license)


# Why use BurnOut?
 - User can keep a track of their calorie intake.
 - User just needs to input the food they've had, calories get calculated automatically.
 - Displays a record of calories in and calories burnt out day wise in History tab.
 - Helps user to figure out how much to eat/exercise according to their desired goal(weight loss/gain).
 - Users can connect with their friends and keep track of each other's progress
 - Enrollment into numerous yoga and workout sessions.
 - Accessible to everyone and easy to use.

# Implementation

Link to the implementation video of the BurnOut application:

https://user-images.githubusercontent.com/89509351/140230712-749bbc0d-d2dd-4c5b-9ec3-6ee51f918aac.mp4

# TechStack Used for the Development of Project

 <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="python" width="20" height="20"/> Python </br>
 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg" alt="mongo" width="20" height="20"/> MongoDB </br>
 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-plain.svg" alt="html" width="20" height="20"> CSS3 </br>
 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-plain.svg" alt="css" width="20" height="20">  HTML 5 </br>
 
# Core Functionalities of the Application
 
 ## Register
 
https://user-images.githubusercontent.com/89509351/140233499-0dba701b-1896-4285-918b-cfee1c63be5a.mp4

 ## Login

https://user-images.githubusercontent.com/89509351/140233566-78a1c729-e14b-4f57-9fa1-b2f84be26b6f.mp4

 ## Set User Profile
 
https://user-images.githubusercontent.com/89509351/140233630-c746f7b6-3d06-4ca7-b79c-c511c63726e6.mp4


 ## Enter Calories in and burnt

https://user-images.githubusercontent.com/89509351/140234074-47fb2fb3-6542-4cec-89d6-b2ec5f7359bc.mp4


 ## Check history

https://user-images.githubusercontent.com/89509351/140234173-c279e3e8-7b67-4d6b-9e20-268a99108622.mp4







## User History Plot

We have used python in the backend to fetch the current weight and goal weight of a person from python collection. We have also implemented a diet recommendation model which gives the user a 30 day diet plan stored in [diet_guide.txt](https://github.com/atharva1996/calorieApp_server/blob/main/model/diet_guide.txt) and intend to integrate this with the application in the further stage of this project. The graphs below demonstrate weight loss prediction if the diet is followed as prescribed.

![alt-text-1](https://user-images.githubusercontent.com/62328699/140241250-b972c6fa-550d-433f-aaa7-04fc0df97a8a.png "title-1") ![alt-text-2](https://user-images.githubusercontent.com/62328699/140241265-f3bb552a-cdfe-47ed-9184-f78a082441c8.png "title-2")






 ## Adding Friends 
 
https://user-images.githubusercontent.com/89509351/140234231-35b85d94-2293-48a8-86f8-fdc485f31cd1.mp4
  
 ## Enrolling into several programs
 
https://user-images.githubusercontent.com/89509351/140389545-6cbeae48-4e5d-4166-a455-912e58972838.mp4


 # Steps for execution
 
 Step 1:
 Install MongoDB using the following link:
 
 https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows
 
 Step 2: 
  Git Clone the Repository 
  
    git clone https://github.com/atharva1996/calorieApp_server.git
    
  (OR) Download the .zip file on your local machine
  
    https://github.com/atharva1996/calorieApp_server.git
  
 Step 3:
   Install the required packages by running the following command in the terminal 
   
    pip install -r requirements.txt
    
 Step 4:
    Run the following command in the terminal
    
    python application.py
    
 Step 5:
    Open the URL in your browser:  
      http://127.0.0.1:5000/
      
      
 
  
  # Future Scope
  
  The  following features can be implemented in the future scope of this application:
  
   1. Predicting workout plans for users based on their history and fitness reports.
   2. Create a mobile application for the web version of the application.
   3. Make the website view port adaptable - the website should look good on phone, tablet and computer.
   4. Chat functionality for friends
   5. Share workout plans with friends
   6. Creating an Activities dashboard based on user enrollment
   7. Track user progress for each activity he/she enrolled for.
   
  # Team Members
   
 * [Setu Kumar Basak](https://github.com/setu1421)  
* [Conor Thomason](https://github.com/ConorThomason)  
* [Keertana Vellanki](https://github.com/KeertanaVellanki)  
* [Muntasir Hoq](https://github.com/muntasirhoq)  
* [Matthew Sohacki](https://github.com/msohacki)  
 
# Contribution
  
Please refer the CONTRIBUTING.md file for instructions on how to contribute to our repository.

# License
  
  This project is licensed under the MIT License.
  
  

