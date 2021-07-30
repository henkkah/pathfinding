# Weekly Report 2
*Author:* Henrik Harjula  
*Course:* Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit (loppukesä 2021)  

## Working hours during the week
8.5 hours

## Done during the week
- Dropped JPS algorithm from project's topic
- Gathered and added base data for the app (city coordinates, highway data between cities)
- Studied working of Dijkstra's algorithm (mainly repetition from Tira2 course)
- Coded first version of Dijkstra's algorithm
- Coded first version how base data is read into app
- Coded first version of how app finds shortest path between two random cities
- Tested working of coded modules
- Initial thinking and information finding of how map and shortest paths should be visualized (not coded yet)

## How program has evolved?
I have coded first versions of:
- Dijkstra's algorithm
- Reading base data into app from csv:s
- Finding shortest path between two random cities and printing info to user

## What I learned during the week?
I repeated how Dijkstra's algorithm works (did not remember all from Tira2 course).
I also got some initial understanding of how visualization should be done (most likely, with Matplotlib module).

## What remained unclear or created trouble?
Something I noticed when testing shortest path finding with two random cities is that highway data from Wikipedia is not complete - in particular, all intersections between different highways are not in the data, which results in not finding the shortest paths by using those intersections.
I think I need to solve this by manually going through the different highways with Google Maps and by manually collecting the intersection data so that graph is 'complete' and shortest paths can be found.

## What will I do next?
- Study IDA* algorithm and start coding it
- Refactor current modules
- Study how to visualize map and shortest paths - and start implementing
- Enhance automatic testing of the app
