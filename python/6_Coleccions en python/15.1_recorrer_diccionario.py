diccionario = {
    "IDE": 'Integrade Development Environment',
    "OPP": "object Orientad Prrograming",
    "DBMS":"Database Management Sytem" 
    
}
 #recojer elemento
for termino, valor in diccionario.items():
    print(termino, valor)
print("\n")
#recoje las llaves
for termino in diccionario.keys():
    print(termino)
    
for valores in diccionario.values():
    print(valores)