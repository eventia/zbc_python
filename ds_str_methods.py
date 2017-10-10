# This is a string object
name = 'Baram'
if name.startswith('Bar'):
    print('Yes, the string starts with "Bar"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if 'x' not in name:
    print('No, it is not contains the string "x"')

if name.find('ara') != -1:
    print('Yes, it contains the string "ara"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
