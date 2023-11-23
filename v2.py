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

yspeed = 2
rect = py.Rect(250,150,30,40)
blockpos = py.Rect(0,random.randint(100,400),random.randint(250,500),200)#left,top,width,height
blockpos.height = windowheight-blockpos.top
blockpos2 = py.Rect(blockpos.right+random.randint(300,500),random.randint(100,400),random.randint(250,500),200)#x distance has to be >=300
blockpos2.height = windowheight-blockpos2.top
blocks = [blockpos,blockpos2]
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    
    window.fill("white")

    if key[py.K_d]:
        print("right")
        nightx -=2
        nightx2 -=2
        for i in range(len(blocks)):
            blocks[i].left -=15
            
    yspeed+=0.25
    rect.top+=yspeed
    
    for i in range(len(blocks)):
        if rect.bottom+1 > blocks[i].top and rect.left > blocks[i].left and rect.left < blocks[i].right:#if py.Rect.colliderect(rect,blocks[i]):
            yspeed = 0
            rect.top = blocks[i].top-40           
            if (key[py.K_SPACE] or key[py.K_w]):
                print("jump")
                yspeed = -7.5
            break
        #elif you touch the side of the building, what happens?
    if blocks[0].right < 0:
        blocks.append(py.Rect(blocks[-1].right+random.randint(300,500),random.randint(100,400),random.randint(250,500),200))
        blocks[-1].height = windowheight-blocks[-1].top
        blocks.pop(0)
    if nightx < -size:
        nightx = size
    if nightx2 < -size:
        nightx2 = size
    
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