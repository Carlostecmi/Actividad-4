print("Ejercicio 3: ¿Se puede exportar el producto?")
print("Nombre: Carlos Noel Vazquez Banda")
print("Matrícula: 07310255")
print()

# Pedimos los datos del producto y del destino
producto = input("¿Qué producto vas a exportar?: ")
respuesta1 = input("¿Está en la lista de restringidos? (si/no): ")
respuesta2 = input("¿La empresa tiene permiso especial? (si/no): ")
respuesta3 = input("¿El permiso está vigente? (si/no): ")
respuesta4 = input("¿El país destino tiene restricciones comerciales? (si/no): ")
kilos = float(input("¿Cuántos kilos vas a enviar?: "))

# Convertimos las respuestas en True o False (agregamos .lower() por seguridad)
restringido = respuesta1.lower() == "si"
tiene_permiso = respuesta2.lower() == "si"
permiso_vigente = respuesta3.lower() == "si"
destino_restringido = respuesta4.lower() == "si"

# Un permiso solo sirve si existe Y está vigente
permiso_valido = tiene_permiso and permiso_vigente

print()
print("===== REVISIÓN DE CUMPLIMIENTO =====")

# Evaluamos si se puede exportar con una variable de control
se_puede = (not restringido or permiso_valido) and not destino_restringido

if se_puede:
    print("✅", producto, "se puede exportar.")
    
    # Si además es restringido y pesa más de 1000 kg, agregamos la inspección
    if restringido and kilos > 1000:
        print("🔍 Por ser restringido y pesar más de 1000 kg, necesita inspección previa.")
else:
    print("🛑", producto, "NO se puede exportar.")

    # Explicamos el motivo exacto del rechazo
    if destino_restringido:
        print("Motivo: el país destino tiene restricciones comerciales.")
    elif restringido and not tiene_permiso:
        print("Motivo: el producto está restringido y no hay permiso especial.")
    elif restringido and not permiso_vigente:
        print("Motivo: el permiso especial está vencido. Hay que renovarlo.")
        