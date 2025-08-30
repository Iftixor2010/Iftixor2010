def yosh_hisobla():
    '''Foydalanuvchi tugilgan yilidan yoshini hisoblaydi'''   
    try:
        joriy_yil = int(input('Joriy yilni kiriting: '))
        tugulgan_yil = int(input('Tugilgan yilingizni kiriting: '))
        yosh = joriy_yil - tugulgan_yil
        print(f'Siz {yosh} yoshdasiz.')       
    except ValueError:
        print('Iltimos, faqat raqamli malumot kiriting.')
    davom_etish='davom ettirasizmi ha/yoq'
    if davom_etish=='yoq':
        print('str')
    else:
        yosh_hisobla
yosh_hisobla()
