import pgzrun
WIDTH=750
HEIGHT=640
TITLE="General knowledge contest"
scrollerbox=Rect(0,0,750,100)
q1=Rect(0,100,550,200)
a1=Rect(0,320,255,150)
a2=Rect(295,320,255,150)
a3=Rect(0,490,255,150)
a4=Rect(295,490,255,150)
qbox=Rect(570,100,170,200)
sbox=Rect(570,320,170,320)
l1=[]
currq=0
totq=0
tottime=10
msg=f"Welcome to quiz master! You are now on {currq}/{totq}"


def draw():
    global msg
    screen.fill("black")
    screen.draw.filled_rect(scrollerbox,"black")
    screen.draw.filled_rect(q1,"white")
    screen.draw.filled_rect(a1,"yellow")
    screen.draw.filled_rect(a2,"yellow")
    screen.draw.filled_rect(a3,"yellow")
    screen.draw.filled_rect(a4,"yellow")
    screen.draw.filled_rect(qbox,"orange")
    screen.draw.filled_rect(sbox,"green")
    screen.draw.textbox(msg,scrollerbox,color="white")
    screen.draw.textbox(str(tottime),qbox,color="black")
    screen.draw.textbox("Skip",sbox,color="black")



def update():
    scrollerbox.x-=3
    if scrollerbox.right<0:
        scrollerbox.x=WIDTH
def load():
    global l1,totq
    with open("questions.txt","r") as file:
        for i in file:
            l1.append(i)
            totq+=1

def question():
    global currq
    currq+=1
    return  l1.pop(0).split("|")



load()
q=question()
print(q)
pgzrun.go()    