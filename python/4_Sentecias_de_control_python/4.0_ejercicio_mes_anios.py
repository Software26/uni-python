mes = int(input("Proporciona mes del año (1-12) "))

estacion = None

if mes >= 1 and mes <= 12:
    if mes == 1 or mes == 2 or mes == 12:
        estacion = "Invierno"
        print(f"Para el mes {mes} la estacion es: {estacion}")
    elif mes ==3 or mes == 4 or mes == 5:
        estacion = "Primavera"
        print(f"Para el mes {mes} la estacion es: {estacion}")
    elif mes == 6 or mes == 7 or mes == 8:
        estacion = "Verano"
        print(f"Para el mes {mes} la estacion es: {estacion}")
    elif mes == 9 or mes == 10 or mes == 11:
        estacion = "Otoño"
        print(f"Para el mes {mes} la estacion es: {estacion}")
else: 
    print(f"El numero del {mes} que se digito no aplica tiene que ser (1-12)")