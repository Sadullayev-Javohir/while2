"""Ekrandan sonlar kiritiladi masalan 5 yoki 10 ta shu sonlarni yig'indisini chiqaring"""

uzunlik = int(input("Nechta son kiritasiz: "))
add = 0
i = 0

while i < uzunlik:
    k = int(input('k sonini kiriting: '))
    add += k
    i += 1
print(add)