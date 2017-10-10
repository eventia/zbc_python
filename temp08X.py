# 숫자 맞추기 게임을 만들어봅시다.
# input() 함수를 사용하면 키보드 입력을 받아올 수 있습니다.

number = 23
guess = int(input('숫자를 입력하세요 : '))
if guess == number:
    print('맞았습니다.')

elif guess < number:
    print('틀렸습니다. 조금 더 큰 수입니다.')

else:
    print('틀렸습니다. 조금 더 작은수입니다.')

print('프로그램 종료')
