import pygame as py
import random
#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
py.display.set_caption("Arav's Spiderman Game")
clock = py.time.Clock()

miles = py.image.load("miles.png")
scale = 1.2
milesm = py.transform.scale_by(miles,scale)
milesloc = py.Rect(0*scale,0*scale,40*scale,40*scale)
milesnum = 0
milesframerate = 3

#loop
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    
    if(milesnum<6-1):
        milesnum+=1
        milesloc.x += milesloc.width+50
    else:
        milesnum=0
        milesloc.x =0
    
    window.fill("white")
    #draw here 
    window.blit(milesm,(0,0),milesloc)
    py.display.flip()
    clock.tick(1)
py.quit()
