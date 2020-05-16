precio = 3.49
descuento = 0.4

precio_con_descuento = precio * descuento

numero_de_barras = int(input("Intro num de barras:\n")) #Input siempre guarda lo pasado como cadena

print("Precio habitual de la barra " + str(precio) )
print("Precio con descuento de la barra " + str(precio_con_descuento) )
print("Coste total = " + str(numero_de_barras * precio_con_descuento))