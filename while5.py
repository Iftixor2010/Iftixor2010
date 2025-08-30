print('kiritilgan sonni kvadratini qaytaruvchi dastur.')
savol='istalgan son kiriting '
savol+='(toxtatish uchun "exit" deb yozing): '
while True:
    qiymat=input(savol)
    if qiymat=='exit':
        break
    else:
        print(float(qiymat)**2)