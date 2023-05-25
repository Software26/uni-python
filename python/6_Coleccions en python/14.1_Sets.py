planeta = {"Marte", "Venus","Jupiter"}
print(planeta)

#eliminando un elemento
planeta.remove("Jupiter")
print(planeta,"\n")

#Eliminar elemento posiblemente sin arrojando un error
planeta.discard("Marte")
print(planeta)

#limpiar set
planeta.clear()
print(planeta)

#Eliminar
del planeta
print(planeta)