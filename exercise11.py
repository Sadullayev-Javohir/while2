"""Ekrandan son kiritiladi shu sonning faktorialini chiqaring"""

num = int(input("son kiriting: "))
factorial = 1
k = 0

while k < num:
    k += 1
    factorial *= k
    
print(f"{num} ning faktoriali {factorial}")