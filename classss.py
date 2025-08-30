class Car:
    def __init__(self,make,model,year,price):
        '''mashina haqida malumotlar '''
        self.make=make
        self.model=model
        self.year=year
        self.price=price
        self.discount='15%'

    def display_info(self):
        print(f"mashinani ishlab chiqaruvchi kompaniya: {self.make}. "
              f" mashinaning modeli: {self.model}. "
              f" mashina ishlab chiqarilgan yil: {self.year}. "
              f" mashina narxi: {self.price}. "
              f" mashinaga berilgan chegirma: {self.discount}.")


mashina1=Car('BMW','M5',2018,'600k$')
mashina1.display_info()