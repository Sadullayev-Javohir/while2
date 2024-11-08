"""
List yarating hosil bolgan listning har bir elementiga 2 ni ko'paytirib ekranga chiqaring"""

numList = [12, 4, 64, 1, 6]
numList2 = []
i = 0
pow = 1

while i < len(numList):
    print(pow)
    pow = 2 * numList[i]   
    numList2.append(pow)
    i += 1
print(numList2)