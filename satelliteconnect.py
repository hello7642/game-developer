import pgzrun
from random import randint
from time import time
WIDTH=500
HEIGHT=500
totalsat=10
game_over=False
game_win=False
score=0
sat=[]
for i in range(10):
    img=Actor("satellite")
    img.pos=(randint(25,475),randint(25,475))
    sat.append(img)
start_time=time()
total_time=0
def draw():
    global totaltime
    screen.blit("ospace",(0,0))
    if currentsat<totalsat:
        totaltime=time()-start_time
        screen.draw.text(str(round(totaltime)),(450,20),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime)),(450,20),fontsize=30)
    if game_over:
        screen.fill("white")
        screen.draw.text("Time is up!Your final score is:"+str(score),color="black",midtop=(250,250),fontsize=40)
    if game_win:
        screen.draw.text("You have won the game!",color="white",midtop=(250,250),fontsize=40)
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
def over():
    global game_win
    global game_over
    if len(line)==9:
        game_win=True
    else:
         game_over=True

clock.schedule(over,20)

def on_mouse_down(pos):
    global score
    global currentsat,line,totalsat
    if currentsat<totalsat:
        if  sat[currentsat].collidepoint(pos):
            if currentsat:
              line.append((sat[currentsat-1].pos,sat[currentsat].pos))
            currentsat+=1
            score+=1
        else:
            line=[]
            currentsat=0
            score=0



pgzrun.go()







