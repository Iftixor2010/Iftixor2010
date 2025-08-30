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
    

class Foydalanuvchi(Shaxs):
    '''foydalanuvchi xususiyatli'''
    def __init__(self, ism, familiya, passport, tyil,yoshi,vazni):
        super().__init__(ism, familiya, passport, tyil)
        self.yoshi=yoshi
        self.vazni=vazni
    
    def get_all_info(self):
        print(f"{self.ism}-ism. "
              f" {self.familiya}-familiya."
              f" {self.passport}-passport."
              f" {self.tyil}-tyil {self.yoshi}-yoshi {self.vazni}-vazni")



class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, yoshi, vazni,boyi):
        super().__init__(ism, familiya, passport, tyil, yoshi, vazni)
        self.boyi=boyi


    
    def get_all_info(self):
        print(f"{self.ism}-ism. "
              f" {self.familiya}-familiya."
              f" {self.passport}-passport."
              f" {self.tyil}-tyil {self.yoshi}-yoshi {self.vazni}-vazni"
              f"{self.boyi}-bo'yi.")
        
shaxs1=Admin('ilhom','qaxxorov',2332233,1674,449,'834kg','1.75m')
shaxs1.get_all_info()