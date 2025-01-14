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
        
    screen.draw.circle((250,250),50,"white")
    screen.draw.filled_circle((410,175),50,"orange")
    screen.draw.line((250,250),(250,500),"white")
    screen.draw.text("Hello",(250,250),fontname="alger",fontsize=50,color="green",gcolor="cyan",owidth=1.5,ocolor="blue")
pgzrun.go()

                                                                                  