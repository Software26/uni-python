#program que me diga todos los rango

edad = int(input("Digite su edad: "))

veinte = (edad >=20) and (edad < 30)
treite = (edad >= 30) and (edad <40 )
cuareta  = (edad >=40)and (edad <50)
cincuenta = (edad >=40)and (edad <50)

if veinte == True:
    print(f" Su edad es {edad} esta en rango de lo veiinte anios")
elif treite == True:
    print(f" Su edad es {edad} esta en rango de lo 30 anios")
elif cuareta == True:
    print(f" Su edad es {edad} esta en rango de lo 40 anios")
elif cincuenta == True: 
    print(f" Su edad es {edad} esta en rango de lo 50 anios")
else:
    print("Su edad no esta en ningun de los rango")