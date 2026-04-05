def obtener_tabla_polibio():
    return {
        'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
        'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25',
        'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
        'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
        'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
    }

def cifrar_polibio(texto):
    tabla = obtener_tabla_polibio()
    texto = texto.upper().replace(" ", "")
    resultado = ""
    for letra in texto:
        if letra in tabla:
            resultado += tabla[letra] + " "
    return resultado.strip()

def descifrar_polibio(codigo):
    tabla = obtener_tabla_polibio()
    tabla_inversa = {valor: clave for clave, valor in tabla.items()}
    numeros = codigo.replace(",", " ").replace("-", " ").split()
    resultado = ""
    for num in numeros:
        if num in tabla_inversa:
            resultado += tabla_inversa[num]
        else:
            resultado += "?"
    return resultado
def menu():
    while True:
        print("\n--- MENÚ CRIPTOGRAFÍA POLIBIO ---")
        print("1. Cifrar texto (Texto -> Números)")
        print("2. Descifrar código (Números -> Texto)")
        print("3. Salir")
        
        opcion = input("\nElige una opción (1/2/3): ")
        
        if opcion == '1':
            msg = input("Introduce el mensaje a cifrar: ")
            print(f"Resultado cifrado: {cifrar_polibio(msg)}")
        elif opcion == '2':
            cod = input("Introduce los números (separados por espacios): ")
            print(f"Mensaje descifrado: {descifrar_polibio(cod)}")
        elif opcion == '3':
            print("¡Adiós!, nos vemos :)")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()