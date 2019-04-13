#1 라이브러리 임포트
import pygame
from pygame.locals import *
import math
import random
import sys
import time

#2 게임 설정
boolStart = 0
pygame.init()
width, height = 1280,720
screen = pygame.display.set_mode((width,height))
keys = [False, False, False, False]
Select = [False, False]
SelectClear = False
Select_Weapon = [False, False]
Restart_Select = True
stopwathStart = False
playerpos = [200,350]
acc = [0,0]
arrows = []
level = 0
pygame.mixer.init()

badtimer=100
badtimer1=0
badguys=[[1280,100]]
healthvalue=194
time = 0



#3 이미지 로드
player = pygame.image.load("images/player.png")
grass = pygame.image.load("images/grass.png")
computer_1 = pygame.image.load("images/computer_1.png") #게임프로토타입연구
computer_2 = pygame.image.load("images/computer_2.png") #게임엔진실습
computer_3 = pygame.image.load("images/computer_3.png") #인포메이션디자인
computer_4 = pygame.image.load("images/computer_4.png") #포토샵
mouse0 = pygame.image.load("images/mouse.png")
mouse1 = pygame.image.load("images/P_Weapon_1.png")
mouse2 = pygame.image.load("images/P_Weapon_2.png")
mouse3 = pygame.image.load("images/P_Weapon_3.png")
mouse4 = pygame.image.load("images/P_Weapon_4.png")
mouses = [mouse1, mouse2, mouse3, mouse4]
mouse5 = pygame.image.load("images/D_Weapon_1.png")
mouse6 = pygame.image.load("images/D_Weapon_2.png")
mouse7 = pygame.image.load("images/D_Weapon_3.png")
mouse8 = pygame.image.load("images/D_Weapon_4.png")
mouse9 = pygame.image.load("images/D_Weapon_5.png")
mouse10 = pygame.image.load("images/D_Weapon_6.png")

mouses_2 = [mouse5, mouse6, mouse7, mouse8, mouse9, mouse10]
mouse = mouse1

bg = pygame.image.load("images/bg.png")
bg_2 = pygame.image.load("images/bg_2.png")
bg_3 = pygame.image.load("images/bg_3.png")
bgs =[bg, bg_2, bg_3]
startimg = pygame.image.load("images/start.png")
eximg = pygame.image.load("images/ex.png")
selectimg = pygame.image.load("images/select.png")

badguyimg1 = pygame.image.load("images/PS.png") #포토샵 악당
badguyimg1_2 = pygame.image.load("images/PS_2.png") #포토샵 악당
badguyimg1_3 = pygame.image.load("images/PS_3.png") #포토샵 악당
badguyimg2 = pygame.image.load("images/AI.png") #일러스트 악당
badguyimg2_2 = pygame.image.load("images/AI_2.png") #일러스트 악당
badguyimg2_3 = pygame.image.load("images/AI_3.png") #일러스트 악당
badguyimg3 = pygame.image.load("images/Python.png") #파이썬 악당
badguyimg3_2 = pygame.image.load("images/Python_2.png") #파이썬 악당
badguyimg3_3 = pygame.image.load("images/Python_3.png") #파이썬 악당
badguyimg4 = pygame.image.load("images/VS.png") #비쥬얼스튜디오 악당
badguyimg4_2 = pygame.image.load("images/VS_2.png") #비쥬얼스튜디오 악당
badguyimg4_3 = pygame.image.load("images/VS_3.png") #비쥬얼스튜디오 악당
badguyimgs = [badguyimg3, badguyimg3_2 ,badguyimg3_3,badguyimg4,badguyimg4_2,badguyimg4_3] #개발자일경우 Enemy
badguyimgs_2 = [badguyimg1, badguyimg1_2, badguyimg1_3, badguyimg2, badguyimg2_2, badguyimg2_3]
badguyimg =  badguyimg2

#체력바 관련
healthbar = pygame.image.load("images/healthbar.png")
health = pygame.image.load("images/health.png")
healthUI  = pygame.image.load("images/healthUI.png")
healthbarBG = pygame.image.load("images/healthbar_bg.png")

#타이머 UI관련
TimerUI = pygame.image.load("images/timerUI.png")
TimerUI_BG = pygame.image.load("images/timerUI_BG.png")

#게임오버 / 게임윈 관련
gameover = pygame.image.load("images/gameover.png")
youwin = pygame.image.load("images/youwin.png")

#오디오관련
hit = pygame.mixer.Sound("audio/explode.wav")
enemy = pygame.mixer.Sound("audio/enemy.wav")
shoot = pygame.mixer.Sound("audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load("audio/BGM.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.10)

def terminate():
    pygame.quit()
    sys.exit()

def StartScreen():
    global SelectClear
    global Select_Weapon
    global stopwathStart

    if SelectClear == False:
        screen.blit(selectimg, (0, 0))
        pygame.display.update()

    while Select[0] == False:


        for event in pygame.event.get(): # X버튼을 누를 때
            if event.type == QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:

                if event.key == K_1 and SelectClear == False: #디자이너
                    global player
                    player = pygame.image.load("images/designer.png")
                    Select_Weapon[0] = True #디자이너 선택했을 경우를 알려주는 Bool
                    SelectClear = True
                    screen.blit(startimg, (0, 0))
                    pygame.display.update()
                    stopwathStart = True
                    stopwathStart += 10
                if event.key == K_2 and SelectClear ==  False: #개발자
                    player = pygame.image.load("images/player.png")
                    Select_Weapon[1] = True #개발자 선택했을 경우를 알려주는 Bool
                    SelectClear = True
                    screen.blit(startimg, (0, 0))
                    pygame.display.update()
                    stopwathStart = True
                    stopwathStart += 10
                if event.key == K_e and SelectClear == True: # e버튼을 누를 때
                    Select[0] = True
                    break
                if event.key == K_f and SelectClear == True: # f버튼을 누를 때
                    screen.blit(eximg, (0, 0))
                    pygame.display.update()
                    break

