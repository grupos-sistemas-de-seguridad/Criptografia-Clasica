def cifrado_cesar_manual(texto, clave, modo="cifrar"):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""

    if modo == "descifrar":
        clave = -clave

    for char in texto:
        if char.upper() in alfabeto:
            # A=1, B=2...
            indice = alfabeto.index(char.upper()) + 1  

            # Aplicar fórmula A=1 correctamente
            nuevo_indice = (indice + clave - 1) % 26 + 1  

            # Volver a índice de lista (0–25)
            nueva_letra = alfabeto[nuevo_indice - 1]

            if char.islower():
                nueva_letra = nueva_letra.lower()

            resultado += nueva_letra
        else:
            resultado += char

    return resultado


# -------- INTERFAZ --------
texto = input("Texto: ")
clave = int(input("Clave: "))
modo = input("cifrar/descifrar: ")

print("Resultado:", cifrado_cesar_manual(texto, clave, modo))