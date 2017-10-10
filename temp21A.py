zoo = ('python', 'elephant', 'penguin')
print('동물원에 있는 동물의 수 : ', len(zoo))
new_zoo = 'monkey', 'camel', zoo
print('새 동물원에 있는 우리의 수 : ', len(new_zoo))
print('새 동물원에 있는 동물들 : ', new_zoo)
print('옛 동물원에서 온 동물들 : ', new_zoo[2])
print('옛 동물원에서 온 마지막 동물 : ', new_zoo[2][2])
print('새 동물원 동물의 수 : ', len(new_zoo)-1+len(new_zoo[2]))
