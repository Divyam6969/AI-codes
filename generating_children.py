import copy
import config

def generate_children(t):
    
    s = t[0]
    curr_depth = t[1]
    
    #global visited
    
    children = []
    for i in range(len(s)):
        temp = copy.deepcopy(s)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                    
                    if (temp1 not in config.visited) and (temp1 not in config.temp_q):
                        config.temp_q += [temp1]
                        children += [(temp1,curr_depth+1)]
                        
    return children


"""
This code defines a function called generate_children(t) that takes in an input parameter t and returns a list of tuples containing the children of the input node along with their depth in a search tree.

The function first extracts the state s and current depth curr_depth from the input node t. It then initializes an empty list called children that will store the children of the input node.

The function then loops through the elements in s and generates new states by moving an element from one list to another. This is done by making a copy of s using the copy.deepcopy() method, popping an element from the current list, and appending it to a different list. This creates a new state that is one move away from the input node.

The new state is then added to the temp_q list defined in the config module if it has not been visited before (i.e., not in the visited list) and not already in the temp_q list. The child node and its depth are then added to the children list.

The function returns the children list containing the newly generated child nodes and their depths. The copy module is imported at the beginning of the code, and the config module is imported to access its variables.
"""