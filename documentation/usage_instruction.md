# Usage Instruction for PathFinding App
*Author:* Henrik Harjula  
  
Application is started by running "*src/pathfinding.py*" in the root folder of the project.  
*Python3* and *matplotlib* library need to be installed in order to run the app.  
  
Application is used from command line.  
With command *1* one can find shortest path between two given cities,  
with command *2* one can find shortest path between two random cities,  
with command *3* one can see list of available cities,  
and with command *4* one can close the application.  
  
When querying for shortest path, application opens a pop-up window to visualize the shortest path found.  
One can zoom the map by choosing *magnifier* icon from the menu bar on top (fifth icon from left).  
Pop-up window needs to be closed before making a new query.  

## Performance Testing
One can do performance testing for the application by running "*src/performance_testing.py*" in the root folder of the project.  
Application randomly chooses 15 paths and categorizes them into short-, mid-, and long-range paths.  
Application gives summary statistics of performance between the algorithms on these paths as the result.  

## Unit Testing
One can test that algorithms and data structures work as they should as follows.
- *poetry* needs to be installed
- Initialize *poetry*: "*poetry init*"
- Add *pytest* to development environment: "*poetry add pytest --dev*"
- Add *coverage* to development environment: "*poetry add coverage --dev*"
- Open *poetry* session: "*poetry shell*"
- Run *pytest* on src folder: "*coverage run --branch -m pytest src*"
- See report of *pytest*: "*coverage report -m*"
- Close *poetry* session: "*exit*"
  
Pylint code quality testing:
- See *pylint* report: "*pylint src*"
