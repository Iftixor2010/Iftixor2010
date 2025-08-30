def yosh_hisobla():
    '''Foydalanuvchi tug'ilgan yilidan yoshini hisoblaydi'''   
    try:
        joriy_yil = int(input('Joriy yilni kiriting: '))
        tugulgan_yil = int(input('Tugilgan yilingizni kiriting: '))
        yosh = joriy_yil - tugulgan_yil
        print(f'Siz {yosh} yoshdasiz.')       
    except ValueError:
        print('Iltimos, faqat raqamli malumot kiriting.')
    
    davom_etish = input('Davom ettirasizmi? ha/yo\'q: ')
    if davom_etish.lower() == 'ha':
        yosh_hisobla()
    else:
        print("Dastur yakunlandi.")
yosh_hisobla()