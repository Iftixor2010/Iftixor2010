mevalar=[ ' ', 'olma', 'anor', 'anjir', 'uzum']
c=int(input('kiriting: '))

try:
    print(mevalar[c])
except IndexError:
    print(f'royxatda {len(mevalar)}ta meva bor xolos')



