while True:
    name = input('영어 이름을 입력하세요. : ')
    if name == 'quit':
        break

    if len(name) < 3:
        print('3글자 이상으로 입력해주세요.')
        continue

    print('입력하신 이름은 {0}입니다. {0}님 반갑습니다.\n'.format(name))
