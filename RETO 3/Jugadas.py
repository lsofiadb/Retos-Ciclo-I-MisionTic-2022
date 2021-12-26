#Entrada
entrada=[]
entrada=input("Ingrese la cadena con los caracteres de los jugadores propuestos: ")
listaEntrada=entrada.split() #se quitan los espacios
letra=""
listaLetras=[]
listaNumeros=[]
#print(listaEntrada)
c=1
#Proceso
#Recorrer cada posicion de la lista
listaEntrada.append("")
for i in range (0,len(listaEntrada)-1):
    letra=listaEntrada[i]
    if (listaEntrada[i]==listaEntrada[i+1]):
      c=c+1
      if (i==len(listaEntrada)-2):
        listaLetras.append(letra)
        listaNumeros.append(c)
       
    else:
      listaLetras.append(letra)
      listaNumeros.append(c)  
      c=1
      
#Salida
for i in range(0,len(listaLetras)):
  print(listaLetras[i], end=" ")
print("\n")
for i in range(0,len(listaNumeros)):
  print(listaNumeros[i], end=" ") 
