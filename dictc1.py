# 'ab' is short for 'a'ddress'b'ook
ab =    {
        'Baram' : 'ludenscode@gmail.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'
        }


# for name, address in ab.items():
#    print('Contact {} at {}'.format(name, address))

for name in ab:
   print(name)

for name in ab:
   print(name, ab[name])

for name, address in ab.items():
   print(name, address)

for name, address in ab.items():
   print('{} {}'.format(name, address))
