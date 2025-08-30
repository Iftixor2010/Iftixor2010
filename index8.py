def foydalanuvchi_malumotlari():
    foydalanuvchilar = []
    
    while True:
     
        ism = input("Ismingizni kiriting: ")
        familiya = input("Familiyangizni kiriting: ")
        tugilgan_yil = input("Tug'ilgan yilingizni kiriting: ")
        tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ")
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
        
       
        foydalanuvchilar.append(foydalanuvchi_lugat)
        

        davom_etish = input("Yana ma'lumot kiritishni istaysizmi? (ha/yo'q): ")
        if davom_etish.lower() != 'ha':
            break
    
   
    return foydalanuvchilar


print(foydalanuvchi_malumotlari())
