#Sergio Abisay Cervantes Sánchez 
#20/junio/22

income = float(input("Introduce el ingreso anual:"))

if income<=85528:
    tax=0.18*income - 556.0
else:
    tax=income+14839.02*0.32

tax = round(tax, 0)
if tax<0:
    tax=0.0
print("El impuesto es:", tax, "pesos")