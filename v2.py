#Ref:https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame?rq=1

import pygame as py
import random
from pygame import mixer
#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
py.display.set_caption("Arav's Spiderman Game")
clock = py.time.Clock()

nightsurface = py.image.load("nightbg 3.jpg")
jump = py.mixer.Sound("jump2.wav")
jump.set_volume(1.0)
climb = py.mixer.music.load("climb.mp3")
#daybg = py.image.load("day bg.png")
#foreground = py.image.load("foreground.png")
milesm = py.image.load("milesrun.png")
milesj = py.image.load("miles4.png")
milesclimb = py.image.load("miles_morales.png")
font1 = py.font.SysFont("times new roman",50)
font2 = py.font.SysFont("times new roman",20)

#fsurface = py.transform.scale_by(foreground,2)
size = 1191
buildings = [py.image.load("building1.png"),py.image.load("building2.png"),py.image.load("building3.png"),py.image.load("building4.png")]
mybuild = [random.choice(buildings),random.choice(buildings)]

gamestate = 0
mytime = 0
distance = 0
time = 0
timelimit = 30
highscore = 0
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
    global nightx,nightx2,size,yspeed,rect,milesloc,milesnum,framecount,air,edge,blockpos,blockpos2,blocks,mytime,distance,time,timeover
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
    mytime = 0
    distance = 0
    time = 0
    timeover = False
reset()
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    if ev.type == py.MOUSEBUTTONDOWN:
        mousepos = py.mouse.get_pos()
        pressed = True
    else:
        pressed = False
    window.fill("white")
    if gamestate == 0:#start
        print("startscreen")
        text1 = font1.render("Miles Morales Jumper",1,(0,0,255))
        window.blit(text1, (25,25))
        start = py.draw.rect(window,(100,100,100),((windowwidth-110)/2,170, 110,50),0,10)
        text = font1.render("Start",1,(0,0,255))
        window.blit(text,(start.x+5,start.y-5))
        settings = py.draw.rect(window,(100,100,100),((windowwidth-165)/2,start.bottom +30, 165,50),0,10)
        text = font1.render("Settings",1,(0,0,255))
        window.blit(text,(settings.x,settings.y-5))
        howtoplay = py.draw.rect(window,(100,100,100),((windowwidth-270)/2,settings.bottom +30, 270,50),0,10)
        text = font1.render("How To Play",1,(0,0,255))
        window.blit(text,(howtoplay.x,howtoplay.y-5))
        if pressed:
            if start.collidepoint(mousepos):
                reset()
                gamestate = 1
            elif settings.collidepoint(mousepos):
                gamestate = 4
            elif howtoplay.collidepoint(mousepos):
                gamestate = 3
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
            if rect.bottom+1 > blocks[i].top  and rect.left > blocks[i].left and rect.left < blocks[i].right:#and rect.bottom+1 < blocks[i].top +20
                yspeed = 0
                air = False
                edge = False
                #print("top")
                rect.bottom = blocks[i].top           
                if (key[py.K_SPACE]):
                    yspeed = -5.5
                    jump.play()
                break
            elif rect.right > blocks[i].left and rect.right < blocks[i].right and rect.bottom > blocks[i].top+20:#and rect.right < blocks[i].left + 10
                #print("edge")
                yspeed = 0
                air = False
                edge = True
                if key[py.K_w]:
                    yspeed = -4.5
                    py.mixer.music.play(0,0.5)
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
        if mytime > timelimit:
            gamestate = 2
            timeover = True
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
        window.blit(font2.render("Time:",1,(0,0,255)),(10,10))
        window.blit(font2.render("Distance:",1,(0,0,255)),(10,30))
        window.blit(font2.render(str(timelimit-mytime),1,(0,0,255)),(100,10))
        window.blit(font2.render(str(int(distance))+ " m",1,(0,0,255)),(100,30))
    elif gamestate == 2:#end screen
        print("endscreen")
        text1 = font1.render("GAME OVER",1,(0,0,255))
        window.blit(text1, (100,25))
        speed = distance/mytime
        if speed >= highscore:
            highscore = speed
            window.blit(font2.render("New High Score!!",1,(0,0,255)),(100,180))
        if timeover:
            window.blit(font2.render("Time Over!",1,(0,0,255)),(100,100))
        else:
            window.blit(font2.render("You Died!",1,(0,0,255)),(100,100))
        window.blit(font2.render("Distance:",1,(0,0,255)),(100,130))
        window.blit(font2.render("Speed:",1,(0,0,255)),(300,130))
        window.blit(font2.render("High Score:",1,(0,0,255)),(100,150))
        window.blit(font2.render(str(int(distance)) + " m",1,(0,0,255)),(200,130))
        window.blit(font2.render(str(int(speed)) + " m/s",1,(0,0,255)),(400,130))
        window.blit(font2.render(str(int(highscore))+ " m/s",1,(0,0,255)),(200,150))
        end = py.draw.rect(window,(100,100,100),((windowwidth-125)/2,220, 125,50),0,10)
        window.blit(font1.render("Home",1,(0,0,255)),(end.x,end.y-5))
        end2 = py.draw.rect(window,(100,100,100),((windowwidth-225)/2,300, 225,50),0,10)
        window.blit(font1.render("Play Again",1,(0,0,255)),(end2.x,end2.y-5))
        if pressed:
            if end.collidepoint(mousepos):
                gamestate = 0
            elif end2.collidepoint(mousepos):
                reset()
                gamestate = 1
    elif gamestate == 3:
        print("how to play")
        f = open("HowToPlay.txt", "r")
            #print(f.read())
        htptext = font2.render(f.read(),1,(0,0,255))
        window.blit(htptext,(15,15))
        #ptext.draw(f, (10, 10))
        f.close()
        end = py.draw.rect(window,(100,100,100),((windowwidth-105)/2,370, 105,50),0,10)
        text = font1.render("Back",1,(0,0,255))
        window.blit(text,(end.x,end.y-5))
        if pressed:
            if end.collidepoint(mousepos):
                gamestate = 0
    elif gamestate == 4:
        print("Settings")
        window.blit(font1.render("Settings",1,(0,0,255)),(50,20))
        
        plus = py.draw.rect(window,(100,100,100),(400,100, 50,50),0,10)
        window.blit(font1.render("+",1,(0,0,255)),(plus.x+10,plus.y-3))
        
        minus = py.draw.rect(window,(100,100,100),(250,100, 50,50),0,10)
        window.blit(font1.render("-",1,(0,0,255)),(minus.x+17,minus.y-7))
        
        window.blit(font2.render("Time Limit:",1,(0,0,255)),(50,100))
        window.blit(font1.render(str(timelimit),1,(0,0,255)),(325,100))
        end = py.draw.rect(window,(100,100,100),(100,370, 105,50),0,10)
        window.blit(font1.render("Back",1,(0,0,255)),(end.x,end.y-5))
        if pressed:
            if end.collidepoint(mousepos):
                gamestate = 0
            elif plus.collidepoint(mousepos) and timelimit <99:
                print("+")
                timelimit+=1
            elif minus.collidepoint(mousepos) and timelimit >1:
                print("-")
                timelimit-=1
    py.display.flip()
    clock.tick(60)
py.quit()