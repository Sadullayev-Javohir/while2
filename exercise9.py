"""Ekrandan son kiritilsa shu son 2 ning darajasi bo'lsa darajasi aks holda darajasi emas kabi so'zlarni
 chiqaring"""

num = int(input("son kiritinging: "))
check = False
k = 1
text = ''

while k <= num:
    if k == num:
        text = f'{num} 2 ning darajasi'
    else:
        text = f'{num} 2 ning darajasi emas'
    k += k
print(text)