"""List berilgan listning ichida biz qidirgan element bor yoki yoqligni tekshirirng bor bo'lsa True aks
holda False chiqaring"""

numList = [12, 35, 64, 12, 6, 90, 78]
number = int(input("n sonini kiriting: "))
i = 0
check = False

while i < len(numList):
    if numList[i] == number:
        check = True
    else:
        check
    i += 1
print(check)