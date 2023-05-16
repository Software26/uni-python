#-----------------------------------------------------------#
# Se solicita la siguiente informacion acerca de un libro:   #
#Titulo, Autor                                              #
#Debes imprimir la informacion en el siguiente formato      #
#Proporciana el tutulo                                      #
#porporciona el Autor                                       #
#<Titulo> fue escrito:<autor>                               #
#-----------------------------------------------------------#
print("Se solicita informacion del libro que esta leyendo")

titulo = str(input("Digite el Nombre del Libro: "))

autor = str(input("Digite cual es el Autor: "))
print("\n")

print("El nombre del libro es: ", titulo)
print("El Autor es: ", autor)
print("\n")

print(titulo, "Fue escrito por: ", autor)