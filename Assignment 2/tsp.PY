import itertools
import sys

def tsp_brute_force(distances):
    # number of cities
    n = len(distances)
    
    # Generate all possible permutations of cities
    perms = itertools.permutations(range(n))
    
    # Initialize shortest distance to infinity
    shortest_dist = sys.maxsize
    
    # Iterate over all permutations and compute total distance
    for perm in perms:
        total_dist = 0
        for i in range(n - 1):
            total_dist += distances[perm[i]][perm[i+1]]
        total_dist += distances[perm[n-1]][perm[0]]
        # Update shortest distance if current permutation is shorter
        if total_dist < shortest_dist:
            shortest_dist = total_dist
            shortest_route = perm
    
    return shortest_dist, shortest_route


# Example usage
distances = [    [0, 5, 1, 3],
    [5, 0, 2, 4],
    [1, 2, 0, 6],
    [3, 4, 6, 0]
]

# Solve TSP using brute force
shortest_dist, shortest_route = tsp_brute_force(distances)

# Display output
print("Shortest distance:", shortest_dist)
print("Shortest route:", shortest_route)
