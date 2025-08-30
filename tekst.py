

faylnomi='ustozlar.txt'
with open('faylnomi', 'w') as fayl:
    fayl.write('hello world')
    
faylnomi='new_file.txt'
ism='olimjon'
tyil=2004
with open(faylnomi, 'a')as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')


faylnomi='new.txt'
ismi='bekjon'
tyili=2010
with open(faylnomi, 'a') as fayl:
    fayl.write(ismi+'\n')
    fayl.write(str(tyili)+'\n')

