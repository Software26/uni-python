#---------------------------------------------------------------------------#
# Instrucciones de la tarea                                                 #
#                                                                           #
#El el siguinete ejercicio se solicita calcular el area y el perimetro      #
#de un rectagulo para elos debemos crear las siguiente variable:            #
#                                                                           #
#alto (int)                                                                 #
#ancho (int)                                                                #
#                                                                           #
#El usrio debe de proposionar los valores de largo y ancho                  #
#y despues se debe imprimir el resultado en el siguiente formato            #
#---------------------------------------------------------------------------#
print("####################################")
print("#Calcular el area de un rectangulo #")
print("####################################\n")
base = int(input("Digite la base: "))
altura = int(input("Digite la altura "))

result =  base * altura
perimetro =  ((base*altura)/2)


print('###############Resultado################\n')
print(f"La base digitida fue de: {base}")           
print(f"La altura digiitada fue de: {altura}")
print(f"Esta es el area del rectagulo: {result}")
print(f"El perimetro del rectagulo es: {perimetro}")
print("\n ")
print(f"#######################################")