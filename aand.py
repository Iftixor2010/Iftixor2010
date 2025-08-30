a=input()
if a=='Iftixor' or a=='iftixor':
    print('sizning ismingiz togri')
else:
    print('sizning ismingiz tugri emas')

kun=input('bugun nima kun?')
harorat=float(input('havo harorati qanday?'))
if kun=='yakshanba' and harorat>30:
    print('bugun kun issiq')
elif kun=='yakshanba' and harorat<30:
    print('bugun sovuq')
else:
    print('uyda otir')
