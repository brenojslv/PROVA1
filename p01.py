a = int(input(" Digite o primeiro número:"))
b = int(input(" Digite o segundo número:"))
c = int(input(" Digite o terceiro número:"))

if (a >= b >= c):
    print("A ordem dos números é:", a, b, c)
elif (a >= c >= b):
    print("A ordem dos números é:", a, c, b)
elif (b >= a >= c):
    print("A ordem dos números é:", b, a, c)
elif (b >= c >= a):
    print("A ordem dos números é:", b, c, a)
elif (c >= a >= b):
    print("A ordem dos números é:", c, a, b)
else:
    print("A ordem dos números é:", c, b, a)