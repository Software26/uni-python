nombres = ['Juan','Karla','Ricardo', 'María']

#----Insert element---
nombres.insert(1, "Octavio")
print(nombres)

#--Remove un elemento--
nombres.remove("Octavio")
print(nombres)

#remueve el ultimo valor agregado
nombres.pop()
print(nombres)