from math import *

initial=[[2,0,3],[1,8,4],[7,6,5]]
final=[[1,2,3],[8,0,4],[7,6,5]]

def find_place(L,x):
  for i in range(3):
    for j in range(3):
      if(L[i][j]==x):
        return i,j

def euclidean():
  eucl=0
  for i in range(1,9):
    x=find_place(initial,i)
    y=find_place(final,i)
    eucl+=((y[1]-x[1])**2+(y[0]-x[0])**2)**(1/2)
  
  return eucl


def manhattan():
  mh=0
  for i in range(1,9):
    x=find_place(initial,i)
    y=find_place(final,i)
    mh+=abs(y[1]-x[1])+abs(y[0]-x[0])
  
  return mh
  
def minkowski(p):
  mk=0
  for i in range(1,9):
    x=find_place(initial,i)
    y=find_place(final,i)
    mk+=((abs(y[1]-x[1]))**p+(abs(y[0]-x[0]))**p)**(1/p)
  return mk


#hill climbing
from queue import PriorityQueue
import copy

initial=[[2,0,3],[1,8,4],[7,6,5]]
final=[[1,2,3],[8,0,4],[7,6,5]]

def find_blank(L):
    for i in range(3):
      for j in range(3):
        if(L[i][j]==0):
          return i,j
def heuristic(curr): #no of misplaced tiles
  ans=0
  for i in range(3):
    for j in range(3):
      if(curr[i][j]!=final[i][j] and curr[i][j]!=0):
        ans+=1
  return ans


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


def steepest_hill_climb(curr):
  pq=[]
  visited=[curr]

  arr=[]

  arr.append(up(curr))
  arr.append(down(curr))
  arr.append(left(curr))
  arr.append(right(curr))

  prev=heuristic(curr)
  pq=[]
  for i in arr:
    if(i not in visited):
      pq.append((heuristic(i),i))
  
  while(len(pq)!=0):
    x=min(pq)
    pq.remove(x)
    if(x[1] in visited):
      continue

    visited.append(x[1])
    curr=x[1]
    if(x[1]==final or x[0] >= prev):
      break;


    pq.clear()

    arr=[]

    arr.append(up(curr))
    arr.append(down(curr))
    arr.append(left(curr))
    arr.append(right(curr))

    for i in arr:
      if(i not in visited):
        pq.append((heuristic(i),i))

  for i in visited:
    print(i,' hval =',heuristic(i))
  if(curr!=final):
    print('failed')

#main

steepest_hill_climb(initial)
