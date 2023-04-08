import math
import heapq

def heuristic(node, goal, distances):

    return distances.get((node, goal), math.inf)

def astar(start, goal, graph):
    distances = {}
    for node1 in graph:
        for node2, cost in graph[node1].items():
            distances[(node1, node2)] = cost
            distances[(node2, node1)] = cost

    frontier = [(heuristic(start, goal, distances), start)]
    explored = set()
    came_from = {}
    g_score = {node: math.inf for node in graph}
    g_score[start] = 0
    f_score = {node: math.inf for node in graph}
    f_score[start] = heuristic(start, goal, distances)

    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            return reconstruct_path(came_from, start, goal)

        explored.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in explored:
                continue

            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal, distances)
                if neighbor not in (node for _, node in frontier):
                    heapq.heappush(frontier, (f_score[neighbor], neighbor))

    return None
def reconstruct_path(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    return list(reversed(path))
graph = {
    'A': {'B': 3, 'D': 2},
    'B': {'A': 3, 'C': 1, 'D': 5},
    'C': {'B': 1, 'D': 6},
    'D': {'A': 2, 'B': 5, 'C': 6, 'E': 4},
    'E': {'D': 4, 'F': 2},
    'F': {'E': 2, 'G': 3, 'H': 4},
    'G': {'F': 3, 'H': 1},
    'H': {'F': 4, 'G': 1}
}

start_node = 'A'
goal_node = 'H'
path = astar(start_node, goal_node, graph)
print(path)