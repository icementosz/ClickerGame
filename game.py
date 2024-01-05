import pygame
import random
from pygame.locals import *
from csv import *

pygame.init()
pygame.font.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("HitFace Game")
fontscore=pygame.font.SysFont("Tahoma",30)
fonthighscore=pygame.font.SysFont("Tahoma",20)
fontgameover=pygame.font.SysFont("Tahoma",90)
bg=pygame.image.load("bg.png")
face=pygame.image.load("face.png")
facehurt=pygame.image.load("facehurt.png")
button1=pygame.image.load("buttonscore.png")
button2=pygame.image.load("buttonexit.png")
button3=pygame.image.load("buttonhigh.png")
buttonsave=pygame.transform.scale(button1,(400,400))
buttonexit=pygame.transform.scale(button2,(400,400))
buttonhighscore=pygame.transform.scale(button3,(400,400))
angel=pygame.image.load("angel1.png")
hitsound=pygame.mixer.Sound("hitsound.wav")
gameoversound=pygame.mixer.Sound("gameoversound.wav")
hitsound.set_volume(0.1)
gameoversound.set_volume(0.1)
score=0
highscore=0
gameover=False
face_rect = Rect(268, 167, face.get_width()-138, face.get_height()-34) #เก็บพิกัดของรูป
buttonsave_rect = Rect(106, 379, buttonsave.get_width(), buttonsave.get_height())
buttonexit_rect = Rect(455, 379, buttonexit.get_width(), buttonexit.get_height())
buttonhighscore_rect = Rect(0, 350, buttonhighscore.get_width(), buttonhighscore.get_height())

#Random Score Over
a=[]
for i in range(5):
    a.append(random.randrange(20,100))
for i in range(50):
    a.append(random.randrange(100,1000))
for i in range(100):
    a.append(random.randrange(1000,10000))
for i in range(1000):
    a.append(random.randrange(10000,50000))
print(a)

def clickplusscore():
    global score
    score=score+1

while True:
    if gameover==False:
        for event in pygame.event.get():
            text1 = fontscore.render("Score : "+str(score), True, (0, 255, 0))
            text2 = fonthighscore.render("HighScore : "+str(highscore), True, (196, 196, 191))

            if event.type==pygame.QUIT:
                quit()

            if score not in a:
                screen.blit(bg,(0,0))
                screen.blit(text1,(25,12))
                screen.blit(face,(200,150))
                screen.blit(text2,(550,12))
                screen.blit(buttonhighscore,(-35,365))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousebutton=event.button
                    if mousebutton == 1:
                        coordinates = pygame.mouse.get_pos()
                        print(coordinates)
                        if face_rect.collidepoint(coordinates): #เช็คตำแหน่งของเม้าส์ตรงกับรูปไหม
                            screen.blit(facehurt,(200,150))
                            hitsound.play()
                            clickplusscore()
                            screen.blit(text1,(25,12))
                            print(score)
                        if buttonhighscore_rect.collidepoint(coordinates):
                            try:
                                with open("filescore.csv","r",encoding="utf-8") as f:
                                    r=reader(f)
                                    l=list(r)
                                    highscore=int(l[0][0])
                                    screen.blit(text2,(550,12))
                                    print(highscore)
                            except IOError:
                                print("No file")
                            except IndexError:
                                print("IndexError Pls Check filescore.csv")
            
            #ถ้ามีรูปนางฟ้าขึ้น กดคลิกขวา
            else:
                screen.fill(0) #ล้างหน้าจอ
                screen.blit(bg,(0,0))
                screen.blit(angel,(240,152))
                screen.blit(text1,(25,12))
                screen.blit(text2,(550,12))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousebutton=event.button
                    if mousebutton == 3: #ถ้ากดเม้าส์ขวา
                        screen.fill(0) 
                        screen.blit(bg,(0,0))
                        coordinates = pygame.mouse.get_pos()
                        print(coordinates)
                        if face_rect.collidepoint(coordinates): #เช็คตำแหน่งของเม้าส์ตรงกับรูปไหม
                            hitsound.play()
                            clickplusscore()
                            screen.blit(text1,(25,12))
                            print(score)
                    elif mousebutton == 1:
                        gameover=True
    #หน้าจอ Game Over                   
    else:
        for event in pygame.event.get():
            screen.fill(0)
            textgameover = fontgameover.render("Game Over !", True, (255, 255, 255))
            screen.blit(textgameover,(150,200))
            screen.blit(text1,(25,12))
            screen.blit(text2,(550,12))
            screen.blit(buttonsave,(50,220))
            screen.blit(buttonexit,(350,220))
            gameoversound.play(500)
            if event.type == pygame.MOUSEBUTTONDOWN:
                coordinates = pygame.mouse.get_pos()
                print(coordinates)
                if buttonsave_rect.collidepoint(coordinates):
                        with open("filescore.csv","w",encoding="utf-8") as f:
                            w = writer(f)
                            if score >= highscore:
                                w.writerow([str(score)])
                                print("Save Score Success !")
                            else:
                                w.writerow([str(highscore)])
                                print("Your Score < HighScore !")
                if buttonexit_rect.collidepoint(coordinates):
                    quit()
        if event.type==pygame.QUIT:
                quit()
       
    pygame.display.update()