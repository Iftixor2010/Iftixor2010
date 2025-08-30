while True:
    yosh = input('Yoshingizni kiriting: ')
    try:
        yosh = int(yosh)
        print(f'Siz {2024 - yosh}-yilda tugilgansiz.')
    except ValueError:
        print('Iltimos, butun son kiriting.')
    davom = input('Yana davom ettirsizmi? (ha/yoq): ')
    if davom.lower() == 'yoq':
        break
