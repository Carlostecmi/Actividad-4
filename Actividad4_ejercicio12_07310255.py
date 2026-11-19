print("Ejercicio 12: Precios del buen fin")
print("Nombre: Carlos Noel Vazquez Banda")
print("Matrícula: 07310255")
print()

# Listas de ejemplo para que el script esté completo
productos = ["Pantalla", "Laptop", "Tenis", "Celular", "Bocina"]
precios = [8000, 15000, 20000, 12000, 3000]
promocion = [6000, 12000, 0, 9000, 0]  # 0 indica que no entra en promoción
productos_promo = ["Pantalla", "Laptop", "Celular"]

pais = "MEXICO"
paises_tmec = ["MEXICO", "ESTADOS UNIDOS", "CANADA"]
meses = 3
ventas = [120, 95, 140, 160, 110, 175]
consulta = "Laptop"

# in: ¿el país destino está en el T-MEC?
if pais in paises_tmec:
    print("🌍", pais, "está en el T-MEC: arancel 0%.")
else:
    print("📄", pais, "no está en el T-MEC: se cobra el arancel general.")

print()
print("===== REPORTE DE VENTAS DEL CLIENTE =====")

# or: los meses deben estar entre 1 y 6
if meses < 1 or meses > 6:
    print("❌ Escribe un número de meses entre 1 y 6.")
else:
    # Rebanada sin inicio: los primeros 'meses' meses
    print("Primeros", meses, "meses:", ventas[:meses])

    # Rebanada con número negativo: los últimos 'meses' meses
    print("Últimos", meses, "meses:", ventas[-meses:])

    # Rebanadas fijas: los dos trimestres del semestre
    print("Primer trimestre:", ventas[0:3])
    print("Segundo trimestre:", ventas[3:6])

print()
print("===== PRODUCTO MÁS CARO EN PROMOCIÓN =====")
# 4. Busca el producto más caro de la promoción
mayor = promocion[0]
pos_mayor = 0
for i in range(len(promocion)):
    if promocion[i] > mayor:
        mayor = promocion[i]
        pos_mayor = i
print("⭐ El producto en promoción más caro es ", productos_promo[pos_mayor if pos_mayor < len(productos_promo) else 0], " a $", mayor, sep="")

print()
print("===== CONSULTA DEL CLIENTE =====")

# 5. Si el producto NO está en el catálogo, avisa al cliente
if consulta not in productos:
    print("❌", consulta, "no está en nuestro catálogo.")
else:
    # Buscamos la posición del producto en el catálogo
    pos = -1
    for i in range(len(productos)):
        if productos[i] == consulta:
            pos = i
    print("Precio normal de ", consulta, ": $", precios[pos], sep="")

    # 6. Revisa si el producto está en la lista de productos en promoción (si su precio promo es mayor a 0)
    if promocion[pos] > 0:
        print("🎉 Precio Buen Fin: $", promocion[pos], sep="")
    else:
        print("🏷️", consulta, "no entra a la promoción. Se cobra el precio normal.")