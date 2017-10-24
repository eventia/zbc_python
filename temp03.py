print('hello world')
# 시작하는 프로그램코드 hello world
# 코드가 어떻게라는 물음에 답한다면 주석은 왜라는 물음의 답이다.

import sys

t1 = sys.maxsize
t2 = t1+1  #파이썬 3.x 에서는 long, int 통합
t3 = t2**10  # 큰 수도 O.K.
print(t1)
print(t2)
print(t3)
print(type(t1))
print(type(t2))
print(type(t3))


age = 26
name = 'Python'

print('{0} was {1} years old'.format(name, age))
print('{0} is easy'.format(name))

print("{0:.3f}".format(1/3))
print("{0:_^10}".format("Hello"))
print("{name} wrote {book}".format(name="LIM", book="Zero Base Coding"))

print("{0:.10f}".format(1234567890123456789.141592))

a=1
b="LaLa"
c=1.01
print(a)
print("a의 타입은 "+str(type(a)))
print("a의 타입은 {}".format(type(a)))

print("7의 -2승은 {:0.9f}".format(7**-2))
print("7의 120승은 {:0.9g}".format(7**120))
