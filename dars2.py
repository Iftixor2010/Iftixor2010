# INPUT
my_dict = {'name': 'Ali', 'age': 25}
my_dict['job'] = 'Dasturchi'
my_dict['age'] = 26
del my_dict['age']

# Natijani chiqarish
print(my_dict)

# 'age' kaliti yo'qligini tekshirish
print(my_dict.get('age', 'Kalit mavjud emas'))  # 'age' kaliti mavjud bo'lmasa, 'Kalit mavjud emas' qaytadi
