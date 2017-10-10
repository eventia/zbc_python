str1 = "This is the amazing movie!!!"
str2 = "i"

# print(str1.find(str2))
# print(str1.find(str2, 1+str1.find(str2)))

startnumber = 0
while (startnumber!=-1):
    startnumber = str1.find(str2, startnumber)
    print(startnumber)
    if startnumber!=-1:
        startnumber = startnumber + 1

# str1.count('i')
print(str1.count(str2))

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))


delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
for nation in mylist:
    print(nation, end='')
    if nation != mylist[-1]:
        print('_*_', end='')
print('')


name = 'Baram'
if name.startswith('Bar'):
   print('Yes, the string starts with "Bar"')

if 'a' in name:
   print('Yes, it contains the string "a"')

if name.find('ara') != -1:
   print('Yes, it contains the string "ara"')
