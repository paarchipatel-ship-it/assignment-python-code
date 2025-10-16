num = int(input("enter no of test cases: "))
for i in range(num):
    x = int(input("enter 1st num: "))
    y = int(input("enter 2nd num:"))
    a = x
    b = y
    while b != 0:
        r = a % b
        a = b
        b = r
        gcd_val = a
        lcm_val = (x * y) // gcd_val
        print("GCD=", gcd_val)
        print("LCM =", lcm_val)