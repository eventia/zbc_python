# 'ab' is short for 'a'ddress'b'ook
ab = {  'Baram' : 'ludenscode@gmail.com',
        'Larry' : 'larry@wall.org',
   		'Matsumoto' : 'matz@ruby-lang.org',
   		'Spammer' : 'spammer@hotmail.com', }
print("Baram's address is", ab['Baram'])

del ab['Spammer']    # Deleting a key-value pair
print('\nThere are {} contacts in the ddress-book\n'.format(len(ab)))
# for name, address in ab.items():
#   print('Contact {} at {}'.format(name, address))

#for key in ab:
#    print('Contact {} at {}'.format(key, ab[key]))
for key, value in ab:
    print('Contact {} at {}'.format(key, value))

ab['Gildong'] = 'gildong@ueldo.org'    # Adding a key-value pair
if 'Gildong' in ab:
   print("\nGildong's address is", ab['Gildong'])
