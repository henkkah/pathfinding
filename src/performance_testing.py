from data_for_app import data_for_app
from dijkstra import dijkstra
from idastar import idastar
from time import time
from random import randint
from math import sqrt


cities, coordinates, speedlimits, adjlist = data_for_app()

def performance_test(n):
    """Performance testing for app.
    
    Finding out how well Dijkstra's and IDA* algorithms perform in different pathfinding problems, and analyzing the results.
    
    Pathfinding problems are categorized into short-range, mid-range, and long-range problems based on euclidean distance between start and end cities, and analysis is on top of this.
    
    Args:
        n: Number of pathfinding problems to be tested
    
    Returns:
        no return value - prints out analysis of performance test
    """
    
    def analyze_result(test_results, start_index, end_index, range_):
        """Helper method - analyzes test results of one range (short, mid, or long).
        
        Args:
            test_results: list of test results containing tuples of (euclidean_distance, time_dijkstra, time_idastar)
            start_index: start index of this range in test results list
            end_index: end index of this range in test results list
            range_: Short, Mid, or Long range
        
        Returns:
            String describing analysis of test results in this range
        """
        time_dij = 0
        time_ida = 0
        ida_not_finished = 0
        for i in range(start_index, end_index):
            result = test_results[i]
            time_dij += result[1]
            if result[2] == "no_time":
                ida_not_finished += 1
            else: # ida finished
                time_ida += result[2]
        result_dij = "Algorithm: Dijkstra - Average time: " + str(round(time_dij/(end_index-start_index)*1000, 3)) + " ms\n"
        result_ida = "Algorithm: IDA*     - Average time: " + str(round(time_ida/(end_index-start_index-ida_not_finished)*1000, 3)) + " ms   [" + str(ida_not_finished) + " attempts not finished]\n"
        header = range_ + "-range results [" + str(end_index-start_index) + " tests]:\n"
        return header + result_dij + result_ida
    
    
    print("\nCalculating...\n")
    
    test_results = []
    
    for _ in range(n):
        # random start and end cities
        start = cities[randint(0, len(cities)-1)]
        end = cities[randint(0, len(cities)-1)]
        while start == end:
            end = cities[randint(0, len(cities)-1)]
        # calculate euclidean distance
        x_diff = coordinates[start][0] - coordinates[end][0]
        y_diff = coordinates[start][1] - coordinates[end][1]
        eucl_dist = sqrt(x_diff**2 + y_diff**2)
        
        # Dijkstra
        dist_dij, path_dij, time_dij = dijkstra(start, end, adjlist)
        # IDA*
        dist_ida, path_ida, time_ida = idastar(start, end, adjlist, coordinates)
        
        test_results.append( (eucl_dist, time_dij, time_ida) )
    
    # Analysis of results
    test_results.sort()
    short_index = 0
    mid_index = n//3
    long_index = n//3*2
    
    # Short-range
    print(analyze_result(test_results, short_index, mid_index, "Short"))
    # Mid-range
    print(analyze_result(test_results, mid_index, long_index, "Mid"))
    # Long-range
    print(analyze_result(test_results, long_index, len(test_results), "Long"))


while True:
    n = input("\nHow many pathfinding problems you want to test? (quit with 'q') ")
    if n == "q":
        break
    try:
        n = int(n)
    except:
        print("Give amount of pathfinding problems to be tested as integer.")
    performance_test(n)


