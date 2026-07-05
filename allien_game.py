import pgzrun
WIDTH=500
HEIGHT=500
alien=Actor('alien.png')
def draw():
    screen.fill('blue')
    alien.draw()
pgzrun.go()