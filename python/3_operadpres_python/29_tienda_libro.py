print("###############################################################")
print("###################   Tienda Producto #########################")
print("###############################################################\n")

print("Propocione los siguientes datos del libro: ")
nombreLibro = (input("Propociona el nombre: "))
idlibro = int(input("Propociona el ID: "))
precio = float(input("Propocina el precio: (Formato decimal) "))
indicacion = str(input("Indica si el envio es gratuito (True/False) "))

if indicacion == True:
    indicacion = "True"

elif indicacion == False:
    indicacion = "False"
else:
    indicacion =  "El valor es incorrecto Favor de digitar True/False"
print("-----------------------------------------------------------")
print(f"Nombre: {nombreLibro}")
print(f"Id: {idlibro}")
print(f"Precio: {precio}")
print(f"Envio Gratuito: {indicacion}")
print("-----------------------------------------------------------")
