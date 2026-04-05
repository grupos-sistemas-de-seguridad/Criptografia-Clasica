import math

def obtener_tablas():
    tabla = {
        'A': 'AA', 'B': 'AD', 'C': 'AF', 'D': 'AG', 'E': 'AX',
        'F': 'DA', 'G': 'DD', 'H': 'DF', 'I': 'DG', 'J': 'DG', 'K': 'DX',
        'L': 'FA', 'M': 'FD', 'N': 'FF', 'O': 'FG', 'P': 'FX',
        'Q': 'GA', 'R': 'GD', 'S': 'GF', 'T': 'GG', 'U': 'GX',
        'V': 'XA', 'W': 'XD', 'X': 'XF', 'Y': 'XG', 'Z': 'XX'
    }
    tabla_inversa = {valor: clave for clave, valor in tabla.items()}
    return tabla, tabla_inversa

def cifrar_adfgx(texto, clave):
    tabla, _ = obtener_tablas()
    texto = texto.upper().replace(" ", "")
    sustituido = "".join([tabla[l] for l in texto if l in tabla])
    columnas = len(clave)
    filas = math.ceil(len(sustituido) / columnas)
    grid = [['' for _ in range(columnas)] for _ in range(filas)]
    for i, char in enumerate(sustituido):
        grid[i // columnas][i % columnas] = char
    orden_clave = sorted(range(len(clave)), key=lambda k: clave[k])
    resultado = ""
    for col in orden_clave:
        for fila in range(filas):
            if grid[fila][col] != '':
                resultado += grid[fila][col]
    return resultado

def descifrar_adfgx(codigo, clave):
    _, tabla_inversa = obtener_tablas()
    codigo = codigo.replace(" ", "")
    columnas = len(clave)
    filas = math.ceil(len(codigo) / columnas)
    
    huecos = (filas * columnas) - len(codigo)
    indices_columnas_cortas = list(range(columnas - huecos, columnas))
    orden_clave = sorted(range(len(clave)), key=lambda k: clave[k])
    grid = [['' for _ in range(columnas)] for _ in range(filas)]
    pos_actual = 0
    
    for col_index in orden_clave:
        filas_en_esta_col = filas - 1 if col_index in indices_columnas_cortas else filas
        for f in range(filas_en_esta_col):
            if pos_actual < len(codigo):
                grid[f][col_index] = codigo[pos_actual]
                pos_actual += 1

    cadena_sustituida = ""
    for f in range(filas):
        for c in range(columnas):
            cadena_sustituida += grid[f][c]
    mensaje = ""
    for i in range(0, len(cadena_sustituida), 2):
        par = cadena_sustituida[i:i+2]
        if par in tabla_inversa:
            mensaje += tabla_inversa[par]
            
    return mensaje

def menu():
    while True:
        print("\n--- SISTEMA CRIPTOGRÁFICO ADFGX ---")
        print("1. Cifrar Mensaje")
        print("2. Descifrar Mensaje")
        print("3. Salir")
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            msg = input("Texto a cifrar: ")
            key = input("Palabra clave: ")
            print(f"Resultado Cifrado: {cifrar_adfgx(msg, key)}")
        elif opcion == '2':
            cod = input("Código a descifrar: ")
            key = input("Palabra clave: ")
            print(f"Resultado Descifrado: {descifrar_adfgx(cod, key)}")
        elif opcion == '3':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()