from dijkstra import dijkstra
from data_for_app import data_for_app
from random import randint
from time import sleep

cities, coordinates, speedlimits, adjlist = data_for_app()
waiting_time = 10

#while True:
start = cities[randint(0, len(cities)-1)]
end = cities[randint(0, len(cities)-1)]
while start == end:
    end = cities[randint(0, len(cities)-1)]

distances, processed, heap, distance, path = dijkstra(start, end, adjlist)

print("Start:", start)
print("End:", end)
print("Min distance:", distance)
print("Min path:", path)
print()
print(distances)
print(processed)
print(heap)
    
#sleep(waiting_time)




