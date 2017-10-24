# 두 정수를 입력받아 그 사이에 있는 소수 출력

import time

aNum = int(input("시작하는 수를 입력하세요 : "))
zNum = int(input("끝나는 수를 입력하세요 : "))

# Original Method
oldTime = time.time()

for anyNum in range(aNum,zNum+1):
    isPrime = 0
    for countNum in range(2,anyNum):
        if anyNum % countNum == 0:
            isPrime = isPrime + 1

    if isPrime == 0:
        print(anyNum)

print("Original Method Time Lap is ", time.time()-oldTime)
# End of Original Method


# Modified Method
oldTime = time.time()
for anyNum in range(aNum,zNum+1):
    isPrime = 0
    if anyNum == 2:
        print(anyNum)
        continue

    if anyNum % 2 == 0:
        isPrime = 1
        continue

    for countNum in range(3,anyNum//2,2):
        if anyNum % countNum == 0:
            isPrime = isPrime + 1
            break

    if isPrime == 0:
        print(anyNum)

print("Modified Method Time Lap is ", time.time()-oldTime)
# End of Modified Method
