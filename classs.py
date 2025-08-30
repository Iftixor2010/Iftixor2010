class User:
    def __init__(self,ism,user_name):
        '''foydalanuvchi haqida malumot'''
        self.ism=ism
        self.user_name=user_name

    def get_info(self):
        print(f"{self.ism} {self.user_name}")

r=User('baxtiyor','baxtiyor1999')
r.get_info()
