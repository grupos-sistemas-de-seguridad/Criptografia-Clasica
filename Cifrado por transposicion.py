# CIFRADO POR TRANSPOSICIÓN COLUMNAR :

import re
from unicodedata import normalize

# FUNCIÓN DE CIFRADO:
def cifrar(texto, clave):
    criptograma=''
    if len(texto)%len(clave)==0:
        filas=len(texto)//len(clave)
    else:
        filas=len(texto)//len(clave)+1
    texto_claro=[" "]*filas*len(clave)
    for i in range(0,len(texto)):
        texto_claro[i]=texto[i]
    clave_alfabetica_ordenada=sorted(clave)
    clave_numerica=[]
    for i in range(0,len(clave)):
         clave_numerica.append(clave_alfabetica_ordenada.index(clave[i]))
    for i in range(1,len(clave)):
        for j in range(0,i):
            if clave_numerica[i]==clave_numerica[j]:
                clave_numerica[i]+=1
    for i in range(0,len(clave)):
        for j in range(0,filas):
            criptograma+=texto_claro[clave_numerica.index(i)+len(clave)*j]
    return criptograma.replace(' ','')

# FUNCIÓN DE DESCIFRADO:
def descifrar(texto, clave):
    texto_claro=''
    if len(texto)%len(clave)==0:
        filas=len(texto)//len(clave)
        columnas_completas=len(clave)
    else:
        filas=len(texto)//len(clave)+1
        columnas_completas=len(texto)%len(clave)
    columnas_incompletas=len(clave)-columnas_completas
    clave_alfabetica_ordenada=sorted(clave)
    clave_numerica=[]
    for i in range(0,len(clave)):
         clave_numerica.append(clave_alfabetica_ordenada.index(clave[i]))
    for i in range(1,len(clave)):
        for j in range(0,i):
            if clave_numerica[i]==clave_numerica[j]:
                clave_numerica[i]+=1
    huecos=[]
    for i in range(-1,-columnas_incompletas-1,-1):
        huecos.append((clave_numerica[i]*filas)+(filas-1))
    huecos=sorted(huecos)
    texto_huecos=''
    huecos_incluidos=0
    for i in range(0,len(texto)):
        if i in huecos:
            texto_huecos+=' '
            huecos_incluidos+=1
            if columnas_incompletas-huecos_incluidos!=0:
                huecos[huecos_incluidos]=huecos[huecos_incluidos]-huecos_incluidos
        texto_huecos+=texto[i]
    criptograma=[" "]*filas*len(clave)
    for i in range(0,len(texto_huecos)):
            criptograma[((i%filas)*len(clave))+(i//filas)]=texto_huecos[i]
    for i in range(0,filas):
        for j in range(0,len(clave)):
            texto_claro+=criptograma[clave_numerica[j]+len(clave)*i]
    return texto_claro.replace(' ','')

# MENÚ:
# Se presenta el menú para que se seleccione una opción.
def main():
    salir = False
    while not salir:
        print ("")
        print ("*** MENÚ *****************************************")
        print ("1. Cifrar.")
        print ("2. Descifrar.")
        print ("3. Salir.")
        print ("")
        opcion = input("Por favor, seleccione una opción: ")
        if opcion == "1":
            print ("")
            print ("--- CIFRAR:")
            texto_claro = clave = "*"
            while not texto_claro.isalpha():
                texto_claro = input('Texto en claro a cifrar: ').upper()
                texto_claro = texto_claro.replace(' ','')
                texto_claro = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
                                     r"\1", normalize("NFD", texto_claro), 0, re.I)
                texto_claro = normalize("NFC", texto_claro)
                if texto_claro.isalpha():
                    print ("[+] Texto en claro a cifrar:", texto_claro)
                    while not clave.isalpha():
                        clave = input('Clave: ').upper()
                        clave = clave.replace(' ','')
                        clave = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
                                    r"\1", normalize("NFD", clave), 0, re.I)
                        clave = normalize("NFC", clave)
                        if clave.isalpha():
                            print ("[+] Clave:", clave)
                            criptograma = cifrar(texto_claro, clave)
                            print ("[+] Criptograma:", criptograma)
                        else:
                            print ("*** ERROR: La clave sólo debe contener caracteres alfabéticos.")
                else:
                    print ("*** ERROR: El texto en claro a cifrar sólo debe contener caracteres alfabéticos.")
        elif opcion == "2":
            print ("")
            print ("--- DESCIFRAR:")
            criptograma = clave = "*"
            while not criptograma.isalpha():
                criptograma = input('Criptograma a descifrar: ').upper()
                criptograma = criptograma.replace(' ','')
                criptograma = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
                                     r"\1", normalize("NFD", criptograma), 0, re.I)
                criptograma = normalize("NFC", criptograma)
                if criptograma.isalpha():
                    print ("[+] Criptograma a descifrar:", criptograma)
                    while not clave.isalpha():
                        clave = input('Clave: ').upper()
                        clave = clave.replace(' ','')
                        clave = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
                                    r"\1", normalize("NFD", clave), 0, re.I)
                        clave = normalize("NFC", clave)
                        if clave.isalpha():
                            print ("[+] Clave:", clave)
                            texto_claro = descifrar(criptograma, clave)
                            print ("[+] Texto en claro:", texto_claro)
                        else:
                            print ("*** ERROR: La clave sólo debe contener caracteres alfabéticos.")
                else:
                    print ("*** ERROR: El criptograma a descifrar sólo debe contener caracteres alfabéticos.")
        elif opcion == "3":
            print ("*** FIN ******************************************")
            salir = True
        else:
            print ("*** ERROR: Opción no válida.")
	
if __name__ == '__main__':
    main()