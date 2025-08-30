talabalar=['jijibek', 'gammik', 'cholap', 'qazi']
baholangan_talabalar={}
while talabalar:
    talaba=talabalar.pop()
    baho=input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f'{talaba.title()} baholandi')
    baholangan_talabalar[talaba]=baho