a = int(input(" enter a num: "))
b = int(input(" enter a num: "))
c = int(input(" enter a num: "))
if(a >= b and a >=c):
    print("first num is max", a)
elif(b >= c):
    print("second num is max", b)
else:
    print(" third num is max", c)