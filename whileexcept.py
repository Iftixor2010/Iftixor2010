# Foydalanuvchidan yoshini so'rash
yosh = 'yoshingizni kiriting: '

while True:
    # Foydalanuvchidan yoshini so'rash va davom etish yoki to'xtatishni so'rash
    qiymat = input(yosh + 'yana davom ettirsizmi? (ha/yoq): ')
    
    if qiymat.lower() == 'yoq':  # Agar "yoq" deb javob bersa, siklni to'xtatish
        break
    elif qiymat.lower() == 'ha':  # Agar "ha" deb javob bersa, yosh so'rash
        try:
            yosh = int(input('Yoshingizni kiriting: '))  # Yoshingizni so'rash
            print(f'Siz {2024 - yosh} yilda tug\'ulgansiz')  # Tug\'ilgan yilni hisoblash
        except ValueError:  # Agar foydalanuvchi son kiritmasa, xatolikni chiqarish
            print('Butun son kiritmadingiz!')
    else:
        print('Iltimos, "ha" yoki "yoq" deb javob bering.')
