def ataque_automatico(cifrado):
    # Lista de palabras que buscamos (puedes añadir más)
    palabras_clave = ["EJERCITO", "ATAQUE", "ESPARTA", "EMI"]
    
    for d in range(2, len(cifrado)):
        # Lógica de descifrado rápida
        cols = (len(cifrado) + d - 1) // d
        intento = [""] * cols
        for i in range(len(cifrado)):
            intento[i % cols] += cifrado[i]
        texto_final = "".join(intento)
        
        # Verificamos si alguna palabra de nuestra lista aparece
        for palabra in palabras_clave:
            if palabra in texto_final:
                print(f"¡ÉXITO! Clave encontrada: {d}")
                print(f"Mensaje recuperado: {texto_final}")
                return
    print("No se encontró ninguna palabra conocida.")

# --- PRUEBA EN IDLE ---
ataque_automatico("ERTJCOEI")
