def ataque_por_patron(cifrado, letra_a, letra_b):
    pos_a = cifrado.find(letra_a)
    pos_b = cifrado.find(letra_b)
    
    if pos_a != -1 and pos_b != -1:
        # La distancia en la tira desenrollada es el diámetro
        clave_probable = abs(pos_a - pos_b)
        print(f"Patrón encontrado! Distancia entre '{letra_a}' y '{letra_b}': {clave_probable}")
        
        # Intentamos descifrar con esa clave
        import math
        cols = math.ceil(len(cifrado) / clave_probable)
        res = [""] * cols
        for i in range(len(cifrado)):
            res[i % cols] += cifrado[i]
        return "".join(res)
    return "No se encontraron las letras en el mensaje."

# --- PRUEBA EN IDLE ---
# En 'ERTJCOEI', la E está en 0 y la J en 3. Distancia = 3.
print("Resultado probable:", ataque_por_patron("ERTJCOEI", "E", "J"))
