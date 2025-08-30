class Transport:
    def __init__(self,turi,markasi,yili):
        """transportning xususiyatlari"""
        self.turi=turi
        self.markasi=markasi
        self.yili=yili

    def malumot_ber(self):
        print(f" Transportning turi: {self.turi}"
              f" Transportning markasi: {self.markasi}"
              f" Transportning yili: {self.yili}")
        
    
class Yengil_avto(Transport):
    def __init__(self, turi, markasi, yili,yolovchilar_soni):
        super().__init__(turi, markasi, yili)
        self.yolovchilar_soni=yolovchilar_soni

    
    def get_transportinfo(self):
        print(f" Transportning turi: {self.turi}"
              f" Transportning markasi: {self.markasi}"
              f" Transportning yili: {self.yili}"
              f" Transportdagi yo'lovchilar soni: {self.yolovchilar_soni}.")

class Yuk_mashinasi(Yengil_avto):
    def __init__(self, turi, markasi, yili, yolovchilar_soni,ogirlik_sigimi):
        super().__init__(turi, markasi, yili, yolovchilar_soni)
        self.ogirlik_sigimi=ogirlik_sigimi
    def get_transport_info(self):
        print(f" Transportning turi: {self.turi}"
              f" Transportning markasi: {self.markasi}"
              f" Transportning yili: {self.yili}"
              f" Transportdagi yo'lovchilar soni: {self.yolovchilar_soni}"
              f" Og'irlik sig'imi: {self.ogirlik_sigimi}.")
    

transport1=Yuk_mashinasi('yengil avtamobil','Taoyota',2018,5,15000)
transport1.get_transport_info()