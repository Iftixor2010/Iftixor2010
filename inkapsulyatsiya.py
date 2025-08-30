class Talaba:
    '''talaba nomli klas yaratamiz'''
    def __init__(self,ism,familiya,tyil):
        '''talabaning xususiyatlari'''
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=1
    def tanishtir(self):
        print(f" {self.ism} {self.familiya}."
              f"{self.tyil} bosqich:{self.bosqich}")
        
    def get_age(self,yil):
        '''talabaning yoshini qaytaradi'''
        return yil-self.tyil


    
        

class Fan:



    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]


    def get_students(self):
        return [talaba.tanishtir() for talaba in self.talabalar]    




    def add_students(self,talaba):
        '''fanga talabalar qoshish'''
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
   

#matematika=Fan('algebra')
talaba1=Talaba('shaxboz','nematov',1987)
print(talaba1.__dict__.keys())
#talaba2=Talaba('Farrux','asamov',1985)
#matematika.add_students(talaba1)
#matematika.add_students(talaba2)
#print(matematika.talabalar_soni)

#mat_talabalar=matematika.get_students()
#print(mat_talabalar)
#['alijon Valiyev. 1-bosqich talabsi',
# 'hasan Alimov. 1-bosqich talabasi',
# 'akrom Boriyev. 1-bosqich talabasi']

