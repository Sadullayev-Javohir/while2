"""Barcha 3 - xonali sonlar ichida raqamlari yi'gindisi 5 dan katta va 8 dan kichik bo'lganlarini ekranga
 chiqaring"""

start = 100
end = 999
first = 0
second = 0
third = 0

while start <= end:
    first = start // 100
    second = (start // 10) % 10
    third = start % 10
    
    if first + second + third > 5 and first + second + third < 8:
        print(start)
    
    start += 1