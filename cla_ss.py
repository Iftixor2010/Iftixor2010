class Student:
    def __init__(self,ism,yosh,baholar):
        self.ism=ism
        self.yosh=yosh
        self.baholar=[baholar]

    
    def add_grade(self):
        self.baholar.append("95")

    def get_info(self):
        print(f"{self.ism}, yoshi-{self.yosh} bahosi-{ self.baholar}")


class Talaba(Student):

    def __init__(self, ism, yosh, baholar,kursi,oquv_yili):
        super().__init__(ism, yosh, baholar)
        self.kurs=kursi
        self.oquvyili=oquv_yili

    def get_infor(self):
        print(f" {self.ism}-ismi, {self.yosh}-yoshi"
              f" {self.baholar}-bahosi, {self.kurs}-kursi, {self.oquvyili}-o'quv yili")
        


student1=Talaba("Dilshod",24,20,3,"2024-2025")
student1.add_grade()
student1.get_infor()