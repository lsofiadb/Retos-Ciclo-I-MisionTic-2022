#Datos de entrada
precioLeche=int(input("Ingrese el precio de la leche "))

#Proceso 
precioArroz=int(2*(precioLeche)+4)
precioCafe=int((precioArroz+precioLeche)/5)

#Salida
print(str(precioLeche)+" "+str(precioArroz)+" "+str((precioCafe)))

if (0<=precioCafe<=20):
  print("uno")
elif (21<=precioCafe<=30):
  print("dos")
elif (31<=precioCafe<=50):
  print("tres")
elif (precioCafe>50):
  print("cuatro")
