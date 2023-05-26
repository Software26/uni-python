diccionario = {
    "IDE": 'Integrade Development Environment',
    "OPP": "object Orientad Prrograming",
    "DBMS":"Database Management Sytem" 
    
}

# comprobar existencia de algun elemento
print('IDE' in diccionario)
print(diccionario)

for termino, valor in diccionario.items():
    print(termino, valor)
    