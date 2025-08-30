class Avto:
    __num_avto=0
    '''Avtomobil classi'''
    def __init__(self, make, model, rang, yil, narx):
        '''Avtomobilning funksiyalari'''
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        Avto.__num_avto+=1
    def __repr__(self):
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self,y):
        return self.narx==y.narx 

    def __lt__(self,y):
        return self.narx<y.narx
     
    def __le__(self,y):
        return self.narx<=y.narx       

avto1=Avto('GM','Malibu','Qora',2020,40000)
print(avto1)


avto2=Avto('GM','Lacetti','oq',2020,40000)
avto3=Avto('Toyota','Carolla','Silver',2018,20000)
avto4=Avto('Mazda','6','qizil',2015,35000)
avto5=Avto('Wolksvagen','Polo','qora',2015,30000)
avto6=Avto('Honda','Accord','oq',2017,42000)


class AvtoSalon:
    '''Avtosalon klassi'''
    def __init__(self,name):
        self.name=name
        self.avtolar=[]

    def __repr__(self):
        return f'{self.name} avtosalon'
    def __getitem__(self, index):
        return self.avtolar[index]

    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print('Avto kiriting')
                
    def __len__(self):
        return len(self.avtolar)

    def __getitem__(self, index):
        return self.avtolar[index]

    def __setitem__(self,index,qiymat):
        self.avtolar[index]=qiymat

    def __call__(self, *qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        return [avto for avto in self.avtolar]
        
    def __add__(self,boshqa_salon):
        yangi_salon=AvtoSalon(f"{self.name} {boshqa_salon.avtolar}")
        return yangi_salon

salon1=AvtoSalon('MaxAvto')
salon2=AvtoSalon('Avto Lider')
avto2=Avto('GM','Lacetti','oq',2020,40000)
avto3=Avto('Toyota','Carolla','Silver',2018,20000)
salon1.add_avto(avto1,avto2, avto3)

avto4=Avto('Mazda','6','qizil',2015,35000)
avto5=Avto('Wolksvagen','Polo','qora',2015,30000)
avto6=Avto('Honda','Accord','oq',2017,42000)
salon2(avto4,avto5,avto6)


print(dir(Avto))
