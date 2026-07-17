import random
import pgzrun

WIDTH=500
HEIGHT=500

TITLE='Beegame'

score=0
game_over=False

bee=Actor('bee.png')
bee.pos=100,100

flower=Actor('flower.png')
flower.pos=200,200

def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score: "+str(score),color="black",topleft=(10,10))
    if game_over:
        screen.fill('red')
        screen.draw.text("GAMEOVER, your final score is "+str(score),color="black",midtop=(WIDTH/2,220),fontsize=40)

def moveflower():
    flower.x=random.randint(0,500)
    flower.y=random.randint(0,500)

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2
    if bee.x>500:
         bee.x=300
         bee.y=300
    if bee.y>500:
         bee.x=300
         bee.y=300
    if bee.x<0:
         bee.x=300
         bee.y=300
    if bee.y<0:
         bee.x=300
         bee.y=300
    if bee.colliderect(flower):
        score=score+10
        moveflower()
moveflower()
pgzrun.go()