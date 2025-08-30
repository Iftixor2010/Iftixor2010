# format()
# s=input("kiriting:" )
# print("salom{}".format(s))
# truncate long string
# print("{:.5}".format(s))
# print(s.capitalize())
# print (s.casefold())
# print(s.count("dasturlash"))
# uzunligi 5 ga teng
# s="salom"
# print(s[0:])

# ("SALOM DUNYO" > "DUNYO SALOM")
# s=input("SALOM DUNYO =>  DUNYO SALOM")
# s=str("kiriting: ")

# import math
# print(math.ceil(8.7))
# print(math.floor(8.7))
# print(math.sqrt(81))

# ikki xil vaqt kiritiladi
# time1=soat1, menut1, secund1,
# time2=soat2, menut2, secund2,

# soat1=int(input("1-soat: "))
# minut1=int(input("1-minut: "))
# secund1=int(input("1-secund: "))

# soat2=int(input("2-soat: "))
# minut2=int(input("2-minut: "))
# secund2=int(input("2-secund: "))

# 1 soat 3600 secund, 1minut 60secund
# secund=(soat2-soat1)*3600+(minut2-minut1)*60+(secund2-secund1)
# print("secund: {} ".format(secund))

# til=input("Tlini tanlang: uz/fr ? ")

# if til == "uz":
# print("Assalomu alaykum")
# else:""
# print("banjur")

# ikkita tasodifiy son yig'indisini toping

# from random import randint

# a=randint(1,100)
# b=randint(1,100)

# c=int(input("{}+{}=".format(a,b)))

# if c==(a+b):
#    print("tog'ri")
# else:
#    print("xato!")

#  summa=input("summani kiriting: ")

#  if summa.isdigit() and int(summa)>0 and int(summa)<100000000:
#     print("tashakkur")
#  else:
#     print("xatolik bor!")

# a='a'
# e='e'
# i='i'
# o='o'
# u='u'
# t="o'"
# b=input('harf kiriting: ')
# if b==a or b==e or b==i or b==o or b==u or b==t:
#    print('unli harf kiritdingiz ')
# elif b==int:
#    print('siz son kiritdingiz')

# else:
#    print('siz undosh harf kiritdingiz')

# range(1,32) #1, 2, 3, 4, ..., 31 


# for son in range(1, 32):
#    print(son)

# karra jadvali . 9 karra
# 9 x 1 = 9, 9 x 2 = 18, ... 9 x 10 = 90

# karra=9

# for son in range(1,11):
#    natija=karra * son

#    print("{} x {} = {}".format(karra, son, natija))

# son = 1 
# while son <= 31:
#     print(son)
#    son=son+1

# from random import randint 
# kodlar=[135, 132, 134, 131, 130, 133]  list
# yangi_kod = randint(130, 135)
# i=0

# while yangi_kod in kodlar:
#    i+=1
#    yangi_kod=randint(130, 135)

# print("takrorlanishlar soni:",i)
# print(yangi_kod)

# satr=input("so'z kiriting: ")

# for s in satr:
#    print(s)

# from datetime import datetime
# from tkinter import *

# oyna = Tk()
# oyna.title("sevimli oynam")
# oyna.geometry("300x300")

# natija = Label(text="Natija",bg="white")
# natija.place(x=90, y=135, width=120, height=40)

# yil = Entry()
# yil.place(x=75, y=50, width=150, height=30)

# def farq():
#    bugun = datetime.today()
#    natija.config(text=bugun.year - int(yil.get())) 
    
# tugma = Button(text="Hisoblsh",command=farq)
# tugma.place(x=90, y=90, width=120, height=40)

# oyna.mainloop()

# def farq(yil):
#    bugun = datetime.today()
#    natija = bugun .year - int(yil)
#    return natija

# tugulgan_yil = input("tug'ulgan yilni kiriting: ")
# natija_f = farq(tugulgan_yil)

# print("natija: ", natija_f)

# maktab_yil = input("maktab yilni kiriting: ")
# natija_f = farq(maktab_yil)
# print("natija: ", natija_f)

# son = 45
# print("son = ", son, type(son))
# sonlar = [45, 61, 27, -91]
# print("sonlar = ", sonlar, type(sonlar))
# sonlar = [45, 61, 27, -91, "python", 6.38, False]
# print(len(sonlar))
# print(sonlar)
# sonlar.append("PHP")
# print(sonlar)

# import tkinter as tk
# win = tk.Tk()
# y = 0


# def sayHi():
#    global y
#    print(y)


# from tkinter import Tk


# bin.geometry('200x100')
# b = Tk.Button(bin,)
# text='click here',
# ('command=sayHi')  
# b.pack()
# bin.mainloop()

# from turtle import *
# setposition(-60, 0)
# speed(0)
# bgcolor("black")
# colors = ["orange", "white"]
# pensize(2)
# for i in range(150):
#    color(colors[i % 2])
#    rt(i)
#    circle(90, i)
#    up()
#    fd(i+50)
#    down()
#    rt(90)
#    fd(i-65)
#    hideturtle()
# done()

