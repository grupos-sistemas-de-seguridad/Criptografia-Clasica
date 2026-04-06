Codificador

def rail_fence_encrypt(texto, rieles):
    cercas = ['' for _ in range(rieles)]

    direccion_abajo = False
    fila = 0

    for letra in texto:
        cercas[fila] += letra

        if fila == 0 or fila == rieles - 1:
            direccion_abajo = not direccion_abajo

        fila += 1 if direccion_abajo else -1

    return ''.join(cercas)

mensaje = "holamundo"
rieles = 3

resultado = rail_fence_encrypt(mensaje, rieles)
print(resultado)

Decodificador

def rail_fence_decrypt(cipher, rieles):
    matriz = [['' for _ in range(len(cipher))] for _ in range(rieles)]

    # Paso 1: marcar el patrón zig-zag
    direccion_abajo = None
    fila, col = 0, 0

    for i in range(len(cipher)):
        if fila == 0:
            direccion_abajo = True
        if fila == rieles - 1:
            direccion_abajo = False

        matriz[fila][col] = '*'
        col += 1
        fila += 1 if direccion_abajo else -1

    # Paso 2: llenar con el texto cifrado
    indice = 0
    for i in range(rieles):
        for j in range(len(cipher)):
            if matriz[i][j] == '*' and indice < len(cipher):
                matriz[i][j] = cipher[indice]
                indice += 1

    # Paso 3: leer en zig-zag
    resultado = []
    fila, col = 0, 0

    for i in range(len(cipher)):
        if fila == 0:
            direccion_abajo = True
        if fila == rieles - 1:
            direccion_abajo = False

        resultado.append(matriz[fila][col])
        col += 1
        fila += 1 if direccion_abajo else -1

    return "".join(resultado)


# Ejemplo
cifrado = "hmooaudln"
rieles = 3

print(rail_fence_decrypt(cifrado, rieles))
