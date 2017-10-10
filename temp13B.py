x = 50
def func():
    global x
    print('x 의 값은', x)
    x = 2
    print('변경된 전역변수 x 는', x)

func()
print('변수 x 의 값은', x)
