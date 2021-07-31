def dijkstra(start, end, adjlist):
    """Finds shortest path from start vertex to end vertex using adjacency list given and Dijkstra's shortest path algorithm.
    
    Args:
        start: start vertex from where path starts
        end: end vertex to which path ends
        adjlist: adjacency list (dictionary technically) of all edges from the graph of the form:
            startvertex -> [(endvertex1,weight1), (endvertex2,weight2), etc...]
    
    Returns:
        tuple of (distance, path), where distance is the min distance between start and end cities and path is the min path forming this min distance
    """
    
    from heapq import heappush, heappop
    # heappush(heap,x)
    # heappop(heap)
    
    inf = 10**9     # infinity
    
    # data structures
    distances = {}  # distances dictionary contains tuples of (distance, via), where 'distance' tells the min distance and 'via' tells via which vertex that min distance is achieved
    processed = {}  # processed dictionary contains info whether each vertex has been processed or not
    heap = []       # min heap contains tuples of (distance, vertex)
    
    for vertex in adjlist.keys():
        distances[vertex] = (inf, None)
        processed[vertex] = False
    
    distances[start] = (0, start)
    heappush(heap, (0, start))
    
    # loop ended directly after reaching end city
    while not processed[end] and len(heap) > 0:
        next = heappop(heap)
        startvertex = next[1]
        if not processed[startvertex]:
            processed[startvertex] = True
            for edge in adjlist[startvertex]:
                endvertex = edge[0]
                weight = edge[1]
                if distances[startvertex][0] + weight < distances[endvertex][0]:
                    distances[endvertex] = (distances[startvertex][0] + weight, startvertex)
                    heappush(heap, (distances[endvertex][0], endvertex))
    
    # get path forming min distance
    distance = distances[end][0]
    path = [end]
    previous = distances[end][1]
    while previous != start:
        path.append(previous)
        previous = distances[previous][1]
    if previous == start:
        path.append(start)
    path.reverse()
    
    # return (distances, processed, heap, distance, path)   # return value for debugging purposes
    return (distance, path)


"""
##### Testing the algorithm #####
adjlist = {}
adjlist['A'] = [('B',9), ('F',2)]
adjlist['B'] = [('C',7)]
adjlist['C'] = [('E',1)]
adjlist['D'] = [('C',4)]
adjlist['E'] = [('B',2), ('D',3)]
adjlist['F'] = [('B',5), ('E',1)]

distances, processed, heap, distance, path = dijkstra('A', 'C', adjlist)
print("distances:", distances)
print("processed:", processed)
print("heap:", heap)
print()
print("distance:", distance)
print("path:", path)
#################################
"""

