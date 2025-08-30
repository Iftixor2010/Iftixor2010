import math
import datetime
import random
def kalkulyator():
    print("\nMatematik kalkulyator")
    print("Misol: 2 + 3, 4 * 5, sin(30), sqrt(16), va hokazo.")
    amal = input("Hisoblash amalini kiriting: ")
    try:
        natija = eval(amal)
        print(f"Natija: {natija}")
    except Exception as e:
        print(f"Xatolik: {e}")

def vaqt_bilan_ishlash():
    print("\nSana va vaqt bilan ishlash")
    print("1. Joriy sanani ko'rish")
    print("2. Keyingi yoki oldingi kunni hisoblash")
    tanlov = input("Tanlovni kiriting (1 yoki 2): ")
    if tanlov == '1':
        bugun = datetime.datetime.now()
        print(f"Bugungi sana: {bugun.strftime('%Y-%m-%d %H:%M:%S')}")
    elif tanlov == '2':
        kunlar = int(input("Necha kun qo'shilsin yoki ayirilsin? (manfiy qiymat ayirish uchun): "))
        yangi_sana = datetime.datetime.now() + datetime.timedelta(days=kunlar)
        print(f"Yangi sana: {yangi_sana.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("Noto'g'ri tanlov!")

def matn_tahriri():
    print("\nMatn tahriri")
    matn = input("Matnni kiriting: ")
    print("1. Katta harflar bilan yozish")
    print("2. Kichik harflar bilan yozish")
    print("3. Harf boshi katta bo'lishi")
    tanlov = input("Tanlovni kiriting (1, 2 yoki 3): ")
    if tanlov == '1':
        print("Natija:", matn.upper())
    elif tanlov == '2':
        print("Natija:", matn.lower())
    elif tanlov == '3':
        print("Natija:", matn.title())
    else:
        print("Noto'g'ri tanlov!")

def tasodifiy_son_oyini():
    print("\nTasodifiy son o'yini")
    son = random.randint(1, 100)
    urinishlar = 0
    print("1 dan 100 gacha sonni toping!")
    while True:
        urinishlar += 1
        taxmin = int(input("Sonni kiriting: "))
        if taxmin < son:
            print("Katta son kiriting.")
        elif taxmin > son:
            print("Kichik son kiriting.")
        else:
            print(f"Tabriklaymiz! Siz {urinishlar} urinishda to'g'ri topdingiz.")
            break

def asosiy_menyu():
    while True:
        print("\n--- Ko'p funktsiyali dastur ---")
        print("1. Kalkulyator")
        print("2. Vaqt bilan ishlash")
        print("3. Matn tahrirlash")
        print("4. Tasodifiy son o'yini")
        print("5. Dasturni tugatish")
        tanlov = input("Tanlovni kiriting (1-5): ")
        
        if tanlov == '1':
            kalkulyator()
        elif tanlov == '2':
            vaqt_bilan_ishlash()
        elif tanlov == '3':
            matn_tahriri()
        elif tanlov == '4':
            tasodifiy_son_oyini()
        elif tanlov == '5':
            print("Dastur tugatildi. Etiboringiz uchun rahmat!")
            break
        else:
            print("Noto'g'ri tanlov, qayta urinib ko'ring.")
asosiy_menyu()
