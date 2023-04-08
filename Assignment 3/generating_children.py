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


