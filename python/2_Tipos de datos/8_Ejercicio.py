var1 = int(input("como estuvo tu dia (1 al 10) "))

if var1 <= 3:
    print("Tu dia no estuvo muy bien")
    
elif var1 <= 5 :
    print("Tu dia no estuvo tan mal")
    
elif var1 <= 8:
    print("Tu dia fue genial")
    
else:
    print("Tu dia fue exelente")

print("*Tu dia estuvo de: ", var1,"*")