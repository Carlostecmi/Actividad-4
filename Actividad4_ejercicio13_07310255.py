print("Ejercicio 13: Cotizaciones de un proveedor")
print("Nombre: Carlos Noel Vazquez Banda")
print("Matrícula: 07310255")
print()

# Presupuesto máximo que autorizó Finanzas
presupuesto = 5000

# Lista vacía donde guardamos las 5 cotizaciones
cotizaciones = []
for numero_de_cotizacion in range(5):
    precio_cotizado = int(input("Precio de la cotización: "))
    cotizaciones.append(precio_cotizado)

total_cotizaciones = len(cotizaciones)
print()
print("Cotizaciones como llegaron:", cotizaciones)

# Algoritmo de ordenamiento burbuja (Bubble Sort)
for vuelta in range(total_cotizaciones - 1):
    for lugar in range(total_cotizaciones - 1 - vuelta):
        precio_izquierda = cotizaciones[lugar]
        precio_derecha = cotizaciones[lugar + 1]
        
        # Si la de la izquierda es mayor (más cara), intercambian posición
        if precio_izquierda > precio_derecha:
            cotizaciones[lugar] = precio_derecha
            cotizaciones[lugar + 1] = precio_izquierda
            
    # Mostramos cómo va quedando la lista al finalizar cada vuelta
    print(f"Después de la vuelta {vuelta + 1}: {cotizaciones}")

print()
print("===== RESULTADO FINAL =====")
print("Cotizaciones de la más barata a la más cara:", cotizaciones)
print("💰 La cotización más barata es:", cotizaciones[0])
print("💸 La cotización más cara es:", cotizaciones[-1])

# Revisamos si la más barata cabe en el presupuesto
if cotizaciones[0] <= presupuesto:
    print("✅ Se aprueba la compra con la cotización de", cotizaciones[0])
else:
    print("🛑 Ninguna cotización cabe en el presupuesto. Pide nuevas cotizaciones.")
    