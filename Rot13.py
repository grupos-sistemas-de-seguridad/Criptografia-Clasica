def cifrado_rot13(texto):
    resultado = ""
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            resultado += chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= caracter <= 'Z':
            resultado += chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
        else:
            resultado += caracter
    return resultado

print("========================================")
print("  CIFRADOR Y DESCIFRADOR ROT13          ")
print("========================================")
print("> Escribe cualquier texto y presiona Enter.")
print("> Escribe 'salir' (sin comillas) para cerrar el programa.\n")

while True:
    texto_usuario = input("Ingresa tu texto: ")
    
    if texto_usuario.strip().lower() == 'salir':
        print("\nCerrando programa. ¡Hasta luego!")
        break
        
    texto_procesado = cifrado_rot13(texto_usuario)
    print(f"Resultado:        {texto_procesado}\n")
    print("-" * 40)
