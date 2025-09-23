# Se pide crear un programa para un sistema de descuentos en una tienda en línea. 
# El descuento del 10% se aplica si un cliente es un 'miembro_vip' y su compra total es mayor a $100. 
# Adicionalmente, se aplica un descuento del 5% si el cliente no es 'miembro_vip' pero su compra total es mayor a $200. 
# En cualquier otro caso, no hay descuento. 


miembro_vip = (input("digite si es mienbro VIP o no: "))
compra_total = float(input("digite el total de su compra: "))
descuento = 0

#Descuentos

if miembro_vip == "si" and compra_total > 100:
    descuento = 0.10
elif miembro_vip == "no" and compra_total > 200:
    descuento = 0.05

total_con_descuento = compra_total * (1 - descuento)

print(f"El descuento aplicado es de: {descuento*100}%")
print(f"El total de su compra con descuento es de: ${total_con_descuento}")
print("Gracias por comprar en nuestra tienda en linea doña pepa")