odamlar={
    'kim':'birov', 'boyi':167 , 'yashash joyi':'miyonqol'}

odam={
    'kim':'kimdir', 'boyi':156, 'yashash joyi': 'miyonqol'}
b={
    'kim': 'juzzi', 'boyi':150, 'yashash joyi':'miyonqol'}
d=[]
uzb=[odamlar, odam, b]

for uz in uzb:
    print(f'{uz['kim']}, '
          f'{uz['boyi']}, '
          f'{uz['yashash joyi']}, ')
