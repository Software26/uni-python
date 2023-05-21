num = int(input("Prorcione un numero de 1 al 3: "))

numtxt = ""
if num == 1:
    numtxt = "Numero uno"
elif num == 2:
    numtxt = "Numero dos"
elif num == 3:
    numtxt = "Numero tres"
else:
    print("Valor fuera de Rango")
print(f"Numero Proporciando: {num} - {numtxt}")