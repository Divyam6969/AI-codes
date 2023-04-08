import sys
import copy
from generating_children import *
import config
        


def search(initial_state,final_state):
    
    if (initial_state[0] in final_state):
        print(final_state)
        print("solution found at the depth:-",initial_state[1])
        print("total number of states visited:-",len(config.visited))
        return
    
    curr_state = copy.deepcopy(initial_state)
    
    while(1):
        
        children = generate_children(curr_state)
        print(curr_state)
        print("------------")
        
        if (curr_state[0] == final_state):
            print(final_state)
            print("solution found at the depth:-",curr_state[1])
            print("total number of states visited:-",len(config.visited))
            return
        else:
            config.q += children
                
        if len(config.q) == 0:
            print("solution does not exists")
            print("current depth is",curr_state[1])
            print("total number of states visited:-",len(config.visited))
            return
        else:
            curr_state = config.q[len(config.q)-1]
            config.visited = config.visited + [curr_state]
            del config.q[len(config.q)-1]
            

def main():
    num_of_blocks = 3
    state = [[]]*num_of_blocks
    initial_state = [['A'],['B','C'],[]]
    final_state = [['A','B','C'],[],[]]
    config.visited = config.visited + [initial_state]
    search((initial_state,0),final_state)

if __name__ == "__main__":
    
    main()