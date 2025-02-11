import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE="Ufo game"
score=0
game_over=False
ufo=Actor("ufo")
ufo.pos=(100,100)
planet=Actor("planet")
planet.pos=(250,250)

def draw():
    screen.blit("space",(0,0))
    ufo.draw()
    planet.draw()
    screen.draw.text("score:"+str(score),color="black",topleft=(0,0))
    if game_over:
        screen.fill("white")
        screen.draw.text("Time is up!Your final score is:"+str(score),color="black",midtop=(250,250),fontsize=40)

def update():
    global score
    if keyboard.left:
        ufo.x-=5
    if keyboard.right:
        ufo.x+=5
    if keyboard.up:
        ufo.y-=5
    if keyboard.down:
        ufo.y+=5
    if ufo.colliderect(planet):
        score+=1
        planet.pos=randint(0,500),randint(0,500)

def over():
    global game_over
    game_over=True
clock.schedule(over,20)







pgzrun.go()


















