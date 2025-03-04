import pgzrun
from random import randint
from time import time
WIDTH=500
HEIGHT=500
totalsat=10
sat=[]
for i in range(10):
    img=Actor("satellite")
    img.pos=(randint(25,475),randint(25,475))
    sat.append(img)
start_time=time()
total_time=0
def draw():
    screen.blit("ospace",(0,0))
    if currentsat<totalsat:
        totaltime=time()-start_time
        screen.draw.text(str(round(totaltime)),(450,20),fontsize=30)

    num=1
    for i in sat:
        i.draw()
        screen.draw.text(str(num),(i.pos[0],i.pos[1]+20))
        num+=1
    for j in line:
        screen.draw.line(j[0],j[1],"white")
def update():
    pass
currentsat=0
line=[]
def on_mouse_down(pos):
    global currentsat,line,totalsat
    if currentsat<totalsat:
        if  sat[currentsat].collidepoint(pos):
            if currentsat:
              line.append((sat[currentsat-1].pos,sat[currentsat].pos))
            currentsat+=1
        else:
            line=[]
            currentsat=0



pgzrun.go()







