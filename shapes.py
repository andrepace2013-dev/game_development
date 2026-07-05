import pgzrun
WIDTH=500
HEIGHT=500
def draw():
    screen.fill('blue')
    rec=Rect((125,150),(250,200))
    screen.draw.filled_rect(rec,'white')
    screen.draw.filled_circle((250,250),50,'red')
    screen.draw.text('Japan',(178,355),color='white',fontsize=75)
pgzrun.go()