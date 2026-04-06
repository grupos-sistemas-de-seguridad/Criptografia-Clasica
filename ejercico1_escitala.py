import math

def descifrar(cifrado, diametro):
    # Determinamos cuántas filas tendría la vara
    columnas = math.ceil(len(cifrado) / diametro)
    resultado = [""] * columnas
    for i in range(len(cifrado)):
        resultado[i % columnas] += cifrado[i]
    return "".join(resultado)

# --- INICIO DEL ATAQUE ---
mensaje_enemigo = "ERTJCOEI" # Ejemplo de tu informe
print(f"Analizando mensaje: {mensaje_enemigo}")

for d in range(2, len(mensaje_enemigo)):
    intento = descifrar(mensaje_enemigo, d)
    print(f"Probando Diámetro {d}: {intento}")
