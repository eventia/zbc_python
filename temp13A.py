x = 50
def func(x):
    print('x 의 값은', x)
    x = 2
    print('지역변수 x 의 값은', x)

func(x)
print('x 는 여전히 ', x)
