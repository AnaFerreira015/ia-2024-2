import heapq
from utils import calculate_distance
from euclidean_distance import heuristic

def greedy_best_first_search(graph, city_info, start, goal):
    """
    Perform Greedy Best-First Search to find a path between two cities.
    Uses only the heuristic to choose the next city to explore.

    Parameters:
    - graph (dict): Graph with city connections and distances
    - city_info (dict): City metadata including coordinates
    - start (str): Name of the starting city
    - goal (str): Name of the goal city

    Returns:
    - tuple: (path as list of city names, total distance as float)
    """
    start_info = city_info[start]
    goal_info = city_info[goal]

    frontier = [(heuristic(start_info, goal_info), start, [start])]
    visited = set()

    while frontier:
        h_current, current_city, path = heapq.heappop(frontier)

        if current_city == goal:
            total_distance = sum(
                calculate_distance(city_info[path[i]], city_info[path[i + 1]])
                for i in range(len(path) - 1)
            )
            return path, total_distance

        if current_city in visited:
            continue
        visited.add(current_city)

        for neighbor, _ in graph[current_city]:
            if neighbor not in visited:
                h_neighbor = heuristic(city_info[neighbor], goal_info)
                heapq.heappush(frontier, (h_neighbor, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found

if __name__ == "__main__":
    from utils import build_graph

    path = "cities.json"
    radius = 300

    graph, city_info = build_graph(path, radius)

    start = "Dallas"
    goal = "Austin"

    path_found, total_distance = greedy_best_first_search(graph, city_info, start, goal)

    if path_found:
        print("\nPath found (Greedy Best-First Search):")
        for city in path_found:
            print(" ->", city)
        print(f"\nTotal distance: {total_distance:.2f} km")
    else:
        print(f"\nNo path found between {start} and {goal} with r = {radius} km")