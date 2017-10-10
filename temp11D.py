number = 23
running = True
loopState = False
while running:
    guess = int(input('숫자를 입력하세요 : '))
    if guess == 777:
        print('종료합니다')
        break

    if guess == number:
        print ('맞았습니다.')
        running = False

    elif guess < number:
        print ('틀렸습니다. 조금 더 큰 수입니다.')

    else:
        print ('틀렸습니다. 조금 더 작은수입니다.')

else:
    print ('반복문이 정상적으로 종료되었습니다.')
    loopState = True

if loopState == True:
    print('프로그램 정상종료')
else :
    print ('프로그램이 강제종료되었습니다.')
