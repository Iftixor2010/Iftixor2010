yigindi = 0

while True:
    try:
        raqam= int(input('Son kiriting (0 siklni toxtatadi): '))
        if raqam<0:
            continue 
        elif raqam==0:
            break  
        yigindi+=raqam  
    except ValueError:
        print('Iltimos, togri son kiriting!')

print('+ sonlar yigindisi: ', yigindi)
