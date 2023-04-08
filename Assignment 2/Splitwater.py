def split_water(max_1,max_2,max_3,aim):

  visited=[]
  x,y,z=max_1,0,0
  visited.append((x,y,z))

  while(True):
    if(x==aim and y==aim):     #goal state
      break


    if(x+y>max_2 and (x-(max_2-y),max_2,z) not in visited):#fill 2nd from 1st
      x=x-(max_2-y)
      y=max_2
      visited.append((x,y,z))
    elif(x>0 and x+y<=max_2 and (0,x+y,z) not in visited): #empty 1st into 2nd
      y=x+y
      x=0
      visited.append((x,y,z))
    
    if(x==aim and y==aim):     #goal state
      break

    if (y+z>max_3 and (x,y-(max_3-z),max_3) not in visited):#fill 3rd from 2nd
      y=y-(max_3-z)
      z=max_3
      visited.append((x,y,z))
    
    elif(y>0 and y+z<=max_3 and (x,0,y+z) not in visited):#empty 2nd into 3rd
      z=z+y
      y=0
      visited.append((x,y,z))

    if(x==aim and y==aim):     #goal state
      break

    if (x+z>max_1 and (max_1,y,z-(max_1-x)) not in visited):#fill 1st from 3rd
      z=z-(max_1-x)
      x=max_1
      visited.append((x,y,z))

    elif(z>0 and x+z<=max_1 and (z+x,y,0) not in visited):#empty 3rd into 1st
      x=x+z
      z=0
      visited.append((x,y,z))



  for i in visited:
    print(i)


#main
split_water(12,8,5,6)
