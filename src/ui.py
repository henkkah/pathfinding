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
    from idastar import idastar
    from random import randint
    import matplotlib.pyplot as plt
    
    
    def get_commands():
        """Helper method - Gets available commands available for user in UI.
        
        Args:
            no arguments
        
        Returns:
            Available commands as string
        """
        return "Commands:\n    1 [Find shortest path between given cities]\n    2 [Find shortest path between random cities]\n    3 [See list of cities]\n    4 [Close application]\n"
    
    
    def shortest_path_output(start, end, distance, path, time_dij, time_ida, ida_terminated):
        """Helper method - Formats resulting shortest path.
        
        Args:
            start: starting city from where path starts
            end: ending city to which path ends
            distance: shortest distance between start and end cities (calculated in other methods)
            path: shortest path between start and end cities (calculated in other methods)
        
        Returns:
            Description of shortest path as string
        """
        hours = int(distance // 1)
        minutes = int(round(distance % 1 * 60, 0))
        citypath = " - ".join(path)
        if ida_terminated:
            time_usage_string = "-- Time usage --\nDijkstra: " + str(time_dij) + " ms\nIDA*:     " + str(time_ida) + " ms\n"
        else: # ida did not finish
            time_usage_string = "-- Time usage --\nDijkstra: " + str(time_dij) + " ms\nIDA*:     did not finish\n"
        return "\n" + time_usage_string + "\n----- Shortest path -----\nStart:    " + start + "\nEnd:      " + end + "\nDuration: " + str(hours) + " hours " + str(minutes) + " minutes\nPath:     " + citypath + "\n"
    
    
    def visualize_path(start, end, distance, path, time_dij, time_ida, ida_terminated):
        """Helper method - Visualizes found shortest path to a separate window.
        
        Args:
            start: starting city from where path starts
            end: ending city to which path ends
            distance: shortest distance between start and end cities (calculated in other methods)
            path: shortest path between start and end cities (calculated in other methods)
        
        Returns:
            no return value - returned from the method when user closes window which has popped up
        """
        ##min_x, max_x, min_y, max_y = 100, 0, 100, 0

        # visited cities and visualization
        xs, ys = [], []
        for city in path:
            x, y = coordinates[city][0], coordinates[city][1]
            xs.append(x)
            ys.append(y)
            plt.annotate(city, (x,y), textcoords="offset points", xytext=(0,5), ha="center")
            ##min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)
        plt.scatter(xs, ys, s=50, color="blue")
        plt.plot(xs, ys, color="blue")
        
        # neighboring cities
        xs, ys = [], []
        neighbors = []
        for city in path:
            for neighbor_tuple in adjlist[city]:
                neighbor = neighbor_tuple[0]
                if neighbor not in path:
                    x, y = coordinates[neighbor][0], coordinates[neighbor][1]
                    xs.append(x)
                    ys.append(y)
                    plt.annotate(neighbor, (x,y), textcoords="offset points", xytext=(0,5), ha="center")
                    neighbors.append(neighbor)
        # neighbors of neighbors and visualization
        for neighbor in neighbors:
            for neighbor_of_neighbor_tuple in adjlist[neighbor]:
                neighbor_of_neighbor = neighbor_of_neighbor_tuple[0]
                x, y = coordinates[neighbor_of_neighbor][0], coordinates[neighbor_of_neighbor][1]
                if neighbor_of_neighbor not in path and neighbor_of_neighbor not in neighbors:
                    xs.append(x)
                    ys.append(y)
                    plt.annotate(neighbor_of_neighbor, (x,y), textcoords="offset points", xytext=(0,5), ha="center")
                x2, y2 = coordinates[neighbor][0], coordinates[neighbor][1]
                plt.plot([x, x2], [y, y2], color="grey", linestyle="dashed")
        plt.scatter(xs, ys, s=5, color="grey")

        # duration
        hours = int(distance // 1)
        minutes = int(round(distance % 1 * 60, 0))
        duration_string = str(hours) + " hours " + str(minutes) + " minutes"
        
        if ida_terminated:
            plt.title("Shortest path: " + start + " -> " + end + "\n(" + duration_string + ")")
        else: # ida did not finish
            plt.title("Shortest path: " + start + " -> " + end + "\n(" + duration_string + ")")
        plt.show()
    
    
    
    print("---------- PATHFINDING APP ----------\n")
    
    # Endless loop to ask user for commands - takes also action based on given command
    while True:
        print(get_commands())
        command = input("Command: ")
        
        if command == "1": # Find shortest path between given cities
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
            
            print("\nCalculating shortest path: " + start + "-" + end + "...")
            
            # get shortest path
            distance_dij, path_dij, time_dij = dijkstra(start, end, adjlist)
            distance_ida, path_ida, time_ida = idastar(start, end, adjlist, coordinates)
            time_dij = round(time_dij*1000, 3) # time in milliseconds rounded to 3 decimals
            
            if path_ida == "no_path":
                print(shortest_path_output(start, end, distance_dij, path_dij, time_dij, time_ida, False))
                visualize_path(start, end, distance_dij, path_dij, time_dij, time_ida, False)
            else: # ida finished
                time_ida = round(time_ida*1000, 3) # time in milliseconds rounded to 3 decimals
                print(shortest_path_output(start, end, distance_dij, path_dij, time_dij, time_ida, True))
                visualize_path(start, end, distance_dij, path_dij, time_dij, time_ida, True)
        
        elif command == "2": # Find shortest path between random cities
            # random start and end cities
            start = cities[randint(0, len(cities)-1)]
            end = cities[randint(0, len(cities)-1)]
            while start == end:
                end = cities[randint(0, len(cities)-1)]
            
            print("\nCalculating shortest path: " + start + "-" + end + "...")
            
            # get shortest path
            distance_dij, path_dij, time_dij = dijkstra(start, end, adjlist)
            distance_ida, path_ida, time_ida = idastar(start, end, adjlist, coordinates)
            time_dij = round(time_dij*1000, 3) # time in milliseconds rounded to 3 decimals
            
            if path_ida == "no_path":
                print(shortest_path_output(start, end, distance_dij, path_dij, time_dij, time_ida, False))
                visualize_path(start, end, distance_dij, path_dij, time_dij, time_ida, False)
            else: # ida finished
                time_ida = round(time_ida*1000, 3) # time in milliseconds rounded to 3 decimals
                print(shortest_path_output(start, end, distance_dij, path_dij, time_dij, time_ida, True))
                visualize_path(start, end, distance_dij, path_dij, time_dij, time_ida, True)
        
        elif command == "3": # See list of cities
            print("\n- Cities -\n" + ", ".join(cities) + "\n")
        
        elif command == "4": # Close application
            exit()
        
        else:
            print("Command not valid")


