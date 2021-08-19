from data_for_app import data_for_app
from dijkstra import dijkstra
from idastar import idastar
from time import time


cities, coordinates, speedlimits, adjlist = data_for_app()

def performance_test_short():
    start = "Helsinki"
    end = "Tampere"
    
    # Dijkstra
    dijkstra_start = time()
    distD, pathD = dijkstra(start, end, adjlist)
    dijkstra_end = time()
    
    # IDA*
    idastar_start = time()
    distI, pathI = idastar(start, end, adjlist, coordinates)
    idastar_end = time()
    
    print("--Performance test short--")
    print("Dijkstra time usage: " + str(round((dijkstra_end-dijkstra_start)*1000,2)) + " milliseconds")
    print("IDA* time usage: " + str(round((idastar_end-idastar_start)*1000,2)) + " milliseconds")
    print()

def performance_test_middle():
    start = "Helsinki"
    end = "Joensuu"
    
    # Dijkstra
    dijkstra_start = time()
    distD, pathD = dijkstra(start, end, adjlist)
    dijkstra_end = time()
    
    # IDA*
    idastar_start = time()
    distI, pathI = idastar(start, end, adjlist, coordinates)
    idastar_end = time()
    
    print("--Performance test middle--")
    print("Dijkstra time usage: " + str(round((dijkstra_end-dijkstra_start)*1000,2)) + " milliseconds")
    print("IDA* time usage: " + str(round((idastar_end-idastar_start)*1000,2)) + " milliseconds")
    print()

def performance_test_long():
    start = "Helsinki"
    end = "Kilpisjärvi"
    
    # Dijkstra
    dijkstra_start = time()
    distD, pathD = dijkstra(start, end, adjlist)
    dijkstra_end = time()
    
    # IDA*
    idastar_start = time()
    distI, pathI = idastar(start, end, adjlist, coordinates)
    idastar_end = time()
    
    print("--Performance test long--")
    print("Dijkstra time usage: " + str(round((dijkstra_end-dijkstra_start)*1000,2)) + " milliseconds")
    print("IDA* time usage: " + str(round((idastar_end-idastar_start)*1000,2)) + " milliseconds")
    print()


performance_test_short()
performance_test_middle()
performance_test_long()


