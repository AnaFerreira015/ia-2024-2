import heapq
from utils import calculate_distance

def heuristic(city_a, city_b):
    """
    Heuristic function: estimates the cost from city_a to city_b using Euclidean distance.

    Parameters:
    - city_a (dict): Info about the current city (latitude, longitude)
    - city_b (dict): Info about the goal city (latitude, longitude)

    Returns:
    - float: estimated distance between cities
    """
    return calculate_distance(city_a, city_b)

def a_star_search(graph, city_info, start, goal):
    """
    Perform A* search to find the shortest path between two cities.

    Parameters:
    - graph (dict): Graph where keys are city names and values are lists of (neighbor, distance)
    - city_info (dict): Dictionary with detailed info of each city
    - start (str): Starting city name
    - goal (str): Destination city name

    Returns:
    - tuple: (path as list of city names, total distance as float)
    """
    start_info = city_info[start]
    goal_info = city_info[goal]

    frontier = [(heuristic(start_info, goal_info), 0, start, [start])]
    visited = set()

    while frontier:
        f_current, g_current, current_city, path = heapq.heappop(frontier)

        if current_city == goal:
            return path, g_current

        if current_city in visited:
            continue
        visited.add(current_city)

        for neighbor, cost in graph[current_city]:
            if neighbor in visited:
                continue

            new_g = g_current + cost
            new_f = new_g + heuristic(city_info[neighbor], goal_info)
            heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

if __name__ == "__main__":
    from utils import build_graph

    path = "cities.json"
    radius = 300

    graph, city_info = build_graph(path, radius)

    start = "Dallas"
    goal = "Austin"

    found_path, total_distance = a_star_search(graph, city_info, start, goal)

    if found_path:
        print("\nPath found (A*):")
        for city in found_path:
            print(" ->", city)
        print(f"\nTotal distance: {total_distance:.2f} km")
    else:
        print(f"\nNo path found between {start} and {goal} with r = {radius} km")