try:
    text = input('Enter something --> ')
except EOFError:
    print("Why did not do an EOF on me?")
except KeyboardInterrupt:
    print("You cancelled the operation.")
else:
    print("You entered {}".format(text))
