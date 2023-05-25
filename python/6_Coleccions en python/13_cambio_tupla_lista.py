frutas =("Naranja", "Platano","Guyaba")

frutasLista = list(frutas) # cambio de tuplas a lista
print(frutas)

frutasLista[0] = "Pera" #agregando un valor a la lista
print(frutasLista)

frutas = tuple(frutasLista)# Combirtiendo a una tupla la lista
print(frutas)

del frutas
print(frutas, "elimino la tupla")



