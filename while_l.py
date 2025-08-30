#son=1
#while son<=31:
#    print(son)
#    son=son+1
from random import randint
kodlar=[135, 132, 134, 131]
yangi_kod=randint(130, 135)
while yangi_kod in kodlar:
    i=+1
    yangi_kod=randint(130, 135)
print('takrorlanishlar soni: ', i )
print(yangi_kod)
