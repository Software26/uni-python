valor = int(input("Escribe el valor: "))
valorMInimo = 0
valorMaximo = 5

dentroRango =(valor >= valorMInimo)and (valor<= valorMaximo)

if (dentroRango == True):
    print("Esta de tro del rango")
    
else: 
    print("Esta fuera del rango")