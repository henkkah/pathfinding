def data_for_app():
    import csv

    # data structures
    cities = []
    coordinates = {}
    speedlimits = {}
    adjlist = {}

    # read city data
    with open('data/cities.csv', 'r') as f:
        r = csv.reader(f)
        rows = [row for row in r]
        headers = rows[0]
        data = rows[1:]

    # process city data
    for row in data:
        cities.append(row[0])
        coordinates[row[0]] = (float(row[2]), float(row[1]))        # (east coordinate, north coordinate) as in x-y coordinate system
        adjlist[row[0]] = []

    # read speed limit data
    with open('data/speedlimits.csv', 'r') as f:
        r = csv.reader(f)
        rows = [row for row in r]
        headers = rows[0]
        data = rows[1:]

    # process speed limit data
    for row in data:
        speedlimits[row[0]] = row[1]

    # read highway data
    with open('data/highways.csv', 'r') as f:
        r = csv.reader(f)
        rows = [row for row in r]
        headers = rows[0]
        data = rows[1:]

    # process highway data
    for row in data:
        start = row[1]
        end = row[2]
        duration = int(row[3]) / int(speedlimits[row[4]])     # duration from start city to end city in hours
        adjlist[start].append((end, duration))
        adjlist[end].append((start, duration))
    
    return (cities, coordinates, speedlimits, adjlist)


"""
##### Test how above works #####
cities, coordinates, speedlimits, adjlist = data_for_app()
print("coordinates:", coordinates)
print()
print("speed limits:", speedlimits)
print()
cities = adjlist.keys()
for city in cities:
    print(city + ": " + str(adjlist[city]))
################################
"""

