import pgzrun
from random import randint
import time
TITLE="Alien game"
WIDTH=500
HEIGHT=500
img=Actor("alien")
img.pos=250,250
message=""
def draw():
    screen.clear()
    img.draw()
    screen.draw.text(message,(350,10),fontsize=30,color="white")

 


def update():
     img.x-=5
     if img.right<0:
         img.x=500


    
def on_mouse_down(pos):
    global message
    if img.collidepoint(pos):
        sounds.eep.play()
        message="Nice shot."
    else:
        message="You missed."
        


pgzrun.go()
