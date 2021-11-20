# Inserción de datos
print("¿De que IP se trata?")
ipatratar = input()
print("¿Cuantas subredes tiene?")
C = input()
print("Los datos son: " + ipatratar + " para " + C + " subredes.")
respuesta = input("¿Quieres empezar el cálculo de subred? S/N: ")
if respuesta == "s" or respuesta == "S":
    print("Procesando...")
    print("...")
    
# Separa cada octeto en variables.
unocteto,dosocteto,tresocteto,cuatrocteto = ipatratar.split(".")

# Cálculo subredes.
N = 0
while 2**int(N) < int(C):
    N += 1

# Busqueda de máscara.
mascara = ("0.0.0.0","128.0.0.0","192.0.0.0","224.0.0.0","240.0.0.0","248.0.0.0","252.0.0.0","254.0.0.0","255.0.0.0","255.128.0.0","255.192.0.0","255.224.0.0","255.240.0.0","255.248.0.0","255.252.0.0","255.254.0.0","255.255.0.0","255.255.128.0","255.255.192.0","255.255.224.0","255.255.240.0","255.255.248.0","255.255.252.0","255.255.254.0","255.255.255.0","255.255.255.192","255.255.255.224","255.255.255.240","255.255.255.248","255.255.255.252","255.255.255.254","255.255.255.255")
if int(unocteto) > 0:
    mascarilla = mascara[8 + N]
else:
    if int(dosocteto) > 0:
        mascarilla = mascara[16 + N]
    else:
        if int(tresocteto) > 0:
            mascarilla = mascara[24 + N]
        else:
            if int(cuatrocteto) > 0:
                mascarilla = mascara[32 + N] 
unoctetomasc,dosoctetomasc,tresoctetomasc,cuatroctetomasc = mascarilla.split(".")

# Calcula el número mágico.
if int(unocteto) == 0:
    magico = 8 + 8 + 8 + 8 - N
else:
    if int(dosocteto) == 0:
        magico = 8 + 8 + 8 - N
    else:
        if int(tresocteto) == 0:
            magico = 8 + 8 - N
        else:
            if int(cuatrocteto) == 0:
                magico = 8 - N
    
# Calcula el salto de red.
if int(unoctetomasc) < 255:
    salto = 256 - int(unoctetomasc)
else:
    if int(dosoctetomasc) < 255:
        salto = 256 - int(dosoctetomasc)
    else:
        if int(tresoctetomasc) < 255:
            salto = 256 - int(tresoctetomasc)
        else:
            if int(cuatroctetomasc) < 255:
                salto = 256 - int(cuatroctetomasc)
                            
# Calcula el número de hosts.
hosts = 2**magico - 2

# Calcula la clase de la IP.
clases = ("Clase A","Clase B","Clase C")
if int(dosocteto) == 0:
    clase = clases[0]
else:
    if int(tresocteto) == 0:
        clase = clases[1]
    else:
        if int(cuatrocteto) == 0:
            clase = clases[2]

# Primer host:
primerhost = int(cuatrocteto) + 1

# Primera IP:
ipnumerouno = str(unocteto) +"."+ str(dosocteto) +"."+ str(tresocteto) +"."+ str(primerhost)

# Último broadcast:
if clase == clases[0]:
    octetoultimohost = int(salto) * int(C) - int(salto)
else:
    if clase == clases[1]:
        octetoultimohost = int(salto) * int(C) - int(salto)
    else:
        if clase == clases[2]:
            octetoultimohost = int(salto) * int(C) - int(salto)

if int(dosocteto) == 0:
    ultimohost = str(unocteto) +"."+ str(octetoultimohost) + "." + "255" + "." + "255"
else:
    if int(tresocteto) == 0:
        ultimohost = str(unocteto) +"."+ str(dosocteto) +"."+ str(octetoultimohost) +".255"
    else:
        if int(cuatrocteto) == 0:
            ultimohost = str(unocteto) +"."+ str(dosocteto) +"."+ str(tresocteto) +"."+ str(octetoultimohost)


# Resultados.
print("--------------")
print("La IP es clase " + str(clase))
print("IP calculada: " + ipatratar)
print("La máscara de red es: " + mascarilla)
print("El número mágico es: " + str(magico))
print("El número de hosts es: " + str(hosts))
print("El salto de red es: " + str(salto))
print("--------------")
print("La primera IP es: " + str(ipnumerouno))
print("El último broadcast es: " + str(ultimohost))


