# Testing Documentation
*Author:* Henrik Harjula  
*Course:* Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit (loppukesä 2021)  
*Study program:* Mathematical Sciences (Matemaattiset tieteet)  
*Programming language for project:* Python  

## Topic
Topic of this project is to make a pathfinding application. Two (shortest) pathfinding algorithms are used to compare their effectiveness (in terms of runtime) in finding the quickest path from one Finnish city to another Finnish city using Finnish highways (valtatie in Finnish). Speed limits of different highways are taken into account. Purpose is to find the quickest path(s) (not necessarily shortest) when driving with car. Application is used from command line – when a shortest path is queried, then a popup window visualizing resulting shortest path(s) is opened.

## Test reports
[Test coverages](https://github.com/henkkah/pathfinding/tree/master/documentation/test_coverages)  
[Pylint ratings](https://github.com/henkkah/pathfinding/tree/master/documentation/pylint_ratings)  

## What and how was tested
Currently (13.8.2021), working of Dijkstra's algorithm and self-coded Min Heap have been tested.  
Testing was done by creating an example graph and an example heap, and by determining correct answers which code needs to return in order to work correctly.  

## Inputs for testing
Currently (13.8.2021), one example graph and one example heap have been created for testing working of Dijkstra's algorithm and self-coded Min Heap.  

## Repeating tests
Tests have been written as a test class using Python's unittest library.  
This means that tests can be re-run as many times as wanted.  

## Empirical test results in graphical format
TBD
