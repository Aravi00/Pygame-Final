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
miles = py.image.load("milesrun.png")
milesjump = py.image.load("miles4.png")

nightsurface = py.transform.scale_by(nightbg2,1)
fsurface = py.transform.scale_by(foreground,2)
size = 1191  
nightx = 0
nightx2 = size
#loop

yspeed = 2
rect = py.Rect(100,150,30,44)
blockpos = py.Rect(0,random.randint(300,400),random.randint(250,400),200)#left,top,width,height
blockpos.height = windowheight-blockpos.top
blockpos2 = py.Rect(blockpos.right+random.randint(100,300),random.randint(250,400),random.randint(250,500),200)#x distance has to be >=300
blockpos2.height = windowheight-blockpos2.top
blocks = [blockpos,blockpos2]

milesm = py.transform.scale_by(miles,1)
milesj = py.transform.scale_by(milesjump,1)

milesjloc = py.Rect(0,0,41,44)
milesloc = py.Rect(0,0,40,44)
milesnum = 0
framecount = 0
air = False
edge = False
def animate(img,framewidth,numframes,framerate):
    global framecount,milesnum
    #milesloc.top = ypos
    if framecount % framerate ==0:
        if(milesnum<numframes-1):
            milesnum+=1
            img.x += framewidth
        else:
            milesnum=0
            img.x =0
    framecount+=1
        
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    
    window.fill("white")

    if key[py.K_d] == True and edge == False:
        nightx -=1
        nightx2 -=1
        for i in range(len(blocks)):
            blocks[i].left -=10
        animate(milesloc,50,6,8)
    yspeed+=0.2
    rect.top+=yspeed
    for i in range(len(blocks)):
        if rect.bottom+1 > blocks[i].top and rect.bottom+1 < blocks[i].top +50 and rect.left > blocks[i].left and rect.left < blocks[i].right:#if py.Rect.colliderect(rect,blocks[i]):
            yspeed = 0
            air = False
            edge = False
            print("top")
            rect.top = blocks[i].top-rect.height           
            if (key[py.K_SPACE]):
                yspeed = -7.5
            break
        elif rect.right > blocks[i].left and rect.right < blocks[i].left + 50 and rect.top > blocks[i].top:#elif you touch the side of the building, what happens?
            # so its in the air and the edge at the same time when on the corner
            print("edge")
            yspeed = 0
            air = False
            edge = True
            if key[py.K_w]:
                #rect.top-=5
                yspeed = -7.5
            
        elif rect.bottom< blocks[i].top:
            air = True
            print("air")
            edge = False
            break
    
    if blocks[0].right < 0:
        blocks.append(py.Rect(blocks[-1].right+random.randint(50,400),random.randint(250,400),random.randint(250,500),200))
        blocks[-1].height = windowheight-blocks[-1].top
        blocks.pop(0)
        
    if nightx < -size:
        nightx = size
    if nightx2 < -size:
        nightx2 = size
    
    if key[py.K_SPACE] != True and key[py.K_d] != True:
        milesloc.y = 0
        milesloc.x = 0
        animate(milesloc,50,1,10)
     #x,y,w,h
    #draw here 
    window.blit(nightsurface,(nightx,0))
    window.blit(nightsurface,(nightx2,0))
    #window.blit(fsurface,(nightx*2-40,175))
    #window.blit(fsurface,(nightx*2-40+612*2-40,175))
    for i in range(len(blocks)):
        py.draw.rect(window,(255,0,0),blocks[i])
    #py.draw.rect(window,(0,0,0),rect)
    if air:
        window.blit(milesj,(rect.x,rect.y),milesjloc)
    else:
        window.blit(milesm,(rect.x,rect.y),milesloc)
    py.display.flip()
    clock.tick(60)
py.quit()