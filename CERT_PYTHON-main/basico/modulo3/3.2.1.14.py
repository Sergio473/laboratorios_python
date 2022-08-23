#Sergio Abisay Cervantes Sánchez 
#20/agosto/22
blocks = int(input("Ingresa el número de bloques: "))

height = 0
while blocks > height:
    height = height + 1
    blocks = blocks - height

print("La altura de la pirámide:", height)
