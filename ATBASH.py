def cifrado_atbash(texto):
    resultado = ""
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            # Invertimos la posición de la letra minúscula
            resultado += chr(ord('z') - (ord(caracter) - ord('a')))
        elif 'A' <= caracter <= 'Z':
            # Invertimos la posición de la letra mayúscula
            resultado += chr(ord('Z') - (ord(caracter) - ord('A')))
        else:
            # Los espacios, números y símbolos se quedan igual
            resultado += caracter
    return resultado

print("========================================")
print("  CIFRADOR Y DESCIFRADOR ATBASH         ")
print("========================================")
print("> Escribe cualquier texto y presiona Enter.")
print("> Escribe 'salir' (sin comillas) para cerrar el programa.\n")

while True:
    texto_usuario = input("Ingresa tu texto: ")
    
    if texto_usuario.strip().lower() == 'salir':
        print("\nCerrando programa. ¡Hasta luego!")
        break
        
    texto_procesado = cifrado_atbash(texto_usuario)
    print(f"Resultado:        {texto_procesado}\n")
    print("-" * 40)
