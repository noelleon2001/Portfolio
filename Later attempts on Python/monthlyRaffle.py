n = int(input(""))
d = 0
while n > 0:
    n = n//10
    d = d + 1
    print("n,d", n,d)
if d != 6:
    print("Invalid entry")
else:
    print("Entry accepted")