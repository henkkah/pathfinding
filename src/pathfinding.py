from dijkstra import dijkstra
from data_for_app import data_for_app
from random import randint


def main():
    """Finds shortest path from random start city to random end city using base data for the app and Dijkstra's shortest path algorithm.
    
    Args:
        no arguments - uses base data for the app from csv files and draws start and end cities randomly
    
    Returns:
        prints shortest distance and shortest path calculated by Dijkstra's algorithm
    """
    
    cities, coordinates, speedlimits, adjlist = data_for_app()
    
    # random start and end cities
    start = cities[randint(0, len(cities)-1)]
    end = cities[randint(0, len(cities)-1)]
    while start == end:
        end = cities[randint(0, len(cities)-1)]
    
    distances, processed, heap, distance, path = dijkstra(start, end, adjlist)
    
    print("Start:", start)
    print("End:", end)
    print("Min distance:", distance, "hours")
    print("Min path:", path)
    
    # For validating working of the algorithm
    print()
    print("distances:", distances, "\n")
    print("processed:", processed, "\n")
    print("heap:", heap, "\n")


main()


