edad = input("Que edad tiene?:\n")

edad = int( edad)

if edad < 4 :
    print("Gratis")
elif  4 <= edad <= 18:
    print("Pagar 3€")
else:
    print("Pagar 4€")