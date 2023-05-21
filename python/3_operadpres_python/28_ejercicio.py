"""
Intrucciones de tareas:

Solitar al usuario dos valores, y determinar cual numero es el mayor
Solicitar al usuario dos valores:

numero(int)
numero(int)

se debe imprimir el mayor de los dos numeros (la lida debe ser identificada a la que sigue):

Proporcina el numero1
Proporciona el numero 2

eEl numero es <Numero/Mayor>    
    
 """
print("###############################################################")
print("###############Indetentificar el numero mayor###################")
print("################################################################")

numero1 = int(input("Digite el primer numero "))
numero2 = int(input("Digite el segundo numero "))

if numero1 > numero2:
    print(f"Es el numero mayor: {numero1}")

elif numero1 == numero2:
    print(f"Los numeros iguales")
    
else:
    print(f"Segundo numero es mayorn{numero2}")


 