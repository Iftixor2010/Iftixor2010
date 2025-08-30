from uuid import uuid4
class Avto:
    num_avto=0
    '''avtomobil classi'''
    def __init__(self, make, model, rang, yil, narx,km=0):
        '''avtomobilning xususiyatlari'''
        self.make=make
        self.model=model
        self.rangi=rang
        self.yili=yil
        self.narxi=narx
        self.__km=km
        self.__id=uuid4()
        Avto.num_avto+=1
    @classmethod 
    def get_num_avto(cls):
        return cls.num_avto

    def get_km(self):
        print({self.__km})

    def get_id(self):
        print({self.__id})
    
    def get_all_info(self):
        print(f" {self.make} "
              f" {self.model}"
              f" {self.rangi}"
              f" {self.yili}"
              f" {self.narxi}"
              f" {self.__km}"
              f" {self.__id}")
        
avto1=Avto('gm','malibu','qora',2017,8282,100000)
avto1.get_all_info()
print(avto1.num_avto)
print(Avto.get_num_avto())

import tkinter 

