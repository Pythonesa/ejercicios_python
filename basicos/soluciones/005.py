venta1 = float(input("Ingresa la primer venta: "))
venta2 = float(input("Ingresa la segunda venta: "))
venta3 = float(input("Ingresa la tercer venta: "))

if venta1 > venta2 and venta1 > venta3:
    print("La primer venta fue la mayor.")
elif venta2 > venta1 and venta2 > venta3:
    print("La segunda venta fue la mayor.")
else:
    print("La tercer venta fue la mayor.")

if venta1 < venta2 and venta1 < venta3:
    print("La primer venta fue la menor.")
elif venta2 < venta1 and venta2 < venta3:
    print("La segunda venta fue la menor.")
else:
    print("La tercer venta fue la menor.")

total = venta1 + venta2 + venta3
print(f"El total de las ventas es: {total}")
print(f"El promedio de las ventas es: {total / 3}")