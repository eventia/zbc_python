shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')
mylist = shoplist[:]

del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
