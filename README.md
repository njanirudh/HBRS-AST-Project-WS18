# HBRS-AST-Project-WS18

## Authors
* Anirudh Narasimamurthy Jayasimha
* Sasi Kiran Gaddipati

## Overview

The goal of this software is to take output from different sensors and then process them to give combined result.
Project link : https://github.com/njanirudh/HBRS-AST-Project-WS18

## Requirements

For the initial prototype of the sensor fusion project the following are the requirements that are used.

* Language : Python 3.6
* Coding Standard : PEP08
* Testing Framework : python unittest
* Data structure : 
    * Input : list of tuples    
    * Output: list of tuples    

## Design Choices

* Algorithm :
    * Each computer vision algorithm is a seperate class .
    * 'algorithm_abstract_class.py' holds the basic structure of the Algorithm class.
    * This structure can help in adding multiple algorithms to the software and test them when required.
    
* Sensor :
    * Each sensor is a seperate class.
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
    * For the current scenario the input can directly without intermidiate conversion. As the output from the 
    the sendor gets more complex data can be stored and transfered as JSON to improve portablity and easy 
    serializing and deserializing.
    




