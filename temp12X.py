# 2개의 수를 주면 그 사이에 있는 소수를 출력하는 prn_prime() 함수를 만들라.

def prn_prime(startNumber=1, endNumber=10):
    isPrime = 0
    for anyNum in range(startNumber, endNumber+1):
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


prn_prime()
prn_prime(1_000_000, 1_000_100)
