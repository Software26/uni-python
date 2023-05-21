valor = int(input("escribe el valor: "))
valorMinimo = 0
valorMaximo = 5

dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)

if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
    
else:
    print(f"El valor {valor} esta fuera del rango")