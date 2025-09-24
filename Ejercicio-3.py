# Se te pide escribir un programa que, dado un mes (como un número del 1 al 12) y un año, 
# imprima el número de días en ese mes. 
# Debes validar la entrada para asegurarte de que el mes es válido. 

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