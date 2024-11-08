"""Ekrandan son kiritilsa shu son 2 ning darajasi bo'lsa nechanchi darajasi 
ekanligini aks holda darajasi emas kabi so'zlarni chiqaring"""

num = int(input("son kiritinging: "))
check = False
k = 1
text = ''
count = 0

while k <= num:
    if k == num:
        text = f'{num} 2 ning darajasi va \n {num} => {count} ning darajasi'
    else:
        text = f'{num} 2 ning darajasi emas'
    count += 1
    k += k
print(text)