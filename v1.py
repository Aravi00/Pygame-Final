import pygame as py
#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
clock = py.time.Clock()
#loop
rext = 50
reyt =50
yspeed = 2
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
    if key[py.K_SPACE] or key[py.K_w]:
        spacepressed = True
    else:
        spacepressed = False
    if key[py.K_d]:
        dpressed = True
    else:
        dpressed = False
    if key[py.K_a]:
        apressed = True
    else:
        apressed = False

    window.fill("white")
    yspeed+=1
    reyt+=yspeed
    if reyt >= 400:
        yspeed = 0
        reyt = 400
    if spacepressed and reyt >= 400:
        print("jump")
        yspeed = -20
    if dpressed:
        print("right")
        rext +=10
    if apressed:
        print("left")
        rext -=10
    if rext > windowwidth:
        rext = 0
    elif rext < 0:
        rext = windowwidth
    
    rect = [rext,reyt,30,40] #x,y,w,h
    #draw here
    py.draw.rect(window,(0,0,0),rect)
    py.display.flip()
    clock.tick(60)                                   
py.quit()