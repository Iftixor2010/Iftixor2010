def foydalanuvchi_malumotlari():
    
    ism = input("Ismingizni kiriting: ")
    familiya = input("Familiyangizni kiriting: ")
    tugilgan_yil = input("Tugilgan yilingizni kiriting: ")
    tugilgan_joy = input("Tugilgan joyingizni kiriting: ")
    email = input("Elektron manzilingizni kiriting: ")
    telefon = input("Telefon raqamingizni kiriting: ")
    foydalanuvchi_lugat = {
        "Ism": ism,
        "Familiya": familiya,
        "Tug'ilgan yil": tugilgan_yil,
        "Tug'ilgan joy": tugilgan_joy,
        "Elektron manzil": email,
        "Telefon": telefon
    }
    
   
    print(foydalanuvchi_lugat)


foydalanuvchi_malumotlari()
