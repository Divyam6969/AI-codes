from collections import deque
import copy

initial=[[1,2,3],[8,0,4],[7,6,5]]
goal=[[2,8,1],[0,4,3],[7,6,5]]

def find_blank(curr):
    for i in range(3):
        for j in range(3):
            if(curr[i][j]==0):
                return (i,j)
    #return (0,0)
            
def to_tup(L):
    tuples = []
    for x in L:
        tuples.append(tuple(x))
    return tuple(tuples)
def up(curr):
  up=copy.deepcopy(curr)
  row,col=find_blank(curr)
  if(row>0):
    up[row][col],up[row-1][col]=up[row-1][col],up[row][col];

  return up;

def down(curr):
  down=copy.deepcopy(curr)
  row,col=find_blank(curr)
  if(row<2):
    down[row][col],down[row+1][col]=down[row+1][col],down[row][col];
  return down

def left(curr):
  left=copy.deepcopy(curr);
  row,col=find_blank(curr)
  if(col>0):
    left[row][col],left[row][col-1]=left[row][col-1],left[row][col];
  return left

def right(curr):
  right=copy.deepcopy(curr);
  row,col=find_blank(curr)
  if(col<2):
    right[row][col],right[row][col+1]=right[row][col+1],right[row][col];
  return right


def puzzle_8(curr):
    visited=[]
    parent_dict={}

    q=deque()
    q.append(curr)
    parent_dict={to_tup(curr):'phi'}

    while (len(q)>0):
      curr=q.popleft()
      visited.append(curr)
      if(curr==goal):
        break;
      (row,col)=find_blank(curr);
      arr=[]

      arr.append(up(curr))
      arr.append(down(curr))
      arr.append(left(curr))
      arr.append(right(curr))



      for i in arr:
        if i not in visited and i not in q:
          q.append(i)
          parent_dict[to_tup(i)]=to_tup(curr)
      
    curr=to_tup(curr)
    path=[]
    while(curr in parent_dict):
      path.append(curr)
      curr=parent_dict[curr]
  
    print('path is: ')
    path.reverse()
    for i in path:
      print(i)

    
#main
puzzle_8(initial);