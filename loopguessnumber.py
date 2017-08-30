number = 23
running = True

while running:
    guess = int(input("정수를 입력하세요 : "))

    if guess == number:
        print("맞았습니다.")
        running = False
    elif guess < number:
        print("틀렸습니다. 조금 더 큰 수를 입력하세요.")
    else :
        print("틀렸습니다. 조금 더 작은 수를 입력하세요.")

else :
    print("while 문이 정상적으로 종료되었습니다.")

print("종료")
