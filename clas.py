class Fan:
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]


    def add_student(self,talaba):
        '''fanga talabalar qoshish'''
        self.talabalar.append(talaba)
        self.talabalar_soni+=1

a=Fan('Algebra')
