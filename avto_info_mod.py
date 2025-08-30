def avto_info(make, model, rangi, karobka, yili, narxi=None):
    avto={'kompaniya':make,
          'model':model,
          'rang':rangi,
          'karobka':karobka,
          'yil':yili,
          'narx':narxi}
    print(avto)
def avto_kirit():
    '''foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida malumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya'''
    print(avto_kirit)



avtolar=[]
while True:
    print('\nquyidagi malumotlarni kiriting', end='')
    kompaniya=input('ishlab chiqaruvchi:')
    model=input('modeli')
    rangi=input('rangi')
    karobka=input('karobka')
    yili=input('yili')
    narxi=input('narxi:')
    avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narxi))
    javob='yana avto qoshasizmi? (yes/no):'
    if javob=='no':
        break
    print(avtolar)
def info_print(avto_info):
    '''avtomobillar haqida malumotlar saqlangan lugatni konsolga chiqaruvchi funksiya'''
    print(f'{avto_info['rang'].title()}'
          f'{avto_info['kompaniya'].upper()}'
          f'{avto_info['model'].upper()}'
          f'{avto_info['karobka']} karobka,'
    f"{avto_info['yil']}-yil, {avto_info['narx']}$")

