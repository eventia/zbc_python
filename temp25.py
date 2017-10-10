delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']

for nation in mylist:
    print(nation, end='')
    if nation != mylist[-1]:
        print(delimiter, end='')
print('')



# 'Brazil_*_Russia_*_India_*_China'
print(delimiter.join(mylist))
