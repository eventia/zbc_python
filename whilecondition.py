running = True

while running:
    number = int(input("숫자를 입력하세요 : "))

    if number == 777:
        print("종료합니다.")
        running = False

    if number%2 == 0:
        print("짝수입니다. ", end="")

    if number%3 == 0:
        print("3의 배수입니다. ", end="")

    print("")

print("종료")
