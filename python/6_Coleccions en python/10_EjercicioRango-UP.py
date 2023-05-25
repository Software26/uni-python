# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
print("-----------Rango del 0 al 10 con for------------------------")
for result in range(0,11):
    if result % 3 == 0:
        print(result,"For")
else:
    print("Fin de la busqueda con for ")
    
    
    
#------------------------------------------------------------------------
print("-----------Rango del 0 al 10 con While------------------------") 
contador1 = 0
while contador1 <= 10:
    contador1 += 1
    if contador1 % 3 == 0:
        print(contador1,"While")
else: 
    print("Fin del While del Rango 0 al 10 ")   
    
############################################################################################33

# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimelos
for result in range(2,7):
    print( result,"For")
    
else:
    print("Fin del rango1")
    
#--------------------------------------------------------------------------------------

print("-----------Rango del 2 al 6con While------------------------") 
contador2 = 2
while contador2 <= 6:
    contador2 += 1
    print(contador2)
else: 
    print("Fin del While del Rango 2 al 6 ")  
    
########################################################################################

# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1
#---------------------------------------------
print("---------Rango con For de 2 en 2 ----------")
for result in range(2,7,2):
    print( result)
    
else:
    print("Fin del rango con for 2 en 2 \n")
#---------------------------------------------
print("---------Rango con While de 2 en 2 ----------")
contador = 3
while contador <= 10:
    print(contador)
    contador += 2
else:
    print("Fin del rango")
    
    
