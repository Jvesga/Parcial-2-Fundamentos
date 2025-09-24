# Un programa debe clasificar un número entero ‘n’ según dos criterios. 
# Si ‘n’ es positivo, debe imprimir 'Positivo y Par' o 'Positivo e Impar'. 
# Si ‘n’ es negativo, debe imprimir 'Negativo y Par' o 'Negativo e Impar'. 
# Si ‘n’ es 0, debe imprimir 'El número es cero'.


numero = int(input("Ingrese un número entero: "))
print(f"El numero digitado es : {numero}")

if numero > 0 and numero % 2 == 0:
    print("El numero digitado es : Positivo y Par")
elif numero > 0 and numero % 2 != 0:
    print("El numero digitado es : Positivo e Impar")

if numero < 0 and numero % 2 == 0:
    print("El numero digitado es : Negativo y Par")

elif numero < 0 and numero % 2 != 0:
    print("El numero digitado es : Negativo e Impar")
    
if numero == 0:
    print("El número digitado es cero")