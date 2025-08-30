class Shaxs:
    shaxssoni=3
    '''Shaxslar haqida malumot'''
    def __init__(self, ism, familiya, passport, tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
        Shaxs.shaxssoni+=1
    def get_info(self):
        '''Shaxsning haqida malumot'''
        info=f"{self.ism} {self.familiya} "
        info+=f"Passport:{self.passport}, {self.tyil}-yilda tugulgan"
        return info
    def get_age(self, yil):
        '''shaxsning yoshini qaytaruvchi metod'''
        return yil-self.tyil
    @classmethod
    def get_shaxs_soni(cls):
        return cls.shaxssoni

print(Shaxs.get_shaxs_soni())
