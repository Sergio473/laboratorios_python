#Sergio Abisay Cervantes Sánchez 
#20/junio/22

year = int(input("Introduce un año: "))

if year<1582:
    print("No dentro del período del calendario Gregoriano")
else: 
    if not(year % 4 ==0):
        print("año comun")
    elif not(year % 100==0):
        print("año bisiesto")
    elif not(year%400==0):
        print("año comun")
    else:
        print("año bisiesto")
