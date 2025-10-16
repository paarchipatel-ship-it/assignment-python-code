n = int(input("enter a num: "))
for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, " ")
        num = num *(i - j) // (j + 1)
        print(n)
