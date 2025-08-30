def avto_info(make, model, rangi, karobka, yili, narxi=None):
    avto={'kompaniya':make,
          'model':model,
          'rang':rangi,
          'karobka':karobka,
          'yil':yili,
          'narx':narxi}
    return avto
print('saytimizdagi avtolar royxatini shakllantiramiz.')
avtolar=[]
while True:
    print('\nquyidagi malumootlarni kiriting. ',end='')
    kampaniya=input('Ishlab chiqaruvchi: ')
    model=input('modeli: ')
    rangi=input('rangi: ')
    karobka=input('karobka: ')
    yili=input('ishlab chiqarilgan yili: ')
    narxi=input('narxi: ')
    avtolar.append(avto_info(kampaniya, model, rangi,\
                             karobka, yili, narxi))
    print(avtolar)
    javob=input('yana avto qushasizmi? (ha/yoq): ')
    if javob=='yoq':
        break
