# 'ab' is short for 'a'ddress'b'ook
ab = {	'Baram' : 'ludenscode@gmail.com',
'Larry' : 'larry@wall.org',
   		'Matsumoto' : 'matz@ruby-lang.org',
   		'Spammer' : 'spammer@hotmail.com'
}
print("Baram's address is", ab['Baram'])

# Deleting a key-value pair
del ab['Spammer']
print('\nThere are {} contacts in the ddress-book\n'.format(len(ab)))

for name, address in ab.items():
   print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Gildong'] = 'gildong@ueldo.org'

if 'Gildong' in ab:
   print("\nGildong's address is", ab['Gildong'])
