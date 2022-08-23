#Sergio Abisay Cervantes Sánchez 
#20/agosto/22
c0 = int(input("ingresa un numero:"))

if c0 < 1:
    print("use a non-negative")
    exit

steps = 0
while c0 !=1:
    if c0 % 2 == 0:
        c0 = int(c0 /2)
    else:
        c0 = 3 *c0 +1
    print(c0)
    steps +=1
print("Total", steps)