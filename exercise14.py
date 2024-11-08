"""List berilgan cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"] berilgan list
 elementlari ichidan eng uzun so'zni toping va uni ekranga chiqaring"""

cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"]
i = 0
maximum = cars[0]

while i < len(cars):
    if len(cars[i]) > maximum:
        maximum = cars[i]
    i += 1
print(maximum)

