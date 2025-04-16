import time
from utils import build_graph
from euclidean_distance import a_star_search
from GBFS import greedy_best_first_search

def compare_algorithms(start, goal, radius, json_path="cities.json"):
    """
    Compare A* and Greedy Best-First Search algorithms for routing between two cities.

    Parameters:
    - start (str): Name of the starting city
    - goal (str): Name of the destination city
    - radius (float): Maximum connection radius (in kilometers)
    - json_path (str): Path to the JSON file containing city data
    """
    print(f"\n[Comparing A* and Greedy from '{start}' to '{goal}' | r = {radius} km]")

    graph, city_info = build_graph(json_path, radius)

    print("\n>> A* Algorithm")
    t1 = time.time()
    path_astar, distance_astar = a_star_search(graph, city_info, start, goal)
    t2 = time.time()

    if path_astar:
        print("Path:", " -> ".join(path_astar))
        print(f"Distance: {distance_astar:.2f} km")
        print(f"Execution time: {t2 - t1:.4f} seconds")
    else:
        print("No path found.")

    print("\n>> Greedy Best-First Search")
    t3 = time.time()
    path_greedy, distance_greedy = greedy_best_first_search(graph, city_info, start, goal)
    t4 = time.time()

    if path_greedy:
        print("Path:", " -> ".join(path_greedy))
        print(f"Distance: {distance_greedy:.2f} km")
        print(f"Execution time: {t4 - t3:.4f} seconds")
    else:
        print("No path found.")

if __name__ == "__main__":
    json_file_path = "cities.json"
    default_radius = 300

    graph, city_info = build_graph(json_file_path, default_radius)

    print(f"\nNumber of connected cities: {len(graph)}\n")

    test_city = "Dallas"
    if test_city in graph:
        print(f"Connections from {test_city}:")
        for neighbor, distance in graph[test_city]:
            print(f" - {neighbor}: {distance:.2f} km")
    else:
        print(f"{test_city} has no connections within r = {default_radius} km")

    # Compare algorithms for three scenarios
    compare_algorithms("Dallas", "Austin", radius=300)
    compare_algorithms("New York", "Philadelphia", radius=500)
    compare_algorithms("New York", "Los Angeles", radius=200)
