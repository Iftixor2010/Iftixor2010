class Avto:
    __num_avto=0
    '''avtomobilning xususiyatlari'''
    def __init__(self, make, model, rang, yil, narx):
        '''avtomobilning xususiyatlari'''
        self.make=make
        self.model=model
        self.rangi=rang
        self.yili=yil
        self.narxi=narx
        Avto.__num_avto+=1
    def __repr__(self):
        return f"Avto: {self.make} {self.model}"
    