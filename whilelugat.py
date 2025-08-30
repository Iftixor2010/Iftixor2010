ismlar=[]
print('yaqin dostlaringizni ruyxatini tuzamiz')
n=1
while True:
    savol=f"{n}-dostingiz ismni kiriting."
    ism=input(savol)
    ismlar.append(ism)
    javob=input('yana ism qoshasizmi (ha/yoq)')
    if javob=='ha':
        n+=1
    
        continue

    else:
        break
print('ruyxat tuzildi')
print('dostlaringiz royxati:')
for ism in ismlar:
    print(ism.title())