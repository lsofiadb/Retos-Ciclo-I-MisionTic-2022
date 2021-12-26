import json
#entrada
sumaTotal=0
cadenaTotal=""
diccionarioJurado={}
diccionarioJurado=json.loads(input("Ingrese los resultados del torneo: ")) #convertir la cadena a diccionario
listApuesta=[]
listApuesta=input("Ingrese los jugadores de la apuesta: ").split(" ")

claves=list(diccionarioJurado.keys())

#proceso
for i in listApuesta:
  if (i in claves):
    sumaTotal=sumaTotal+diccionarioJurado[i]
    cadenaTotal=cadenaTotal+i+" "

#salida
print(sumaTotal)
print(cadenaTotal)