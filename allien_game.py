import random
import pgzrun
WIDTH=500
HEIGHT=500
msg=''
death='YOU DIED!!!'
more=0
alien=Actor('alien.png')
def draw():
    screen.fill('blue')
    alien.draw()
    screen.draw.text(msg,(300,300))
    screen.draw.text(death,(70,250),fontsize=100,color='red')
def update():
    if keyboard.left:
            alien.x-=10
    if keyboard.right:
        alien.x+=10
    if keyboard.up:
        alien.y-=10
    if keyboard.down:
        alien.y+=10
    if alien.x>500:
         alien.x=300
         alien.y=300
    if alien.y>500:
         alien.x=300
         alien.y=300
    if alien.x<0:
         alien.x=300
         alien.y=300
    if alien.y<0:
         alien.x=300
         alien.y=300
def alien_clicker():
    alien.x=random.randint(0,500)
    alien.y=random.randint(0,500)
def on_mouse_down(pos):
    global msg
    global death
    if alien.collidepoint(pos):
        alien_clicker()
        if more==0:
            msg="DON'T TOUCH ME"
            more+=1
        if more==1:
            msg="I TOLD DON'T TOUCH ME"
            more+=1
        if more==2:
            msg="I TOLD DON'T TOUCH ME"
            more+=1
        if more==3:
            msg="STOP I'LL KILL YOU!!!!!!"
            more+=1
        if more==4:
            msg="ONE MORE TIME AND YOU'RE DEAD!!!"
            more+=1
        if more==5:
            death='You Died!!!'
    else:
         msg="Imagine trying to touch me and failing misrebly"
pgzrun.go()