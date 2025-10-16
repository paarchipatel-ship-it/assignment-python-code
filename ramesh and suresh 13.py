N = int(input("enter a num: "))
used = 0
i = 1
while True:
 if used + i >= N:
    print("ramesh")
    break
 
used += i

if used + 2 * i >= N:
    print("suresh")

used += 2 * i
i += 1