def restart():
    global Restart_Select
    global Select_Weapon
    global SelectClear
    global Select
    global running
    global exitcode
    global healthvalue
    global badtimer
    global badtimer1
    global badguys
    global time
    global level
    if Restart_Select == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    Select_Weapon = [False, False]
                    SelectClear = False
                    Select = [False, False]
                    stopwathStart = False
                    #running = 1
                    exitcode = 0
                    healthvalue = 194
                    Restart_Select = True
                    badtimer = 100
                    badtimer1 = 0
                    badguys = [[1280, 100]]
                    healthvalue = 194
                    time += 5

                    if exitcode == 4:
                        level += 5
                    break
                StartScreen()



running = 1
exitcode = 0

def stopwatch():
    global time
    stopwathStart = True
    if stopwathStart == True:
        stopwatch2 = int((90000 - pygame.time.get_ticks()) / 1000 % 60)
        stopwatch = time + stopwatch2
    return stopwatch

#4 게임 실행 루프

while running:




    StartScreen()

    #badguyimg = badguyimgs[random.randint(0,3)]
    badtimer -= 1
    #5
    screen.fill(0)
    #6
    bg = bgs[random.randint(0,2)]
    screen.blit(bg, (0, 0)) #배경화면
    screen.blit(computer_1,(10,30)) #게임프로토타입연구
    screen.blit(computer_2, (10, 200)) #게임엔진실습
    screen.blit(computer_3, (10,370)) #인포메이션디자인
    screen.blit(computer_4, (10,540)) #포토샵파일



    #6.Player rotation Code
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)

    # 6.3 - Draw badgers
    if badtimer == 0:

        badguys.append([1280, random.randint(50, 600)])
        badtimer = 100 - (badtimer1 * 2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5
    index = 0
    for badguy in badguys:
        if badguy[0] < -64 and exitcode != 3 and exitcode != 4:
            badguys.pop(index)
        badguy[0] -= 7+level

        # 6.3.1 - Attack castle
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            hit.play()
            healthvalue -= random.randint(30,40)
            #healthvalue -= random.randint(30, 50)
            badguys.pop(index)

        # 6.3.2 Check for Collisions
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(mouse.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                enemy.play()
                acc[0] += 1
                badguys.pop(index)
                arrows.pop(index1)
            index1+=1


        # 6.3.3 - Next bad guy
        index += 1
    for badguy in badguys:

        # 개발자일 경우에 Enemy 변경 해주는 코드
        if Select_Weapon[1] == True:
            badguyimg = badguyimgs[random.randint(0, 4)]

        # 디자이너일 경우에 Enemy 변경 해주는 코드
        if Select_Weapon[0] == True:
            badguyimg = badguyimgs_2[random.randint(0, 4)]

        screen.blit(badguyimg, badguy)


    #Mouse
    for bullet in arrows:

        # 개발자일 경우에 계속 웨폰 변경해주는 코드
        if Select_Weapon[1] == True:
            mouse = mouses[random.randint(0, 3)]

        # 디자이너일 경우에 계속 웨폰 변경해주는 코드
        if Select_Weapon[0] == True:
            mouse = mouses_2[random.randint(0, 5)]

        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 1280 or bullet[2] < -64 or bullet[2] > 720:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(mouse, 360 - projectile[0] * 57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # 6.4 Draw Clock

    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 36)
    # survivedtext = (pygame.time.get_ticks() - pygame.time.get_ticks()) / 1000
    screen.blit(TimerUI_BG, (955, 24))
    survivedtext = font.render(str(stopwatch()).zfill(2), True, (255, 255, 255))
    textRect = survivedtext.get_rect()
    textRect.topright = [1200,20]
    screen.blit(TimerUI, (970, 33))
    screen.blit(survivedtext, textRect)

    # 6.5 Draw Health Bar
    screen.blit(healthbarBG, (197,22))
    screen.blit(healthUI, (210,30))
    screen.blit(healthbar, (350,30))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+353,33)) #바에 +3 +3씩 하면 됨.

    #7
    if exitcode == 0:
        pygame.display.flip()

    #8
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position = pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append(
                [math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)), playerpos1[0] + 32,
                 playerpos1[1] + 32])

            # 9 - Move player
        if keys[0]:
                playerpos[1] -= 10
        elif keys[2]:
                playerpos[1] += 10
        if keys[1]:
                playerpos[0] -= 10
        elif keys[3]:
                playerpos[0] += 10

    # Win / Lose Check
    # if pygame.time.get_ticks() >= 90000:
    if int(stopwatch()) == 0:
        #running = 0
        exitcode = 4
    if healthvalue <= 0:
        #running = 0
        exitcode = 3

    if exitcode == 3:
        Restart_Select = False
        screen.blit(gameover, (0,0))
        pygame.display.update()
        restart()

    if exitcode == 4:
        Restart_Select = False
        screen.blit(youwin, (0, 0))
        pygame.display.update()
        restart()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    #pygame.display.flip()
