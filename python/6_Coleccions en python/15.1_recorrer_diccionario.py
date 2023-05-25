diccionario = {
    "IDE": 'Integrade Development Environment',
    "OPP": "object Orientad Prrograming",
    "DBMS":"Database Management Sytem" 
    
}

for termino, valor in diccionario.items():
    print(termino, valor)
print("\n")


for termino in diccionario.keys():
    print(termino)
    
for valores in diccionario.values():
    print(valores)