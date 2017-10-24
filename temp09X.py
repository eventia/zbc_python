"""if 조건문을 사용해서 사용자가 입력한 숫자가
짝수이면, "짝수입니다." 를,
3의 배수이면, "3의 배수입니다." 를,
6의 배수이면 "짝수이면서 3의 배수입니다."를,
짝수도 3의배수도 아니면 "짝수도 3의 배수도 아닙니다."를
출력하는 프로그램을 만들어 보세요."""

running = True
while running:
    guess = int(input('숫자를 입력하세요 : '))
    if guess == 777:
        running = False

    if guess%6 == 0 :
        print(guess, "는 짝수이면서 3의 배수입니다.\n")

    elif guess%2 == 0:
        print(guess, "는 짝수입니다.\n")

    elif guess%3 == 0:
        print(guess, "는 3의 배수입니다.\n")

    else :
        print(guess, "는 짝수도 3의 배수도 아닙니다.\n")

print('프로그램 종료')
