#복소수 2+i , 1-2i 를 =, -, *, / 연산을 한 결과와 그 절대값을  표시하시오.
cNum1 = 2+1j
cNum2 = 1-2j

addNum = cNum1 + cNum2
minNum = cNum1 - cNum2
mulNum = cNum1 * cNum2
divNum = cNum1 / cNum2

print("{0} + {1} = {2}, abs({2}) = {3}".format(cNum1, cNum2, addNum, abs(addNum)))
print("{0} - {1} = {2}, abs({2}) = {3}".format(cNum1, cNum2, minNum, abs(minNum)))
print("{0} * {1} = {2}, abs({2}) = {3}".format(cNum1, cNum2, mulNum, abs(mulNum)))
print("{0} / {1} = {2}, abs({2}) = {3}".format(cNum1, cNum2, divNum, abs(divNum)))
