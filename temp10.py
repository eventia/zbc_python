# 구구단 프로그램
# 2단 : 2*1, 2*2, 2*3, .... 2*9
# 3단 : 3*1, 3*2, 3*3, .... 3*9
# ...
# 9단 : 9*1, 9*2, 9*3, .... 9*9

for firstNumber in range(2,10):
    for secondNumber in range(1,10):
        # print(firstNumber, '*', secondNumber, '=', firstNumber*secondNumber)
        print("{} * {} = {}".format(firstNumber,secondNumber,firstNumber*secondNumber))
        # print(str(firstNumber)+ ' * '+str(secondNumber)+' = '+str(firstNumber*secondNumber))
    print('')

print("구구단출력 완료")
