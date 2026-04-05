def cifrado_cesar_A1(texto, clave, modo="cifrar"):
    resultado = ""

    if modo == "descifrar":
        clave = -clave

    for char in texto:
        if char.isalpha():
            # Convertir a mayúscula para simplificar
            mayus = char.upper()

            # A=1 → convertimos A→1, B→2,... Z→26
            valor = ord(mayus) - ord('A') + 1

            # Aplicar desplazamiento
            nuevo_valor = (valor + clave - 1) % 26 + 1

            # Convertir de nuevo a letra
            nueva_letra = chr(nuevo_valor - 1 + ord('A'))

            # Mantener minúsculas si corresponde
            if char.islower():
                nueva_letra = nueva_letra.lower()

            resultado += nueva_letra
        else:
            resultado += char

    return resultado


# ----------- INTERFAZ -----------
print("=== CIFRADO CÉSAR  ===")

texto = input("Texto: ")
clave = int(input("Clave: "))
modo = input("¿cifrar o descifrar?: ").lower()

resultado = cifrado_cesar_A1(texto, clave, modo)

print("\nResultado:", resultado)