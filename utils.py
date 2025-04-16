import json
import math
from collections import defaultdict

def calculate_distance(city1, city2):
    """
    Calculates the approximate Euclidean distance (in kilometers) between two cities.

    Parameters:
    - city1 (dict): Dictionary containing 'latitude' and 'longitude' of the first city
    - city2 (dict): Dictionary containing 'latitude' and 'longitude' of the second city

    Returns:
    - float: Euclidean distance between the two cities
    """
    lat1, lon1 = city1['latitude'], city1['longitude']
    lat2, lon2 = city2['latitude'], city2['longitude']
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2) * 111  # Approximation in km

def build_graph(json_path, radius):
    """
    Builds a graph from the JSON city data, connecting cities within a given radius.

    Parameters:
    - json_path (str): Path to the JSON file containing city data
    - radius (float): Maximum distance to create a connection (in km)

    Returns:
    - tuple: (graph as adjacency list, dictionary with city data)
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        cities = json.load(f)

    for city in cities:
        city['latitude'] = float(city['latitude'])
        city['longitude'] = float(city['longitude'])
        city['population'] = int(city['population'])

    graph = defaultdict(list)
    city_map = {city['city']: city for city in cities}

    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            city1 = cities[i]
            city2 = cities[j]
            distance = calculate_distance(city1, city2)
            if distance <= radius:
                graph[city1['city']].append((city2['city'], distance))
                graph[city2['city']].append((city1['city'], distance))

    return graph, city_map