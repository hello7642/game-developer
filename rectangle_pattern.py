import pgzrun
import random
WIDTH=500
HEIGHT=500

def draw():
    screen.fill("black")
    w=200
    h=100
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    for i in range(20):
        place=Rect((100,100),(w,h))
        place.center=250,250
        screen.draw.rect(place,(r,g,b))
        w-=10
        h+=10
        

pgzrun.go()

                                                                                  