if __name__ == '__main__':
    print('This program is being run by itself. My name is ', end='')
    print(__name__)
else:
    print('I am being imported from another module. My name is ', end='')
    print(__name__)
