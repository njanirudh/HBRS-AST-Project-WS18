# HBRS-AST-Project-WS18

## Authors
* Anirudh Narasimamurthy Jayasimha
* Sasi Kiran Gaddipati

## Overview

The goal of this software is to take output from different sensors and then process them to give combined result.    
Project link : https://github.com/njanirudh/HBRS-AST-Project-WS18

## Week 1 Update :

* Since the architecture of the code was well designed and the classes were properly decoupled, no major refactoring was required.
* The code already had provisions to add extra sensors and algorithms so no major class changes were made.
* Only a minor bug was found for one of the test case so a single line code change could solve the problem. More about the bug is given in the 'error_report.md'.

## Requirements

For the initial prototype of the sensor fusion project the following are the requirements that are used.

* Language : Python 3.6
* Coding Standard : PEP08
* Testing Framework : python unittest
* Data structure : 
    * Input : list of tuples    
    * Output: list of tuples    
* Design Patterns : Bridge design pattern

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





