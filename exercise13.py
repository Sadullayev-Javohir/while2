"""Ekrandan biror son kiritilsa shunga mos holda karra jadvalini chiqaring
son = 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15"""

num = int(input("Son kiriting: "))
i = 1
x = 0

while i <= 10:
    print(f"{num} * {i} = {x}")
    i += 1
    x = num * i