# import turtle as t#

# t.speed(0) 
# t.bgcolor("black")
# t.pencolor("orange")
# def square(x, y):
#    for j in range(4):
#        t.forward(x)
#        t.right(y)
# for i in range(80):
#    square(170, 90)
#    t.right(5)
#    t.circle(50)
#    t.right(50)
#    t.hideturtle()
# t.done()

# from turtle import *
# from colorsys import *
# setposition(50, -50)
# speed(0)
# bgcolor('black')
# pensize(2)
# n=100
# h=0
# for i in range(120):
#    for i in range(4):
#        color(hsv_to_rgb(h, 1, 1))
#        h += 0.003
#        circle(40+i*5, 90)
#        forward(250)
#        left(90)
#    rt(10)
#    hideturtle()
# done 

# from turtle import*
# assalomu_alaykum='salom'
# print(assalomu_alaykum)

#a="bmwni yaxshi kurasizmi"
#print(a)


#a=11
#b=22
#c=11+22
#print(c)

#s=input('kiriting: ')
#print(s.casefold())
#print(s.count('dasturlash'))

#til=input('tilni tanling: uz/en ? ')

#if til=='uz':
#    print('Assalomu alaykum')
#elif til=='en':
#    print('HELLO')
#else:
#   print('uz/en lardan birini tanlang')

# ikkita tasodifiy son yig'indisini toping

#from random import randint

#a = randint(1, 500)
#b = randint(1, 500)

#c = int(input('{} + {} = '.format(a, b)))

#if c == (a + b):
#    print("to'g'ri")
#else:
#    print("xato!")

#summa = input('summani kiriting: ')

#if summa.isdigit() and int(summa) > 0 and int(summa) < 10000000:
#    print('tashakkur)')
#else:
#    print('xatolik bor!')

#ism = input('ismingizni kiriting: ')
#fam = input('familiyangizni kiriting: ')
#
#if ism or fam:
#    print('tashakkur)')
#else:
#    print('ism yoki familiyangizni kiriting!')


#n = int(input("son kiriting: "))


#yigindi = 0
#for i in range(2, n +1, 2):  
#    yigindi += i


#print(f"1 dan {n} gacha bo'lgan juft sonlar yig'indisi: {yigindi}")

#12-dastur.statistika
# import pygal

# line_chart = pygal.Line()
# line_chart.title='Statistika'
# line_chart.x_labels=['Fevral', 'Mart', 'Aprel', 'May']
# line_chart.add('Instagram', [9.24, 13.7, 16.24, 18.07])
# line_chart.render_in_browser()

# davlat = {'davlat': 'Ozbekiston', 'poytaxt': 'Toshkent', 'til':'uzbek'}
# print(davlat)
# print(type(davlat))

# print(davlat['davlat'], '-', davlat['poytaxt'])

# davlat2 = dict()
# davlat2['davlat'] = 'AQSH'
# davlat2['poytaxt'] = 'vashington'

# print(davlat2['poytaxt'])

# davlat2.update({'davlat': '*', 'poytaxt': 'Toshkent'})
# print(davlat2)

# from datetime import datetime
# from tkinter import *

# oyna = Tk()
# oyna.title('Dasturcha :)')
# oyna.geometry('400x400')

# yil = Entry()
# yil.place(x=85, y=50, width=150, height=30)

# oyna.mainloop()

# tugilgan_yil = input('Tugilgan yilini kiriting: ')

# bugun = datetime.today()
# natija = bugun.year - int(tugilgan_yil)

# print('natija: ', natija)

# maktab_yil = input('yilni kiriting: ')
# natija = bugun.year - int(maktab_yil)
# print('natija: ', natija)

# from turtle import Turtle, Screen
# oyna = Screen()
# oyna.title('Mening oynam')

# chiziq = Turtle()
# chiziq.color('red')
# chiziq.pensize(5)

# chiziq.hideturtle()
# chiziq.up()
# chiziq.goto(300, 300)
# chiziq.down()
# chiziq.goto(300, -300)
# chiziq.goto(-300, -300)
# chiziq.goto(-300, 300)
# chiziq.goto(300, 300)

# koptok = Turtle()
# koptok.shape('circle')
# koptok.color('red')
# koptok.up()
# koptok.goto(0, 0)

# step_x = 3
# step_y = 2

# while True:
#      x, y = koptok.position()
#      if x + step_x >= 300 or x + step_x <= -300:
#          step_x = -step_x

#      if y + step_y >= 300 or y + step_y <= -300:
#                  step_y = -step_y




#      koptok.goto(x+step_x, y+step_y)

# oyna.mainloop()

# from random import randint
# kodlar = [] 
# yangi_kod = randint(130, 135)

# i = 0
# while yangi_kod in kodlar:
#      i += 1
#      yangi_kod = randint(130, 135)

# print('takrorlanishlar soni: ', i)
# print(yangi_kod)    
