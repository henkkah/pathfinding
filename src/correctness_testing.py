from data_for_app import data_for_app
from dijkstra import dijkstra
from idastar import idastar
from random import randint
from math import sqrt


cities, coordinates, speedlimits, adjlist = data_for_app()

def correctness_test(n):
    """Correctness testing for the algorithms used in the application.
    
    Verifying that Dijkstra's and IDA* algorithms return same shortest paths.
    
    Return value of Dijkstra's algorithm is defined as 'correct' solution for each problem.
    
    Args:
        n: Number of pathfinding problems to be tested
    
    Returns:
        no return value - prints out comparison of returned shortest paths by the algorithms
    """
    
    print("\nCalculating...\n")
    
    test_results = []
    
    for _ in range(n):
        # random start and end cities
        start = cities[randint(0, len(cities)-1)]
        end = cities[randint(0, len(cities)-1)]
        while start == end:
            end = cities[randint(0, len(cities)-1)]
        path = start + "-" + end
        # calculate euclidean distance
        x_diff = coordinates[start][0] - coordinates[end][0]
        y_diff = coordinates[start][1] - coordinates[end][1]
        eucl_dist = sqrt(x_diff**2 + y_diff**2)
        
        # Dijkstra
        dist_dij, path_dij, time_dij = dijkstra(start, end, adjlist)
        # IDA*
        dist_ida, path_ida, time_ida = idastar(start, end, adjlist, coordinates)
        
        test_results.append( (path, path_dij, path_ida) )
    
    # Analysis of results
    paths_same = 0
    ida_not_finished = 0
    different_paths = []
    for test_result in test_results:
        if test_result[1] == test_result[2]:
            paths_same += 1
        elif test_result[2] == "no_path":
            ida_not_finished += 1
        else:
            different_paths.append(test_result)
    print("Out of " + str(n) + " pathfinding problems algorithms produced " + str(paths_same) + " same results and " + str(n-paths_same-ida_not_finished) + " different results.")
    print("(For " + str(ida_not_finished) + " problems IDA* did not finish)\n")
    for different_path in different_paths:
        print("For path " + different_path[0] + " algorithms produced different shortest paths.")
        path_dij_descr = "-".join(different_path[1])
        path_ida_descr = "-".join(different_path[2])
        print("Shortest path by Dijkstra: " + path_dij_descr)
        print("Shortest path by IDA*:     " + path_ida_descr)
        print()


while True:
    n = input("\nHow many pathfinding problems you want to test? (quit with 'q') ")
    if n == "q":
        break
    try:
        n = int(n)
    except:
        print("Give amount of pathfinding problems to be tested as integer.")
    correctness_test(n)


