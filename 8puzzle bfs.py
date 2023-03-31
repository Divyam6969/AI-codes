from queue import Queue

# Define the initial and goal states
INITIAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]

# Define the BFS search function
def bfs_search(initial_state, goal_state):
    # Create a queue to store the states to be explored
    state_queue = Queue()
    state_queue.put((initial_state, 0, []))
    # Create a set to keep track of the explored states
    explored_states = set()

    # Perform BFS search
    while not state_queue.empty():
        current_state, current_depth, path = state_queue.get()
        # Check if the current state is the goal state
        if current_state == goal_state:
            # Print out the solution path
            for matrix in path + [current_state]:
                print(matrix)
                print()
            return current_depth
        # Generate all possible states from the current state
        for i in range(3):
            for j in range(3):
                if current_state[i][j] == 0:
                    # Try moving the blank tile to the left
                    if j > 0:
                        new_state = [row[:] for row in current_state]
                        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
                        if tuple(map(tuple, new_state)) not in explored_states:
                            state_queue.put((new_state, current_depth+1, path+[current_state]))
                            explored_states.add(tuple(map(tuple, new_state)))
                    # Try moving the blank tile to the right
                    if j < 2:
                        new_state = [row[:] for row in current_state]
                        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
                        if tuple(map(tuple, new_state)) not in explored_states:
                            state_queue.put((new_state, current_depth+1, path+[current_state]))
                            explored_states.add(tuple(map(tuple, new_state)))
                    # Try moving the blank tile up
                    if i > 0:
                        new_state = [row[:] for row in current_state]
                        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
                        if tuple(map(tuple, new_state)) not in explored_states:
                            state_queue.put((new_state, current_depth+1, path+[current_state]))
                            explored_states.add(tuple(map(tuple, new_state)))
                    # Try moving the blank tile down
                    if i < 2:
                        new_state = [row[:] for row in current_state]
                        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
                        if tuple(map(tuple, new_state)) not in explored_states:
                            state_queue.put((new_state, current_depth+1, path+[current_state]))
                            explored_states.add(tuple(map(tuple, new_state)))
    # If the goal state cannot be reached, return None
    return None

# Call the BFS search function with the initial and goal states
steps_to_goal = bfs_search(INITIAL_STATE, GOAL_STATE)
print("Steps to goal:", steps_to_goal)
