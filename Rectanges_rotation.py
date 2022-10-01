import pygame,sys,math,time,random
from pygame.locals import *
pygame.init()
size = [900, 900]
screen = pygame.display.set_mode(size)
keep_going=True
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
PURPLE=(128,0,128)
LIME=(0,255,0)
GREY=(128,128,18)
TEAL=(0,128,128)
radius=50
timer=pygame.time.Clock()
screen.fill('violet')
N=100

clr=[GREEN,RED,BLUE,WHITE,BLACK,YELLOW,PURPLE,LIME,GREY,TEAL]

def rect_rotation(x1,y1,W,H,clr,angle):
    
    x2,y2=(x1+W),y1
    x3,y3=(x1+W),(y1+H)
    x4,y4=x1,(y1+H)
   
    x0=(x1+W/2)
    y0=(y1+H/2)
    #angle=45*i
    X1=x0+(x1-x0)*math.cos(math.radians(angle))-(y1-y0)*math.sin(math.radians(angle))
    Y1=y0+(x1-x0)*math.sin(math.radians(angle))+(y1-y0)*math.cos(math.radians(angle))
    X2=x0+(x2-x0)*math.cos(math.radians(angle))-(y2-y0)*math.sin(math.radians(angle))
    Y2=y0+(x2-x0)*math.sin(math.radians(angle))+(y2-y0)*math.cos(math.radians(angle))

    X3=x0+(x3-x0)*math.cos(math.radians(angle))-(y3-y0)*math.sin(math.radians(angle))
    Y3=y0+(x3-x0)*math.sin(math.radians(angle))+(y3-y0)*math.cos(math.radians(angle))
    X4=x0+(x4-x0)*math.cos(math.radians(angle))-(y4-y0)*math.sin(math.radians(angle))
    Y4=y0+(x4-x0)*math.sin(math.radians(angle))+(y4-y0)*math.cos(math.radians(angle))
    Point1,Point2,Point3,Point4=(X1,Y1),(X2,Y2),(X3,Y3),(X4,Y4)
    pygame.draw.polygon(screen, clr, (Point1,Point2,Point3,Point4))
        
A1,A2,angle1=[],[],[]
for m in range(N):
    A1.append(random.randint(100,800))
    A2.append(random.randint(100,800))
    angle1.append(random.randint(0,360))

keep_going=True
while keep_going: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('violet')
    
    
        
    for i in range(360):
        angle2=i
        for q in range(N):
            q1=q%10
            rect_rotation(A1[q],A2[q],50,80,clr[q1],angle1[q]+angle2)
        
        timer.tick(200)
        #time.sleep(1)
        pygame.display.update()
        #time.sleep(1)
    #timer.tick(5)
        screen.fill('violet')
    
        
    #pygame.display.update()
    
pygame.quit()


