#Entrada
entradaPedro=input("Pedro, ingrese su apuesta ")
entradaNestor=input("Nestor, ingrese su apuesta ")
entradaJurado=input("Jurado, ingrese el resultado ")
#Proceso
puntosPedro=0
puntosNestor=0
salida=""

for letra in entradaJurado:
  if (letra in entradaPedro):
    puntosPedro=puntosPedro+1

  if (letra in entradaNestor): 
    puntosNestor=puntosNestor+1

  if (puntosPedro>puntosNestor):
    salida=salida+'J' 
  elif (puntosPedro<puntosNestor): 
    salida=salida+'K'
  elif (puntosPedro==puntosNestor):
    salida=salida+'L'

#Salida
print(salida)