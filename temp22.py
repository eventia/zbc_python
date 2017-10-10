ab = {  'Baram' : 'ludenscode@gmail.com',
        'Larry' : 'larry@wall.org',
   		'Matsumoto' : 'matz@ruby-lang.org',
   		'Spammer' : 'spammer@hotmail.com', }
print("Baram's address is", ab['Baram'])
del ab['Spammer']
print('\nThere are {} contacts in the addrss book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
#for key in ab:
#    print('Contact {} at {}'.format(key, ab[key]))

ab['Gildong'] = 'gildong@ueldo.org'

if 'Gildong' in ab:
    print("\nGildong's address is", ab['Gildong'])
