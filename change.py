i = input("Please enter an amount in cents less than a dollar")
quarter = 25
dime = 10
nickel = 5
penny = 1
i = int(i)
print("Your change will be:")
if i>=25:
    q = int(i/quarter)
    i = i % quarter
    print("Q: ", q)
if i>=10:
    d = int(i/dime)
    i = i % dime
    print("D: ", d)
if i>=5:
    n = int(i/nickel)
    i = i % nickel
    print("N: ", n)
if i>0:
    p = int(i/penny)
    i = 0
    print("P: ", p)