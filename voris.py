class Shaxs:
    '''Shaxslar haqida malumot'''
    def __init__(self, ism, familiya, passport, tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil

    def get_info(self):
        '''Shaxsning haqida malumot'''
        info=f"{self.ism} {self.familiya} "
        info+=f"Passport:{self.passport}, {self.tyil}-yilda tugulgan"
        return info
    def get_age(self, yil):
        '''shaxsning yoshini qaytaruvchi metod'''
        return yil-self.tyil
    

class Manzil:
    '''manzil saqlash uchun klass '''
    def __init__(self,uy,kocha,tuman,viloyat):
        '''manzil xususiyatlari'''
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat

    def get_manzil(self):
        '''manzilni korish'''
        manzil=f"{self.viloyat} viloyati, {self.tuman} tumani,{self.kocha} ko'chasi, {self.uy}-uy"
        print(manzil)
    
class Talaba(Shaxs):
    '''talaba classi'''
    def __init__(self, ism, familiya, passport, tyil, idraqam,manzil,):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam=idraqam
        self.bosqich=1
        self.manzil=manzil
        


    def get_id(self):
        '''talabaning id raqami'''
        return self.idraqam
    def get_bosqich(self):
        '''talabaning oqish bosqichi'''
        return self.bosqich
    
    def get_info(self):
        '''Shaxsning haqida malumot'''
        info=f"{self.ism} {self.familiya} "
        info+=f"Passport:{self.passport}, {self.tyil}-yilda tugulgan"
        info+=f"{self.get_bosqich}-boqich. ID raqami: {self.idraqam}"
        print(info)
            
    def get_name(self,ism):
        self.ism=ism
        print(f"{self.ism}")

    

