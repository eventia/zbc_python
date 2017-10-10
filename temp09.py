running = True
while running:
    guess = int(input('숫자를 입력하세요 : '))
    if guess%2==0 and guess%3==0:
        print(guess, '는 짝수이면서, 3의 배수입니다.')

    else:
        if guess%2==0:
            print(guess, '는 짝수입니다.')

        if guess%3 == 0:
            print(guess, '는 3의 배수입니다')

        if guess == 777:
            running = False

print('프로그램 종료')
