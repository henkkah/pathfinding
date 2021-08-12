# Implementation Documentation
*Author:* Henrik Harjula  
*Course:* Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit (loppukesä 2021)  
*Study program:* Mathematical Sciences (Matemaattiset tieteet)  
*Programming language for project:* Python  

## Topic
Topic of this project is to make a pathfinding application. Two (shortest) pathfinding algorithms are used to compare their effectiveness (in terms of runtime) in finding the quickest path from one Finnish city to another Finnish city using Finnish highways (valtatie in Finnish). Speed limits of different highways are taken into account. Purpose is to find the quickest path(s) (not necessarily shortest) when driving with car. Application is used from command line – when a shortest path is queried, then a popup window visualizing resulting shortest path(s) is opened.

## General structure of application
Application is used from command line by running 'src/pathfinding.py' in root folder of the project.  
Application consists of several modules described below.  
- pathfinding.py module is the module which is run in order to start the application
- data_for_app.py module reads base data for app (from csv files), e.g. highway data, city coordinates and distances between them, etc.
- ui.py module runs text-based user interface for the user
- dijkstra.py module is the implementation of Dijkstra's shortest path finding algorithm
- min_heap.py module is the implementation of Min Heap (used in Dijkstra's algorithm)
- application_test.py module is for automatic testing of the application

## Achieved time and space complexities
In this particular pathdfinding application Finnish map forms a graph where cities are vertices (V below) and highways are edges (E below).

### Dijkstra's Algorithm
- Time complexity: O(V + E log V)
- Space complexity: O(E)

#### Reasoning for Time complexity
Pseudocode for Dijkstra's algorithm together with comments about time complexity:
  
(1) for each V:							O(V) as initialization done for each vertex once  
(2)     distance[V] = infinity  
(3)     processed[V] = False  
(4) while not processed[ending_city]:				O(V) as each vertex (city) is processed zero or one times  
(5)     next_city = heap.pop()					O(1) - constant time operation from heap  
(6)     if not processed[next_city]:				O(1) - truth comparison for value from dictionary  
(7)         processed[next_city] = True				O(1) - set value to dictionary  
(8)         for edge_and_neighbor in adjacency_list[next_city]:	O(E) as all edges can start from current vertex  
(9) 	    E = edge_and_neighbor[0]				O(1)  
(10)	    neighbor = edge_and_neighbor[1]			O(1)  
(11)	    if distance[next_city] + E < distance[neighbor]:	O(1) - truth comparison for two values from dictionaries  
(12)		distance[neighbor] = distance[next_city] + E	O(1) - set value to dictionary  
(13)		heap.push(neighbor)				O(log V) is the time complexity for inserting new item into min heap and heapifying to preserve min heap property  
  
Each vertex and each edge is processed at maximum once in rows 4 and 8, which is O(V + E).  
Then, for each edge, pushing to heap is done in O(log V) time in row 13, which results in total time complexity of O(V + E log V) for the algorithm.  

#### Reasoning for Space complexity
Data structures:
- distances-dictionary: space complexity of O(V) as distance is recorded to each vertex (city)
- processed-distionary: space complexity of O(V) as processed flag is recorded for each vertex (city)
- min heap: space complexity of O(E) as each edge can be added to the heap once at maximum. If each vertex is connected to all other vertices, number of connections (edges E) is V^2. This is for a dense graph. For a sparse graph space complexity is much better, i.e. the less edges E, the better space complexity
E <= V^2, so resulting space complexity of algorithm is O(E).  

### IDA* Algorithm
TBD

## Performance comparison and O-analysis comparison
TBD

## Possible shortages in app and improvement ideas
TBD

## Sources
### Sources for algorithms, data structures and application implementation:
- Lecture slides by Jyrki Kivinen for courses 'Tietorakenteet ja algoritmit I-II' (University of Helsinki's courses)
- https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
- https://matplotlib.org/stable/tutorials/index.html
### Sources for geographic data:
- https://fi.wikipedia.org/wiki/Valtatiet_Suomessa
- https://fi.wikipedia.org/wiki/Suomen_tieverkko
- https://fi.wikipedia.org/wiki/Suomen_moottoritieverkko
- https://fi.wikipedia.org/wiki/Luettelo_Suomen_kuntien_koordinaateista
