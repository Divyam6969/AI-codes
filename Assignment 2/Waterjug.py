def water_jug(max_x,max_y,aim):
  visited=[(0,0)]
  x,y=0,0
  while(True):
    if(x==aim and y==0):
      break

    if(x<max_x and (max_x,y) not in visited):                   #fill 1st from pump
      x=max_x
      visited.append((x,y))
    elif (y<max_y and (x,max_y) not in visited):                  #fill 2nd from pump
      y=max_y
      visited.append((x,y))
    elif (x>0 and (0,y) not in visited):                  #empty first
      x=0
      visited.append((x,y))
    elif (y>0 and (x,0) not in visited):                  #empty second
      y=0
      visited.append((x,y))
    elif (x+y>=max_x and (max_x,y-(max_x-x)) not in visited):                 #transfer from second to first to completely fill first
      y=y-(max_x-x)
      x=max_x
      visited.append((x,y))
    elif (x+y>=max_y and (x-(max_y-y),max_y) not in visited):                 #transfer from first to second to completely fill second
      x=x-(max_y-y)
      y=max_y
      visited.append((x,y))
    elif (x+y <= max_x and (x+y,0) not in visited):               #empty second jug into first
      x=x+y
      y=0
      visited.append((x,y))
    elif (x+y <=max_y and (0,x+y) not in visited):                #empty first into second
      y=x+y
      x=0
      visited.append((x,y))
    
  for i in visited:
    print(i)



max_x=int(input("enter capacity of first jug: "))
max_y=int(input('enter capacity of second jug: '))
aim=int(input('enter aim: '))

water_jug(max_x,max_y,aim)