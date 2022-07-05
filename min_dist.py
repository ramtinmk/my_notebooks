import numpy as np
import matplotlib.pyplot as plt
def dist(first,second):
    return np.linalg.norm(first-second)
def is_in_red(red,x,y):
    for p in red:
        if x==p[0] and y==p[1]:
            return True
    return False
pointarr = [(0,0)]
x = 0 
y = 0
redx = np.random.randint(0,11,10)
redy = np.random.randint(0,11,10)
red = []
for i in range(len(redx)):
    while (redx[i] == 0 and redy[i]==0):
        redx[i] = np.random.randint(0,11)
        redy[i] = np.random.randint(0,11)
for i,j in zip(redx,redy):
    red.append((i,j))
dest = np.random.randint(0,11,2)
while is_in_red(red,dest[0],dest[1]) or (dest[0]==0 and dest[1]==0):
    dest = np.random.randint(0,11,2)
while (x!=dest[0] or y!=dest[1]) :
    min = 1000
    if dist(np.array([x+1,y]),dest)< min and is_in_red(red,x+1,y)==False:
        min = dist(np.array([x+1,y]),dest)
    if dist(np.array([x,y+1]),dest)< min and is_in_red(red,x,y+1)==False:
        min = dist(np.array([x,y+1]),dest)
    if dist(np.array([x+1,y+1]),dest)< min and is_in_red(red,x+1,y+1)==False:
        min = dist(np.array([x+1,y+1]),dest)
    if dist(np.array([x-1,y]),dest)< min and is_in_red(red,x-1,y)==False:
        min = dist(np.array([x-1,y]),dest)
    if dist(np.array([x,y-1]),dest)< min and is_in_red(red,x,y-1)==False:
        min = dist(np.array([x,y-1]),dest)
    if dist(np.array([x-1,y-1]),dest)< min and is_in_red(red,x-1,y-1)==False:
        min = dist(np.array([x-1,y-1]),dest)
    if dist(np.array([x+1,y-1]),dest)< min and is_in_red(red,x+1,y-1)==False:
        min = dist(np.array([x+1,y-1]),dest)
    if dist(np.array([x-1,y+1]),dest)< min and is_in_red(red,x-1,y+1)==False:
        min = dist(np.array([x-1,y+1]),dest)
    if min == dist(np.array([x+1,y+1]),dest):
        pointarr.append((x+1,y+1))
        x +=1
        y+=1
    elif min == dist(np.array([x+1,y]),dest):
        pointarr.append((x+1,y))
        x +=1
    elif min == dist(np.array([x,y+1]),dest):
        pointarr.append((x,y+1))
        y+=1
    elif min == dist(np.array([x-1,y]),dest):
        pointarr.append((x-1,y))
        x -=1
    elif min == dist(np.array([x,y-1]),dest):
        pointarr.append((x,y-1))
        y-=1
    elif min == dist(np.array([x-1,y-1]),dest):
        pointarr.append((x-1,y-1))
        x -=1
        y-=1
    elif min == dist(np.array([x-1,y+1]),dest):
        pointarr.append((x-1,y+1))
        y+=1
        x-=1
    elif min == dist(np.array([x+1,y-1]),dest):
        pointarr.append((x+1,y-1))
        y-=1
        x+=1
    if y ==dest[1] and (x-dest[0]==2):
        pointarr.append((x+1,y))
        x+=1
    if x ==dest[0] and (y-dest[1]==2):
        pointarr.append((x,y+1))
        y+=1
    if dist(np.array([x,y]),dest)<=(math.sqrt(2)):
        pointarr.append((x,y))
        break
pointarr[-1] = (dest[0],dest[1])   
x = [i[0] for i in pointarr]
y = [i[1] for i in pointarr]
greenx = np.linspace(0,10,11)
for i in range(11):
    plt.scatter(greenx,np.linspace(i,i,11),c='g',linewidths=7)
plt.scatter(redx,redy,c='r',linewidths=7)
plt.scatter(dest[0],dest[1],c='black',linewidths=7)
plt.scatter(0,0,c='b',linewidths=7)
plt.plot(x,y,c = 'black',linewidth=7)
print(dest)