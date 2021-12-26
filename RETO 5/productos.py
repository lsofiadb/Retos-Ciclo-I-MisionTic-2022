def grupos(lista):
    listaGrupoUnico=[]
    for i in range (0, len(lista)):
        if (lista[i] not in listaGrupoUnico):
            listaGrupoUnico.append(lista[i])
    return listaGrupoUnico

def necesito_del_grupo(listaIndices, listaGrupos, nombreGrupo):
  listaPosiciones=[] #retorno
  #obtener la lista de indices
  for i in range(len(listaIndices)):
    if (listaGrupos[listaIndices[i]]==int(nombreGrupo)):
      listaPosiciones.append(listaIndices[i])

  return listaPosiciones

def sirven_a_marta(listaMaria,listaMarta):
  listaIndices=[]
  #generar la lista de indices para el retorno
  for i in range(len(listaMaria)):
    if (listaMaria[i] not in listaMarta):
      listaIndices.append(listaMaria[i])

  return listaIndices
  
def cuantas_cambian(listaMarta,listaMaria):
    listProductosMaria=[]
    for i in range (len(listaMarta)):
        if (listaMarta[i] not in listaMaria):
            listProductosMaria.append(listaMarta[i])
    listProductosMarta=[]
    for i in range (len(listaMaria)):
        if (listaMaria[i] not in listaMarta):
            listProductosMarta.append(listaMaria[i])
    cantidad=0
           
    if(len(listProductosMaria)==len(listProductosMarta)):
        cantidad=len(listProductosMaria)
    if(len(listProductosMaria)<len(listProductosMarta)):
        cantidad=len(listProductosMaria)
    if(len(listProductosMaria)>len(listProductosMarta)):
        cantidad=len(listProductosMarta)
    return cantidad
    
     
    
    