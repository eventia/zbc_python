# 전체 완료
#
# 파이게임 참고 문서들 http://www.pygame.org/docs/
# python 3.6 and pygame 1.9.3
# 파이썬 기초 과정을 마치는 의미로 파이게임을 이용한 간단한 게임제작 프로젝트 진행
# 게임의 원 개발자는 Julian Meyer 로 북캘리포니아에 사는 13세 파이썬 프로그래머다.
# 원 소스와 매뉴얼은 다음 사이트에 있다.
# https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python
#
# python 3.6 으로 수정된 소스와 튜토리얼은 다음 사이트에 있다.
# http://winduino.co.kr/300
#

# 1 - 파이게임 모듈을 가져온다
import pygame
import math
import random

# 2 - 초기화 시킨다
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))  # 게임창을 만든다
keys = [False, False, False, False]
playerpos = [100,100]
acc = [0,0]
arrows = []
badtimer = 100
badtimer1 = 0
badguys = [[640,100],]
healthvalue = 194
pygame.mixer.init()

# 3.이미지를 가져온다
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

# 3.1 - 게임음향
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# 4 - 계속 화면이 보이도록 반복해서 실행한다
running = 1
exitcode = 0
while running:
    badtimer = badtimer-1

    # 5 - 화면을 깨끗하게 청소한다 (R,G,B) 값 사용
    screen.fill((0,0,0))

    # 6. - 모든 요소들을 다시 그린다
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345))

    # 6.1 - 플레이어 포지션과 회전
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width//2, playerpos[1]-playerrot.get_rect().height//2)
    screen.blit(playerrot, playerpos1)

    # 6.2 - 화살 그리기
    for bullet in arrows:
        index=0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1] = bullet[1]+velx
        bullet[2] = bullet[2]+vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(index)
        index = index+1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # 6.3 - 오소리 공격
    if badtimer == 0:
        badguys.append([640, random.randint(50,430)])
        badtimer = 100-(badtimer1*2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 = badtimer1+5
    index=0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        badguy[0] = badguy[0]-7

        # 6.3.1 - 성 공격
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            hit.play()
            healthvalue = healthvalue-random.randint(5,20)
            badguys.pop(index)

        #6.3.2 - 충돌 체크
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                enemy.play()
                acc[0] = acc[0]+1
                badguys.pop(index)
                arrows.pop(index1)
            index1 = index1+1

        # 6.3.3 - 다음 오소리
        index = index+1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    # 6.4 - 남은시간
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())//60000)+\
        ":"+str(((90000-pygame.time.get_ticks())//1000)%60).zfill(2), \
        True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright = [635,5]
    screen.blit(survivedtext, textRect)

    # 6.5 - 남은 생명을 표시
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))

    # 7. - 화면을 다시 그린다
    pygame.display.flip()

    # 8 - 게임을 종료할 준비, 종료아이콘(x)를 누르면 종료되도록 프로그램
    for event in pygame.event.get():
        # X 를 눌렀는지 검사
        if event.type==pygame.QUIT:
            # 게임종료
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
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
            acc[1] = acc[1]+1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32), \
                position[0]-(playerpos1[0]+26)),playerpos1[0]+32,\
                playerpos1[1]+32])

    # 9 - 플레이어 움직이기
    if keys[0]:
        playerpos[1] = playerpos[1] - 5
    elif keys[2]:
        playerpos[1] = playerpos[1] + 5
    if keys[1]:
        playerpos[0] = playerpos[0] - 5
    elif keys[3]:
        playerpos[0] = playerpos[0] + 5

    #10 - Win/Lose 검사
    if pygame.time.get_ticks() >= 90000:
        running = 0
        exitcode = 1
    if healthvalue <= 0:
        running = 0
        exitcode = 0
    if acc[1] != 0:
        accuracy = acc[0]*1.0/acc[1]*100
    else:
        accuracy = 0

# 11 - Win/lose 디스플레이
if exitcode == 0:    # 패배 (LOSE)
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+"{0:.2f}".format(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)

else:    # 게임승리 (WIN)
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+"{0:.2f}".format(accuracy)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
