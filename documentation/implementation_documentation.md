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
- *pathfinding.py* module
    - module which is run in order to start the application
- *data_for_app.py* module
    - reads base data for app (from csv files), e.g. highway data, city coordinates and distances between them, etc.
- *ui.py* module
    - runs text-based user interface for the user
- *dijkstra.py* module
    - implementation of Dijkstra's shortest path finding algorithm
- *idastar.py* module
    - implementation of IDA* shortest path finding algorithm
- *min_heap.py* module
    - implementation of Min Heap (used in Dijkstra's algorithm)
- *application_test.py* module
    - for automatic testing of the application
- *performance_test.py* module
    - for performance testing between algorithms

## Achieved time and space complexities
In this particular pathdfinding application Finnish map forms a graph where cities are vertices (V below) and highways are edges (E below).

### Dijkstra's Algorithm
- Time complexity: O(V + E log V)
- Space complexity: O(E)

#### Reasoning for Time complexity
Pseudocode for Dijkstra's algorithm together with comments about time complexity:
  
*01* for each V: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(V) as initialization done for each vertex once*  
*02* &nbsp;&nbsp;&nbsp;&nbsp;distance[V] = infinity  
*03* &nbsp;&nbsp;&nbsp;&nbsp;processed[V] = False  
*04* while not processed[ending_city]: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(V) as each vertex (city) is processed zero or one times*  
*05* &nbsp;&nbsp;&nbsp;&nbsp;next_city = heap.pop() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1) - constant time operation from heap*  
*06* &nbsp;&nbsp;&nbsp;&nbsp;if not processed[next_city]: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1) - truth comparison for value from dictionary*  
*07* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;processed[next_city] = True &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1) - set value to dictionary*  
*08* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for edge_and_neighbor in adjacency_list[next_city]: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(E) as all edges can start from current vertex*  
*09* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E = edge_and_neighbor[0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*10* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor = edge_and_neighbor[1] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*11* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if distance[next_city] + E < distance[neighbor]: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1) - truth comparison for two values from dictionaries*  
*12* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance[neighbor] = distance[next_city] + E &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1) - set value to dictionary*  
*13* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;heap.push(neighbor) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(log V) is the time complexity for inserting new item into min heap and heapifying to preserve min heap property*  
  
Each vertex and each edge is processed at maximum once in rows 4 and 8, which is O(V + E).  
Then, for each edge, pushing to heap is done in O(log V) time in row 13, which results in total time complexity of O(V + E log V) for the algorithm.  

#### Reasoning for Space complexity
Data structures:
- distances-dictionary: space complexity of O(V) as distance is recorded to each vertex (city)
- processed-distionary: space complexity of O(V) as processed flag is recorded for each vertex (city)
- min heap: space complexity of O(E) as each edge can be added to the heap once at maximum. If each vertex is connected to all other vertices, number of connections (edges E) is V^2. This is for a dense graph. For a sparse graph space complexity is much better, i.e. the less edges E, the better space complexity
  
E <= V^2, so resulting space complexity of algorithm is O(E).

### IDA* Algorithm
- Time complexity: O(b^d), where b is branching factor and d is depth of first solution
- Space complexity: O(d)

#### Reasoning for Time complexity
Pseudocode for IDA* algorithm together with comments about time complexity:
  
*01* helper_function(current_vertex, cost_to_vertex, threshold):  
*02* &nbsp;&nbsp;&nbsp;&nbsp;if current_vertex==end_vertex: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*03* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return "FOUND!" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*04* &nbsp;&nbsp;&nbsp;&nbsp;f_score = cost_to_vertex + heuristics[current_vertex] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*05* &nbsp;&nbsp;&nbsp;&nbsp;if f_score > threshold: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*06* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return f_score &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*07* &nbsp;&nbsp;&nbsp;&nbsp;min_f_score = MAX_INT &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*08* &nbsp;&nbsp;&nbsp;&nbsp;for neighbor_and_cost in adjacency_list[current_vertex]: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(b) as number of neighbors = number of branches*  
*09* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor, weight = neighbor_and_cost[0], neighbor_and_cost[1] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*10* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return_value = helper_function(neighbor, cost_to_vertex+weight, threshold)  
*11* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if return_value == "FOUND!": &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*12* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return "FOUND!" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*13* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if return_value < min_f_score &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*14* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_f_score = return_value &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*15* &nbsp;&nbsp;&nbsp;&nbsp;return min_f_score &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*16*  
*17* while True: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(d), so while loop is looped the less times to more depth there is in first solution (the larger the threshold initially)*  
*18* &nbsp;&nbsp;&nbsp;&nbsp;return_value = helper_function(start_vertex, 0, initial_threshold)  
*19* &nbsp;&nbsp;&nbsp;&nbsp;if return_value == "FOUND!": &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*20* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return "FOUND!" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
*21* &nbsp;&nbsp;&nbsp;&nbsp;threshold = return_value &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *O(1)*  
  
From rows 8 and 17 it can be inferred that time complexity of IDA* is O(b^d).  
Intuitively, the more depth there is in first solution (the larger the threshold initially), the less solutions are found and the faster the running time is.  
Similarly, the less branching there is from vertices, the less solutions are found and the faster the running time.  

#### Reasoning for Space complexity
IDA* is a space-optimized algorithm, so it does not store any information (except current threshold) between iterations.  
It starts to search for the solution from the start vertex at each iteration, only threshold value is increased between iterations.  
IDA* stores information only of current iteration, so amount of space depends on depth of the iteration, thus space complexity of O(d).  

## Performance comparison and O-analysis comparison
TBD

## Possible shortages in app and improvement ideas
TBD

## Sources
### Sources for algorithms, data structures and application implementation:
- Lecture slides by Jyrki Kivinen for courses 'Tietorakenteet ja algoritmit I-II' (University of Helsinki's courses)
- https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
- https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
- https://en.wikipedia.org/wiki/Iterative_deepening_A*
- https://algorithmsinsight.wordpress.com/graph-theory-2/ida-star-algorithm-in-general/
- https://matplotlib.org/stable/tutorials/index.html
### Sources for geographic data:
- https://fi.wikipedia.org/wiki/Valtatiet_Suomessa
- https://fi.wikipedia.org/wiki/Suomen_tieverkko
- https://fi.wikipedia.org/wiki/Suomen_moottoritieverkko
- https://fi.wikipedia.org/wiki/Luettelo_Suomen_kuntien_koordinaateista
