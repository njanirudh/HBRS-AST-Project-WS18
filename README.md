
[![Build Status](https://travis-ci.org/njanirudh/HBRS-AST-Project-WS18.svg?branch=master)](https://travis-ci.org/njanirudh/HBRS-AST-Project-WS18)
![](https://img.shields.io/github/issues/njanirudh/HBRS-AST-Project-WS18.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/njanirudh/hbrs-ast-project-ws18/badge/master)](https://www.codefactor.io/repository/github/njanirudh/hbrs-ast-project-ws18/overview/master)
[![HitCount](http://hits.dwyl.io/njanirudh/HBRS-AST-Project-WS18.svg)](http://hits.dwyl.io/njanirudh/HBRS-AST-Project-WS18)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/njanirudh/HBRS-AST-Project-WS18/blob/master/LICENSE)


# HBRS-AST-Project-WS18

## Authors
* Anirudh Narasimamurthy Jayasimha
* Sasi Kiran Gaddipati

## Overview

The goal of this software is to take output from different sensors and then process them to give combined result.    
Project link : https://github.com/njanirudh/HBRS-AST-Project-WS18

## Week 2 Update :

* Readme updates : Basic readme of the general working of the software along with design consideration and test cases were already written.
* Integration of Travis CI to the repository and basic [documentation](https://github.com/njanirudh/HBRS-AST-Project-WS18/blob/master/docs/CI.md).
* Comments given for all the issues added or relevant changes made where required
* Test cases and [related documentation](https://github.com/njanirudh/HBRS-AST-Project-WS18/blob/master/docs/error_report.md) are added.
* Documentation about the installation and the relevant files to check for running the code is written in Readme.md.
* Added codefactor.io for code quality check.
* Release version is being created for every update and was also previously done.
* Added badges to the repository


## Week 1 Update :

* Since the architecture of the code was well designed and the classes were properly decoupled, no major refactoring was required.
* The code already had provisions to add extra sensors and algorithms so no major class changes were made.
* Only a minor bug was found for one of the test case so a single line code change could solve the problem. More about the bug is given in the 'error_report.md'.

## Requirements

For the initial prototype of the sensor fusion project the following are the requirements that are used.

* Language : Python 3.6
* Coding Standard : PEP08
* Testing Framework : python unittest
* Code Quality check: CodeFactor.io
* Data structure : 
    * Input : list of tuples    
    * Output: list of tuples    
* Design Patterns : Bridge design pattern

## Installation 

* Make sure you have the required python version given in the Requirements above.
* Download the latest release folder to the required path.(https://github.com/njanirudh/HBRS-AST-Project-WS18/releases)
* Extract the source.zip file and go to 'ast_project_2018' folder.
* Run the 'main.py' file to run a general case of sensor integration with a random test case.     
```python3 main.py```
* To run test case use 'test_cases.py' file. The documentation to create custom test case is given in the file.     
```python3 main.py```

## Design Choices

The design choices are such that S.O.L.I.D principles are being used along with good coding practices to make the code readable , extensible and testable.

* Algorithm :
    * Each computer vision algorithm is a seperate class .
    * This class makes use of the **Bridge design pattern** to decouple abstraction and the implementation of the class.
    * 'algorithm_abstract_class.py' holds the basic structure of the Algorithm class.
    * This structure can help in adding multiple algorithms to the software and test them when required.
    
* Sensor :
    * Each sensor is a seperate class.
    * This class makes use of the **Bridge design pattern** to decouple abstraction and the implementation of the class.
    * 'sensor_abstract_class.py' holds the basic structure of the Sensor class.
    * Each sensor class will be resposible for storing the sensor properties along with the sensor preprocessing.
    * The modular sensor class helps in adding new and removing sensors without affecting structure of the code.
    
* Sensor Fusion :
    * This class holds all the sensors object and process the input to give the combined confidance.
    * The sensors get added by the user or client to the sensorfusion class and then process is called.
    * New sensors can be added without changing the structure of the code.

* Input/Output data :
    * The input data from sensor and output are assumed to be of the form of array of tuples.
    * The tuples consists of the following data :
         - object name : string
         - object id   : int
         - confidance  : int
    * For the current scenario the input is taken directly without intermidiate conversion. As the output from the 
    the sendor gets more complex, data can be stored and transfered as JSON to improve portablity and easy 
    serializing and deserializing.
    

## Features to be added :    
- [ ] Changing datastructure into JSON
- [ ] Adding exception handling throughout the code base
- [ ] Adding logging for the code base
- [ ] Porting the project to C++ 




