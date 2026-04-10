titular = input("nombre de titular: ")

# validamos si el valor de potencia es un numero, si no lo es, se le pide al usuario que ingrese un valor valido
# se convierte el valor de potencia a un numero flotante, si el usuario ingresa un valor que no se puede convertir a un numero, se lanza una excepcion ValueError y se le pide al usuario que ingrese un valor valido

while True:
   try:
      potencia = float(input("dijite la potencia: "))
      break
   except ValueError:
      print ("dijite un valor valido")


if potencia <= -0.1 and potencia > -15:
   print(f"La potencia de {titular} es fuerte/alta")
elif potencia <= -15 and potencia >= -25:
   print(f"La potencia de {titular} es normal")
elif potencia < -25 and potencia >= -27:
   print(f"La potencia de {titular} es critica")
elif potencia < -27:
   print(f"La potencia de {titular} es debil/baja")
elif potencia > -0.1:
   print(f"la potencia del titular {titular} es muy fuerte, o, te equivocaste al ingresar la potencia en positivo, recuerda que la potencia normalmente es un numero negativo")

