shoplist = ['apple', 'mango', 'carrot', 'banana']

mylist = shoplist
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)

mylist = shoplist[:]
print('shoplist is', shoplist)
print('mylist is', mylist)
del mylist[0]
print('modified shoplist is', shoplist)
print('modified mylist is', mylist)
