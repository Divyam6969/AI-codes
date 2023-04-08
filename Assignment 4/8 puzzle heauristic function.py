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


#main
print(euclidean())
print(manhattan())
print(minkowski(1))
print(minkowski(2))
print(minkowski(3))