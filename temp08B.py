# 숫자 맞추기 게임
# PC 저장된 수, number 변수에 23 저장
# 사용자가 숫자를 입력(input), guess 변수 저장
# guess 수와 number 비교
# guess 가 number 보다 크면(조건) ,
#          "틀렸습니다. 조금 더 작은수입니다."
# guess 가 number 보다 작으면(조건) ,
#          "틀렸습니다. 조금 더 큰수입니다."
# guess 와 number 가 같으면(조건),
#          "맞았습니다."
# "프로그램 종료" 출력해주고 끝.
number = 23
guess = int(input("숫자를 입력하세요: "))
if guess > number :
    print("틀렸습니다. 조금 더 작은수입니다.")

if guess < number :
    print("틀렸습니다. 조금 더 큰수입니다.")

if guess == number:
    print("맞았습니다.")

print("프로그램 종료")
