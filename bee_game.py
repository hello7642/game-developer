import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE="Bee game"
score=0
game_over=False
bee=Actor("bee")
bee.pos=(100,100)
flower=Actor("flower")
flower.pos=(250,250)

def draw():
    screen.blit("field",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+str(score),color="black",topleft=(0,0))
    if game_over:
        screen.fill("white")
        screen.draw.text("Time is up!Your final score is:"+str(score),color="black",midtop=(250,250),fontsize=40)

def update():
    global score
    if keyboard.left:
        bee.x-=5
    if keyboard.right:
        bee.x+=5
    if keyboard.up:
        bee.y-=5
    if keyboard.down:
        bee.y+=5
    if bee.colliderect(flower):
        score+=1
        flower.pos=randint(0,500),randint(0,500)

def over():
    global game_over
    game_over=True
clock.schedule(over,20)







pgzrun.go()





