import csv

# Ruta al archivo CSV
ruta_archivo = "clientes.csv"

# Lista para guardar solo los clientes suscritos
clientes_suscritos = []

# Leer archivo CSV
with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)

    print("📋 Lista completa de clientes:\n")
    for fila in lector:
        print(
            f"🔹 {fila['Nombre']} | Edad: {fila['Edad']} | Email: {fila['Email']} | Suscrito: {fila['Suscrito']}")

        if fila["Suscrito"].strip().lower() == "sí":
            clientes_suscritos.append(fila)

# Guardar solo los clientes suscritos en un nuevo CSV
with open("Data/clientes_suscritos.csv", mode="w", newline='', encoding='utf-8') as archivo_nuevo:
    campos = ["Nombre", "Edad", "Email", "Suscrito"]
    escritor = csv.DictWriter(archivo_nuevo, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(clientes_suscritos)

print("\n✅ ¡Archivo 'clientes_suscritos.csv' generado con éxito!")
