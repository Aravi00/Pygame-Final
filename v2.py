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
rect = py.Rect(250,50,30,40)
touching = False
blockpos = py.Rect(0,350,random.randint(250,500),500-350)#left,top,width,height
blockpos2 = py.Rect(blockpos[0]+blockpos[2]+random.randint(300,500),350,random.randint(250,500),500-350)#x distance has to be >=300
blockpos3 = py.Rect(blockpos2[0]+blockpos2[2]+random.randint(300,500),350,random.randint(250,500),500-350)#x distance has to be >=300
blocks = [blockpos,blockpos2,blockpos3]
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    window.fill("white")
    
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
        for i in range(len(blocks)):
            blocks[i].left -=15
    if nightx < -size:
        nightx = size
    if nightx2 < -size:
        nightx2 = size
    
    yspeed+=0.25
    rect.top+=yspeed
    for i in range(len(blocks)):
        #if (reyt+40 > blocks[i].top and rext < blocks[i].left+blocks[i].width and rext > blocks[i].left):
        #if py.Rect.colliderect(rect,blocks[i]):
        if rect.top+40 >
            yspeed = 0
            reyt = blocks[i].top-40
            touching = True
        else:
            touching = False
     #x,y,w,h
    #draw here
    window.blit(nightsurface,(nightx,0))
    window.blit(nightsurface,(nightx2,0))
    window.blit(fsurface,(nightx*2-40,175))
    for i in range(len(blocks)):
        py.draw.rect(window,(255,0,0),blocks[i])
    py.draw.rect(window,(0,0,0),rect)
    py.display.flip()
    clock.tick(60)
py.quit()