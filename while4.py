print('kiritilgan sonni kvadratini qaytaruvchi dastur.')
savol='istalgan son kiriting '
savol+='(toxtatish uchun "exit" deb yozing): '
ishora=True
while ishora:
    qiymat=input(savol)
    if qiymat=='exit':
        ishora=False
    else:
        print(float(qiymat)**2)

