class Oquvchi:
    def __init__(self,ism,familiya,baho):
        '''oquvchi xususiyatlari'''
        self.ism=ism
        self.familiya=familiya
        self.baho=baho

    def get_info(self,):
        print(f"{self.ism} {self.familiya}ning bahosi: {self.baho}")

oquvchi1=Oquvchi('Sobit','Baxtiyorov',4)
oquvchi2=Oquvchi('Rustam','Allayorov',5)
oquvchi2.get_info()
oquvchi1.get_info()
