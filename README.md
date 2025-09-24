# Parcial 2 Fundamentos

## Ejercicio-1
> Un programa debe clasificar un número entero ‘n’ según dos criterios.
> Si ‘n’ es positivo, debe imprimir 'Positivo y Par' o 'Positivo e Impar'.
> Si ‘n’ es negativo, debe imprimir 'Negativo y Par' o 'Negativo e Impar'.
> Si ‘n’ es 0, debe imprimir 'El número es cero'.


```python
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
```

## Ejercicio-2
> Un programa de gestión de inventario tiene que clasificar un producto.
> La clasificación depende del stock actual y de si el producto es perecedero.
> Si el producto es perecedero y el stock es menor a 10, la clasificación es 'Riesgo Crítico'.
> Si el stock es menor a 50 (sin importar si es perecedero o no), la clasificación es 'Bajo Stock'.
> Si el stock es 50 o más y el producto no es perecedero, la clasificación es 'Stock Normal'.

```python
producto = input("Ingrese el nombre del producto: ")
stock = int(input("Ingrese la cantidad en stock: "))
perecedero = input("¿El producto es perecedero? (si/no): ")

if perecedero == "si" and stock < 10:
    print(f"El stock del producto {producto} esta en Riesgo Crítico")

elif stock < 50:
    print(f"El producto {producto} tiene Bajo Stock")

else:
    stock >= 50 and perecedero == "no"
    print(f"El producto {producto} tiene Stock Normal")
```
## Ejercicio-3 
> Se te pide escribir un programa que, dado un mes (como un número del 1 al 12) y un año, imprima el número de días en ese mes.
> Debes validar la entrada para asegurarte de que el mes es válido.

``` python
mes = int(input("Ingrese un mes solo digite numeros del 1 al 12: "))
año = int(input("Ingrese un año: "))
print(f"El numero de mes digitado es {mes} ")
print(f"El año digitado es el: {año}")
print("El nombre y numero de dias del mes digitado es: ")
match mes:
    case 1:
        print("Enero tiene 31 días")
    case 2:
        print("Febero tiene 28 días")
    case 3:
        print("Marzo tiene 31 días")
    case 4:
        print("Abril tiene 30 días")       
    case 5:
        print("Mayo tiene 31 días")
    case 6:
        print("Junio tiene 30 dias")
    case 7:
        print("Julio tiene 31 días")
    case 8:
        print("Agosto tiene 31 días")
    case 9:
        print("Septiembre tiene 30 días")
    case 10:
        print("Octubre tiene 31 días")
    case 11:
        print("Noviembre tiene 30 días")
    case 12:
        print("Diciembre tiene 31 días")
```
