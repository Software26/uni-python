"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor incorrecto
Por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""
print("############################################################")
print("################ Calificaciones ############################")
print("############################################################\n")
print("------------------- Digite un valor -----------------------------------")
numero = float(input("Proporcione un valor entre 0 y 10: "))

resultado = ""
if numero >= 9 and numero  <= 10:
    resultado = "A"
    
elif numero >= 8 and numero < 9:
    resultado = "B"
    
elif numero >= 7 and numero < 8:
    resultado = "C"

elif numero >=6 and numero < 7:
    resultado = "D"

elif numero >= 0 and numero < 6:
    resultado = "F"
else :
    resultado = "Valor incorrecto"
print(f"La calificacion obtenida es: {resultado}")