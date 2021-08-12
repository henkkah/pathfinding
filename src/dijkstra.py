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
    
    from min_heap import MinHeap
    
    inf = 10**9         # infinity
    
    # data structures
    distances = {}      # distances dictionary contains tuples of (distance, via), where 'distance' tells the min distance and 'via' tells via which vertex that min distance is achieved
    processed = {}      # processed dictionary contains info whether each vertex has been processed or not
    heap = MinHeap()    # min heap contains tuples of (distance, vertex)
    
    for vertex in adjlist.keys():
        distances[vertex] = (inf, None)
        processed[vertex] = False
    
    distances[start] = (0, start)
    heap.insert( (0, start) )
    
    # loop ended directly after reaching end city
    while not processed[end] and not heap.is_empty():
        next = heap.pop_min()
        startvertex = next[1]
        if not processed[startvertex]:
            processed[startvertex] = True
            for edge in adjlist[startvertex]:
                endvertex = edge[0]
                weight = edge[1]
                if distances[startvertex][0] + weight < distances[endvertex][0]:
                    distances[endvertex] = (distances[startvertex][0] + weight, startvertex)
                    heap.insert( (distances[endvertex][0], endvertex) )
    
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


