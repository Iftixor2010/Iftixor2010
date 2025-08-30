def tortburchak_yuzi(uzunlik, eni):
    '''Togri tortburchakning yuzini hisoblovchi funksiya'''
    return uzunlik * eni
uzunlik = float(input("Togri tortburchakning uzunligini kiriting: "))
eni = float(input("Togri tortburchakning enini kiriting: "))
yuza = tortburchak_yuzi(uzunlik, eni)
print(f"Togri tortburchakning yuzi: {yuza}")