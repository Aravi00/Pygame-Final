import pygame as py
#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
clock = py.time.Clock()

nightbg = py.image.load("nightbg.jpg")
nightbg2 = py.image.load("nightbg 3.jpg")
daybg = py.image.load("day bg.png")
foreground = py.image.load("foreground.png")
nightsurface = py.transform.scale_by(nightbg2,windowheight/419)
fsurface = py.transform.scale_by(foreground,2)
nightx = 0
nightx2 = 1000*(windowheight/419)
#loop
rext = 250
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
#     if nightx + 1000*(windowheight/419) < 0 or nightx >0:
#         nightx = 1000*(windowheight/419)
#     if nightx2 < -1000*(windowheight/419) or nightx2 > 1000*(windowheight/419):
#         nightx2 = 1000*(windowheight/419)
    if nightx > -1000*(windowheight/419):
        print("movemnet check")
    else:
        x = 1000*(windowheight/419)
    if nightx2> -1000*(windowheight/419):
        print("movemnet check")
    else:
        nightx2 = 1000*(windowheight/419)

    yspeed+=0.25
    reyt+=yspeed
    if reyt >= 400:
        yspeed = 0
        reyt = 400
    if spacepressed and reyt >= 400:
        print("jump")
        yspeed = -7.5
    if dpressed:
        print("right")
        nightx -=5
        nightx2 -=5
    if apressed:
        print("left")
        nightx +=5
        nightx2 +=5
    if rext > windowwidth:
        rext = 0
    elif rext < 0:
        rext = windowwidth
    
    rect = [rext,reyt,30,40] #x,y,w,h
    #draw here
    window.blit(nightsurface,(nightx,0))
    window.blit(nightsurface,(nightx2,0))
    window.blit(fsurface,(nightx*2-40,170))
    py.draw.rect(window,(0,0,0),rect)
    py.display.flip()
    clock.tick(60)
py.quit()