import heapq
import math

def ucs(graph, start, goal):
    visited = set()
    heap = [(0, start, [])]
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == goal:
                return (cost, path)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path))
    return math.inf

# Example usage
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'C': 2, 'D': 3},
    'C': {'D': 4},
    'D': {'C': 1},
    'E': {'F': 2},
    'F': {'C': 3}
}
print(ucs(graph, 'A', 'D'))
# Output: (5, ['A', 'C', 'D'])
