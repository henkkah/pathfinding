def ui(cities, coordinates, speedlimits, adjlist):
    """Finds shortest path from start city to end city using base data for the app and Dijkstra's shortest path algorithm.
    
    User can either input desired cities or app draws cities randomly.
    
    Args:
        cities: all available cities from base data for app (from csv file)
        coordinates: coordinates of all cities from base data for app (from csv file)
        speedlimits: speed limits currently in use in road types (from csv file)
        adjlist: adjacency list of roads and distances to neighboring cities calculated for each city, data from base data for app (from csv file)
    
    Returns:
        no return value - app closes when user decides to close it
    """
    
    from dijkstra import dijkstra
    from random import randint
    import matplotlib.pyplot as plt
    
    def get_commands():
        return "Commands:\n    1 [Find shortest path between given cities]\n    2 [Find shortest path between random cities]\n    3 [See list of cities]\n    4 [Close application]\n"
    
    def shortest_path_output(start, end, distance, path):
        hours = int(distance // 1)
        minutes = int(round(distance % 1 * 60, 0))
        citypath = " - ".join(path)
        return "\n----- Shortest path -----\nStart:    " + start + "\nEnd:      " + end + "\nDuration: " + str(hours) + " hours " + str(minutes) + " minutes\nPath:     " + citypath + "\n"
    
    def visualize_path(start, end, distance, path):
        min_x, max_x, min_y, max_y = 100, 0, 100, 0

        # neighboring cities not in path
        neighbors = []
        neighbors_from = []
        for city in path:
            for neighbor_tuple in adjlist[city]:
                neighbor = neighbor_tuple[0]
                if neighbor not in path:
                    neighbors.append(neighbor)
                    neighbors_from.append(city)
        # visualization
        xs, ys = [], []
        for i in range(len(neighbors)):
            city = neighbors[i]
            x, y = coordinates[city][0], coordinates[city][1]
            xs.append(x)
            ys.append(y)
            plt.annotate(city, (x,y), textcoords="offset points", xytext=(0,5), ha="center")
            min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)
            # original city in path from where neighbor stems from - road with dashed line
            city2 = neighbors_from[i]
            x2, y2 = coordinates[city2][0], coordinates[city2][1]
            plt.plot([x, x2], [y, y2], linestyle="dashed", color="cyan")
        plt.scatter(xs, ys, s=5, color="cyan")
        
        # visited cities and visualization
        xs, ys = [], []
        for city in path:
            x, y = coordinates[city][0], coordinates[city][1]
            xs.append(x)
            ys.append(y)
            plt.annotate(city, (x,y), textcoords="offset points", xytext=(0,5), ha="center")
            min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)
        plt.scatter(xs, ys, s=50, color="blue")
        plt.plot(xs, ys, color="blue")
        
        plt.title("Shortest path: " + start + " -> " + end)
        plt.show()
    
    print("---------- PATHFINDING APP ----------\n")
    
    while True:
        print(get_commands())
        command = input("Command: ")
        
        if command == "1":
            # get start and end cities
            print()
            start = ""
            while start not in cities:
                start = input("Give start city: ").title().replace('å','a').replace('ä','a').replace('ö','o').replace('Å','A').replace('Ä','A').replace('Ö','O')
                if start not in cities:
                    print("City not available")
            end = ""
            while end not in cities:
                end = input("Give end city: ").title().replace('å','a').replace('ä','a').replace('ö','o').replace('Å','A').replace('Ä','A').replace('Ö','O')
                if end not in cities:
                    print("City not available")
            
            # get shortest path
            distance, path = dijkstra(start, end, adjlist)
            
            print(shortest_path_output(start, end, distance, path))
            visualize_path(start, end, distance, path)
        
        elif command == "2":
            # random start and end cities
            start = cities[randint(0, len(cities)-1)]
            end = cities[randint(0, len(cities)-1)]
            while start == end:
                end = cities[randint(0, len(cities)-1)]
            
            # get shortest path
            distance, path = dijkstra(start, end, adjlist)
            
            print(shortest_path_output(start, end, distance, path))
            visualize_path(start, end, distance, path)
        
        elif command == "3":
            print("\n- Cities -\n" + ", ".join(cities) + "\n")
        
        elif command == "4":
            exit()
        
        else:
            print("Command not valid")


