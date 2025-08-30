def oquvchilar():
    while True:
        ism = input('Ismingizni kiriting: ')
        familiya = input('Familiyangizni kiriting: ')
        yosh = input('Yoshingizni kiriting: ')
        print(f"Sizning yoshingiz {yosh}, ismingiz {ism}, familiyangiz {familiya}.")
        davom_ettirish = input("Davom etasizmi? (ha/yo'q): ")
        if davom_ettirish.lower() == 'yo\'q':
            break
oquvchilar()