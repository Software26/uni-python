diccionario = {
    "IDE": 'Integrade Development Environment',
    "OPP": "object Orientad Prrograming",
    "DBMS":"Database Management Sytem" 
    
}

print (diccionario)

#largo
print(len(diccionario))

#acceder a un elemento (Key)
print(diccionario["IDE"])

#otra forma de recuperacion un elemento
print(diccionario.get("OPP"))

#midifidicacion de elementos 
diccionario["IDE"] = "Integrasjdjsljd"
print(diccionario)