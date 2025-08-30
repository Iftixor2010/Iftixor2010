def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Nolga bo'lish mumkin emas"
print("Kalkulyator dasturiga xush kelibsiz!")
print("1. Qo'shish")
print("2. Ayirish")
print("3. Ko'paytirish")
print("4. Bo'lish")
tanlov = input("Amalni tanlang (1/2/3/4): ")
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
if tanlov == '1':
    print("Natija:", add(son1, son2))
elif tanlov == '2':
    print("Natija:", subtract(son1, son2))
elif tanlov == '3':
    print("Natija:", multiply(son1, son2))
elif tanlov == '4':
    print("Natija:", divide(son1, son2))
else:
    print("Noto'g'ri tanlov!")
