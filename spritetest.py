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
milesloc = py.Rect(0*scale,0*scale,42*scale,40*scale)
milesnum = 0
milesframerate = 30
framecount = 0
#loop
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    if framecount % milesframerate ==0:
        if(milesnum<6):
            milesnum+=1
            milesloc.x += milesloc.width
        else:
            milesnum=0
            milesloc.x =0
    framecount+=1
    window.fill("white")
    #draw here 
    window.blit(milesm,(0,0),milesloc)
    py.display.flip()
    clock.tick(60)
py.quit()
