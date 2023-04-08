def create_graph():
  # graph=[]
  # n=int(input('enter no of vertices: '))
  # for i in range(n+1):
  #   graph.append([])
  # choice='y'
  # while(choice=='y'):
  #   x,y,w = [int(x) for x in input("Enter edge and weight: ").split()]
  #   graph[x].append([y,w])
  #   graph[y].append([x,w])

  #   choice=input('more edges? (y/n)')


  graph=[]
  for i in range(5):
    graph.append([])

  graph[1].append([2,10])
  graph[2].append([1,10])
  graph[1].append([3,15])
  graph[3].append([1,15])
  graph[1].append([4,20])
  graph[4].append([1,20])

  graph[2].append([3,35])
  graph[3].append([2,35])
  graph[2].append([4,25])
  graph[4].append([2,25])
  graph[3].append([4,30])
  graph[4].append([3,30])

  
  return graph


all_paths=[]
def get_all_paths(graph,s,path,visited,weight,count):

  if(count==4):
    all_paths.append((path,weight))
    return
  
  for i in graph[s]:
    if i[0] not in visited:
      get_all_paths(graph,i[0],path+[i[0]],visited+[i[0]],weight+i[1],count+1)

def tsp(graph,s,n):
  
  cost=10**5
  opt=[]
  get_all_paths(graph,s,[],[],0,0)
  
  for i in all_paths:
    path=i[0]
    if(path[-1]==s and i[1]<cost):
      opt=i[0]
      cost=i[1]

  print('path is: ',s,end='')
  for i in opt:
    print('->',i,end='')
  print('\ncost is: ',cost)

#main
graph=create_graph()
x=int(input('enter start node: '));
tsp(graph,x,4)