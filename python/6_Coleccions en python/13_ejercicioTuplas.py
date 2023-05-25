# Dada la siguiente tupla, 
# crear una lista que sólo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)

lista= []#definir lista

for elemento in tupla: #filtamos los element de la tupla
    if elemento < 5:
        lista.append(elemento)# combinamos lista con t usando append()

print(lista)      


