"""List berilgan x = [1,23,10,45,-41,56,78,13] shu listning juft va toq elementlarini
 2 ta alohida listga yuklang. juft = [10,56, 78]. toq = [1,23,45,-41,13]"""

x = [1,23,10,45,-41,56,78,13]
i = 0
toq = []
juft = []

while i < len(x):
    if x[i] % 2 == 0:
        juft.append(x[i])
    else:
        toq.append(x[i])
    i += 1

print(f"Juft sonlar:{juft}")
print(f"Toq sonlar: {toq}")