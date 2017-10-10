while True:
    name = input('영어 이름을 입력하세요. : ')
    if name == 'quit':
        break

    if len(name) < 3:
        print('너무 작습니다. 다시 입력해주세요.')
        continue

    print('이름을 입력하셨습니다.')
