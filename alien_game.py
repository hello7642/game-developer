import pgzrun
from random import randint
import time
TITLE="Alien game"
WIDTH=500
HEIGHT=500
img=Actor("pink_alien")
img.pos=250,250
msg=""
def draw():
    screen.clear()
    img.draw()
    screen.draw.text(msg,(400,450),fontsize=30,color="white")

def update():
     img.pos=(randint(0,500),randint(0,500))
     time.sleep(1)



    
def on_mouse_down(pos):
    global msg
    if img.collidepoint(pos):
        msg="Nice shot."
    else:
        msg="You missed."
        


pgzrun.go()
