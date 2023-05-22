#propociona tu edad:

# 0-10: la infanci es increible...
# 10-20: Muchos cambios y mucho estudio...
#20-30: Amor y comiena el trabajo

#Cualquier otro valor : Etapa de vida no reconocida

edad = int(input("propociona tu edad: "))
if edad >=0 and edad < 10:
    print(" la infancia es increible...")
    
elif edad >=10 and edad < 20:  
    print("Muchos cambios y mucho estudio...")

elif edad >=20 and edad <30:
    print("Amor y comiena el trabajo")
    
else:
    print("Etapa de vida no recocida")