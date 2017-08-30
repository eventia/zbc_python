number = 23
guess = int(input("정수를 입력하세요 : "))

if guess == number:
    print("맞았습니다.")
elif guess < number:
    print("틀렸습니다. 조금 더 큰 수를 입력하세요.")
else :
    print("틀렸습니다. 조금 더 작은 수를 입력하세요.")

print("종료")
