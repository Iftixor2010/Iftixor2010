print('dostlaringiz yoshini saqlaymiz')
dostlar={}
ishora=True
while ishora:
    ism=input('dostingizni ismini kiriting: ')
    yosh=input(f'{ism.title()}ning yoshini kiriting:')
    dostlar[ism]=int(yosh)
    javob=input('yana malumot qushasizmi (ha/yoq)')
    if javob=='yoq':
        ishora=False