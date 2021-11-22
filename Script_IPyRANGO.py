# Entrada de datos
print("¿De que IP se trata?")
ipatratar = input()

print("¿Que rango tendría?")
rangoip = input()

print("Los datos son: " + ipatratar + "/" + rangoip + " ?")
respuesta = input("¿Quieres empezar el cálculo de subred? S/N: ")

if respuesta == "s" or respuesta == "S":
    print("Procesando...")
    print("...")

# Binarizado
unocteto,dosocteto,tresocteto,cuatrocteto = ipatratar.split(".")
mascara = ("0.0.0.0","0.0.0.0","128.0.0.0","192.0.0.0","224.0.0.0","240.0.0.0","248.0.0.0","252.0.0.0","254.0.0.0","255.0.0.0","255.128.0.0","255.192.0.0","255.224.0.0","255.240.0.0","255.248.0.0","255.252.0.0","255.254.0.0","255.255.0.0","255.255.128.0","255.255.192.0","255.255.224.0","255.255.240.0","255.255.248.0","255.255.252.0","255.255.254.0","255.255.255.0","255.255.255.192","255.255.255.224","255.255.255.240","255.255.255.248","255.255.255.252","255.255.255.254","255.255.255.255")
unoctetomasc,dosoctetomasc,tresoctetomasc,cuatroctetomasc = mascara[int(rangoip)].split(".")

# AND
ipnumerouno = (int(unocteto)) & int(unoctetomasc)
ipnumerodos = (int(dosocteto)) & int(dosoctetomasc)
ipnumerotres = (int(tresocteto)) & int(tresoctetomasc)
ipnumerocuatro = (int(cuatrocteto)) & int(cuatroctetomasc)
ipnumerocuatrohost = ipnumerocuatro + 1

primeraip = str(ipnumerouno) +"."+ str(ipnumerodos) +"."+ str(ipnumerotres) +"."+ str(ipnumerocuatro)
primerhost = str(ipnumerouno) +"."+ str(ipnumerodos) +"."+ str(ipnumerotres) +"."+ str(ipnumerocuatrohost)

# Calcula la clase de la IP.
clases = ("Clase A","Clase B","Clase C")
if int(dosoctetomasc) < 255:
    clase = clases[0]
else:
    if int(tresoctetomasc) < 255:
        clase = clases[1]
    else:
        if int(cuatroctetomasc) < 255:
            clase = clases[2]

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

equivalencia = ("1","2","4","8","16","32","64","128","256")

# Número de hosts.
if str(salto) in equivalencia:
    magico = equivalencia.index(str(salto))                           
numerodehosts = 2 ** magico -2

# Número de subredes.
numerodesubredes = (equivalencia[-magico - 1])
     
# Broadcast.
mibro = (equivalencia[magico])
ultimoctetobroad = int(mibro) + int(ipnumerocuatro) - 1
broadcast = str(ipnumerouno) +"."+ str(ipnumerodos) +"."+ str(ipnumerotres) +"."+ str(ultimoctetobroad)

# Último host.
ultimoctetoulthost = int(ultimoctetobroad) - 1
ultimohost = str(ipnumerouno) +"."+ str(ipnumerodos) +"."+ str(ipnumerotres) +"."+ str(ultimoctetoulthost)

# Resultados.
print("Estos son los resultados:")
print()
print("1. La IP de la subred que pertenece: " + str(primeraip))
print("2. La máscara de red es: " + mascara[int(rangoip)])
print("3. El primer host es: " + str(primerhost))
print("4. El último host es: " + str(ultimohost))
print("5. La broadcast: " + str(broadcast))
print("6. La IP es " + str(clase))
print("7. Numero de host: " + str(numerodehosts))
print("8. El número de subredes es: " + str(numerodesubredes))
print("--------------")
print("Información adicional.")
print("IP calculada: " + ipatratar)
print("El salto de red es: " + str(salto))
print("El número mágico es: " + str(magico))

