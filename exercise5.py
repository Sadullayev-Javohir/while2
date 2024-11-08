"""Ekrandan sonlar kiritiladi masalalan 5 yoki 10 ta shun sonlarni kattasini chiqaring"""

uzunlik = int(input("Nechta son kiritasiz: "))
add = 0
i = 0

while i < uzunlik:
    k = int(input("k sonini kiriting: "))
    if add < k:
        add = k
    i += 1
print(f"Katta son: {add}")