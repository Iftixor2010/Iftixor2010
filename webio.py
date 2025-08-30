# from pywebio.input import input
# from pywebio.output import put_text
# import random

# def sontop(x=10):
#     tasodifiy_son = random.randint(1, x)
#     while True:
#         taxmin = int(input(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?"))
#         if taxmin < tasodifiy_son:
#             put_text("Kattaroq son kiriting")
#         elif taxmin > tasodifiy_son:
#             put_text("Kichikroq son kiriting")
#         else:
#             put_text("Yutding!!")
#             break

# sontop()

import random
from time import sleep
import pywebio.output
from pywebio.output import put_text

def sontop_pc(x=10):
    pywebio.output.clear(scope=-1)

    global quyi, yuqori, taxmin
    quyi = 1
    yuqori = x

    put_text(f"1 dan {x} gacha son o'ylang. 3 soniya vaqt beriladi.")
    
    for i in [3, 2, 1, "Boshladik!"]:
        put_text(str(i))
        sleep(1)

    def guess():
        pywebio.output.clear(scope=-1)
        global taxmin
        taxmin = random.randint(quyi, yuqori)

sontop_pc()

