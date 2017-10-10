# if 조건문을 사용해서 사용자가 입력한 숫자가 짝수이면,
# "짝수입니다." 를 출력하고, 3의 배수이면,
# "3의 배수입니다." 를 출력하는 프로그램을
# 만들어 보세요. if 조건문  사용 / input() 함수 사용
# / print() 함수 사용 / 나머지 연산 % 사용
# / 대입연산자 = 사용 / 변수 사용

guess = int(input('숫자를 입력하세요 : '))

if guess%2==0:
    print(guess, '는 짝수입니다.')

if guess%3 == 0:
    print(guess, '는 3의 배수입니다')

print('프로그램 종료')





guess = int(input('숫자를 입력하세요 : '))

if ((guess%2)==0 or (guess%3)==0 ):
    print(guess, '는', end='')
    if guess%2 == 0:
        print(' 짝수입니다.', end='')

    if guess%3 == 0:
        print(' 3의 배수입니다', end='')

    print('')

else :
    print(guess, '는 짝수도 3의 배수도 아닙니다.')

print('프로그램 종료')
