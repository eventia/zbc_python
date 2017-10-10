a = 5         # 0101
b = 3         # 0011
print(a&b)    # 0001 => 1
print(a|b)    # 0111 => 7
print(a^b)    # 0110 => 6
print(~a)     # 1010 ... MSB => -6

#print(a>b)
#print(a<b)
#print(a>=b)
#print(a<=b)
print(a!=b)    #T
print(not(a!=b)) #F
print(not(a and b))
print(not(a or b))
