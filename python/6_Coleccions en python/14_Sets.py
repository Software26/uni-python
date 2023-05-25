planeta = {"Marte", "Venus","Jupiter"}
print(planeta)

#largo
print(len(planeta))

#revisar elemento presente en el set
print("Marte" in planeta)
print("Tierra" in planeta)

#agregar elementos 
planeta.add("Tierra")
print(planeta)

#no se peude agregar elementos Duplcados
planeta.add("Venus")
print(planeta)