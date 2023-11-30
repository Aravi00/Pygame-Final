import pygame as py
import random
#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
py.display.set_caption("Arav's Spiderman Game")
clock = py.time.Clock()

nightsurface = py.image.load("nightbg 3.jpg")
#daybg = py.image.load("day bg.png")
#foreground = py.image.load("foreground.png")
milesm = py.image.load("milesrun.png")
milesj = py.image.load("miles4.png")
milesclimb = py.image.load("miles_morales.png")
font1 = py.font.SysFont("times new roman",50)
#fsurface = py.transform.scale_by(foreground,2)
size = 1191
buildings = [py.image.load("building1.png"),py.image.load("building2.png"),py.image.load("building3.png"),py.image.load("building4.png")]
mybuild = [random.choice(buildings),random.choice(buildings)]

gamestate = 1
mytime = 0
distance = 0
time = 0
def animate(img,framewidth,numframes,framerate):
    global framecount,milesnum
    if framecount % framerate ==0:
        if(milesnum<numframes-1):
            milesnum+=1
            img.x += framewidth
        else:
            milesnum=0
            img.x =0
    framecount+=1
def build(rectangle,build):
    buildw,buildh = py.Surface.get_size(build)
    return py.transform.smoothscale(build,(buildw*(rectangle.width/buildw),buildh*(rectangle.height/buildh)))
def reset():
    global nightx,nightx2,size,yspeed,rect,milesloc,milesnum,framecount,air,edge,blockpos,blockpos2,blocks
    nightx = 0
    nightx2 = size
    yspeed = 2.0
    rect = py.Rect(100,150,30,44)
    milesloc = py.Rect(0,0,40,44)
    milesnum = 0
    framecount = 0
    air = False
    edge = False
    blocks = []
    blocks.clear()
    blockpos = py.Rect(0,random.randint(300,400),random.randint(250,400),200)#left,top,width,height
    blockpos.height = windowheight-blockpos.top
    blockpos2 = py.Rect(blockpos.right+random.randint(100,300),random.randint(250,400),random.randint(250,500),200)
    blockpos2.height = windowheight-blockpos2.top
    blocks = [blockpos,blockpos2]
reset()
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    window.fill("white")
    if gamestate == 0:#start
        print("startscreen")
        text1 = font1.render("Miles Morales Jumper",1,(0,0,255))
        window.blit(text1, (25,25))
        start = py.draw.rect(window,(100,100,100),((windowwidth-100)/2,170, 100,50),0,1)
        settings = py.draw.rect(window,(100,100,100),((windowwidth-100)/2,start.bottom +30, 100,50),0,1)
        howtoplay = py.draw.rect(window,(100,100,100),((windowwidth-100)/2,settings.bottom +30, 100,50),0,1)
    elif gamestate == 1: #play
        if key[py.K_d] == True and edge == False:
            nightx -=1
            nightx2 -=1
            for i in range(len(blocks)):
                blocks[i].left -=10
            animate(milesloc,50,6,8)
            distance +=0.5
        yspeed+=0.2
        rect.top+=yspeed
        
        for i in range(len(blocks)):
            if rect.bottom+1 > blocks[i].top and rect.bottom+1 < blocks[i].top +20 and rect.left > blocks[i].left and rect.left < blocks[i].right:
                yspeed = 0
                air = False
                edge = False
                #print("top")
                rect.bottom = blocks[i].top           
                if (key[py.K_SPACE]):
                    yspeed = -7.5
                break
            elif rect.right > blocks[i].left and rect.right < blocks[i].left + 10 and rect.bottom > blocks[i].top+20:
                #print("edge")
                yspeed = 0
                air = False
                edge = True
                if key[py.K_w]:
                    yspeed = -7.5
            elif rect.bottom< blocks[i].top:
                air = True
                #print("air")
                edge = False
                break
        
        if blocks[0].right < 0:
            blocks.append(py.Rect(blocks[-1].right+random.randint(50,400),random.randint(250,400),random.randint(250,500),200))
            blocks[-1].height = windowheight-blocks[-1].top
            mybuild.append(random.choice(buildings))
            mybuild.pop(0)
            blocks.pop(0)
            
        if nightx < -size:
            nightx = size
        if nightx2 < -size:
            nightx2 = size
        
        if key[py.K_SPACE] == False and key[py.K_d] == False:
            milesloc.y = 0
            milesloc.x = 0
            animate(milesloc,50,1,10)
        
        if rect.bottom > windowheight:
            gamestate = 2
        if mytime > 90:
            gamestate = 2
        elif time % 60 ==0:
            mytime +=1
            print(mytime,int(distance))
        time+=1
        #draw here 
        window.blit(nightsurface,(nightx,0))
        window.blit(nightsurface,(nightx2,0))
        #window.blit(fsurface,(nightx*2-40,175))
        #window.blit(fsurface,(nightx*2-40+612*2-40,175))
        for i in range(len(blocks)):
            block = build(blocks[i],mybuild[i])
            window.blit(block,blocks[i])
            py.draw.rect(window,(100,100,100),(blocks[i].left,blocks[i].top+20,10,blocks[i].height))
            py.draw.rect(window,(0,0,0),(blocks[i].left,blocks[i].top,blocks[i].width,20))
        if air:
            window.blit(milesj,(rect.x,rect.y))
        elif edge:
            window.blit(milesclimb,(rect.x,rect.y))
        else:
            window.blit(milesm,(rect.x,rect.y),milesloc)
    elif gamestate == 2:#end screen
        print("endscreen")
        reset()
        gamestate = 1
    py.display.flip()
    clock.tick(60)
py.quit()