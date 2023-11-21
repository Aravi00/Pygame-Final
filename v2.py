import pygame as py
import random
#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
py.display.set_caption("Arav's Spiderman Game")
clock = py.time.Clock()

nightbg = py.image.load("nightbg.jpg")
nightbg2 = py.image.load("nightbg 3.jpg")
daybg = py.image.load("day bg.png")
foreground = py.image.load("foreground.png")
nightsurface = py.transform.scale_by(nightbg2,1)
fsurface = py.transform.scale_by(foreground,2)
size = 1191
nightx = 0
nightx2 = size
#loop
rext = 250
reyt =50
yspeed = 2
touching = False
randomw = random.randint(250,500)
blockpos = [0,350,randomw,500-350]
blockpos2 = [blockpos[0]+blockpos[2]+300,350,randomw,500-350]#x distance has to be >=300
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    if ev.type == py.MOUSEBUTTONUP:
        pressed = True
        x,y = py.mouse.get_pos()
        print(x,y)
    else:
        pressed = False
    if (key[py.K_SPACE] or key[py.K_w]) and touching == True:
        print("jump")
        yspeed = -7.5
    if key[py.K_d]:
        print("right")
        nightx -=2
        nightx2 -=2
        blockpos[0] -=15
        blockpos2[0] -=15
    window.fill("white")
    if nightx < -size:
        nightx = size
    if nightx2 < -size:
        nightx2 = size


    yspeed+=0.25
    reyt+=yspeed
    if (reyt+40 > blockpos[1] and rext < blockpos[0]+blockpos[2] and rext > blockpos[0]) or (reyt+40 > blockpos2[1] and rext < blockpos2[0]+blockpos2[2] and rext > blockpos2[0]):
        yspeed = 0
        reyt = blockpos2[1]-40#-blockpos[3]
        touching = True
    else:
        touching = False

    rect = [rext,reyt,30,40] #x,y,w,h
    #draw here
    window.blit(nightsurface,(nightx,0))
    window.blit(nightsurface,(nightx2,0))
    window.blit(fsurface,(nightx*2-40,170))
    py.draw.rect(window,(255,0,0),blockpos)
    py.draw.rect(window,(0,0,255),blockpos2)

    py.draw.rect(window,(0,0,0),rect)
    py.display.flip()
    clock.tick(60)
py.quit()