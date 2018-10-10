
import os,re,random,math
import numpy as np
import pandas as pd
from scipy import optimize, special
import matplotlib.pyplot as plt
import pylab as pl
import matplotlib.mlab as mlab
import random
import copy


#xmin,ymin,xmax,ymax=input('please input the size of the simulation box:xmin,ymin,xmax,ymax \n').split()
#print("the size of the simution box is %d %d %d %d" %(int(xmin),int(ymin),int(xmax),int(ymax)))
xmin,ymin,xmax,ymax=0,0,800,800
#number_ball=input('please input the number of ball you want to display: \n')
number_ball=8
range_min=1;range_max=2000
time_step=0.1
display_step=0.025

X=[
    [
      []for i in range(0,int(number_ball))
    ]   for i in range(0,int(number_ball))
  ]

Y=[[[]for i in range(0,int(number_ball))]for i in range(0,int(number_ball))]

cordinate_ball=[]
cordinate_initial=[]
cordinate_all=[]

for i in range(0,int(number_ball)):

    x0=random.randint(xmin,xmax)
    y0=random.randint(ymin,ymax)
    vx0=random.random()*10
    vy0=random.random()*10
    cordinate_ball.append([x0,y0,vx0,vy0])
    cordinate_initial.append([x0,y0,vx0,vy0])

cordinate_all.append(cordinate_initial)

#in this case; we use a imaginary L-j potential to calculate the force between balls

def force(x):
    force=6*100**6/(x**7)-12*100**12/(x**13)
    return force
cut_off=100

#---------------------------------------------------------------------------------------------------------------------
#steps
for i in range(range_min,range_max):

#cal all the balls
    for j in range(0,int(number_ball)):
        xforce=0;yforce=0
        #cordinate_new=[]


        for k in range(0,int(number_ball)):

#self interaction            
            if j==k:
                X[j][k]=0;Y[j][k]=0
            else:
                X[j][k]=cordinate_all[i-1][k][0]-cordinate_all[i-1][j][0]
                Y[j][k]=cordinate_all[i-1][k][1]-cordinate_all[i-1][j][1]
                distance=(X[j][k]**2+Y[j][k]**2)**(1/2)
                totalforce=force(distance)
                
                xforce+=totalforce*(X[j][k]/distance);
                yforce+=totalforce*(Y[j][k]/distance)
                
        cordinate_ball[j][0]=cordinate_all[i-1][j][0]+time_step*cordinate_all[i-1][j][2]+1/2*xforce*time_step**2
        cordinate_ball[j][1]=cordinate_all[i-1][j][1]+time_step*cordinate_all[i-1][j][3]+1/2*yforce*time_step**2
        cordinate_ball[j][2]=cordinate_all[i-1][j][2]+time_step*xforce
        cordinate_ball[j][3]=cordinate_all[i-1][j][3]+time_step*yforce
        if cordinate_ball[j][0]>=xmax:
            cordinate_ball[j][0]=2*xmax-cordinate_ball[j][0]
            cordinate_ball[j][2]=-1*cordinate_ball[j][2]
        if cordinate_ball[j][0]<=xmin:
            cordinate_ball[j][0]=2*xmin-cordinate_ball[j][0]
            cordinate_ball[j][2]=-1*cordinate_ball[j][2]
        if cordinate_ball[j][1]>=ymax:
            cordinate_ball[j][1]=2*ymax-cordinate_ball[j][1]
            cordinate_ball[j][3]=-1*cordinate_ball[j][3]
        if cordinate_ball[j][1]<=ymin:
            cordinate_ball[j][1]=2*ymin-cordinate_ball[j][1]
            cordinate_ball[j][3]=-1*cordinate_ball[j][3]   
        
        #print(xforce,yforce)
    #cordinate_new=copy.deepcopy(cordinate_ball)
    cordinate_all.append(copy.deepcopy(cordinate_ball))

###the animation code is downloaded from website!               
import time
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    from tkMessageBox import *
    import tkFileDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *

image1 = "toy2.png"

root = Tk()
root.title("a simple molecular dynamic simulation display") #在这里修改窗口的标题
canvas = Canvas(width=800, height=800, bg='white')
canvas.pack()
photo1 = PhotoImage(file=image1)
width1 = photo1.width()
height1 = photo1.height()
image_x = (width1) / 2.0
image_y = (height1) / 2.0
# 每次的移动
for t in range(0, range_max):
    for i in range(0,int(number_ball)):
        canvas.create_image(cordinate_all[t][i][0], cordinate_all[t][i][1], image=photo1, tag="pic")
        canvas.update()
    # 暂停0.05妙，然后删除图像
    time.sleep(display_step)
    canvas.delete("pic")
root.mainloop()




            
                
    

