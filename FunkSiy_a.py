from datetime import datetime
def farq(yil):
    bugun=datetime.today()
    natija=bugun.year-int(yil)
    return natija
tugilgan_yil=input('Tugilgan yilni kiriting: ')

bugun=datetime.today()
natija_f=farq(tugilgan_yil)
print('Natija: ', natija_f)

maktab_yil=input('yilni kiriting: ')
natija_f=farq(maktab_yil)
print('Natija: ', natija_f)