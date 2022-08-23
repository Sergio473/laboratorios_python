#Sergio Abisay Cervantes Sánchez 
#20/agosto/22

beatles = []
# paso 1
print("Paso 1:", beatles)

# paso 2
beatles.append("John")
beatles.append("Paul")
beatles.append("George")
print("Paso 2:",beatles)

# paso 3
print("Paso 3:", beatles)
for member in range(2):
    beatleName= input("new beatle name: ")
    beatles.append(beatleName)

# paso 4
del beatles[3:5]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
