"""Mukammal son yoki Mukammal son emasligini tekshiring. Mukammal sonlar o'zidan tashqari bo'luvchilarini
yig'indisi o'ziga teng. Masalan : 28 -> 1,2,4,7,14 shu sonlarning yigindisi 28 ga teng"""

n = int(input("n sonini kiriting: "))

i = 1
add = 0
text = ''

while i < n:
    
    if n % i == 0:
        add += i
        if add == n:
            text = f"Bo'luvchilar soni: {add} -> {n}"
        else:
            text = f"Bo'luvchilar soni: {add} != > {n}"
    i += 1
print(text)