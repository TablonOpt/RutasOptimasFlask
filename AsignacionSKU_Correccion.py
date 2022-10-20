# -*- coding: utf-8 -*-
"""
Created on  November

Esta función asigna correctamente todos los SKU a las coordenadas de recolección.
Dados los pedidos en cola y los articulos por pedido
Así como las coordenadas de recolección.

@author: Alban Rodríguez

"""


import pandas as pd
###################################
#Buscamos asignar los SKUS en las rutas de recolección de forma correcta.
nameCols=["X","Y","SKU_PRODUCTO","ID_Pasillo","ID_Ubic"]
Ubicaciones_SKU = pd.read_csv("Ubicaciones.csv", usecols=nameCols)

#Casteamos a listas.
SKU=Ubicaciones_SKU['SKU_PRODUCTO'].tolist()
Pasillo_Ubic=Ubicaciones_SKU['ID_Pasillo'].tolist()
ID_Ubic=Ubicaciones_SKU['ID_Ubic'].tolist()



#Llenamos una lista con los elementos de las ubicaciones.
#SKU,Pasillo y Ubicación
File_Ubicaciones_List=[]
for i in range(0,len(SKU),1):
    File_Ubicaciones_List.append((SKU[i],Pasillo_Ubic[i],ID_Ubic[i]))  


def AsignacionSKU_Correcto_RutaRecolec(Pedidos_Cola,Artic_Pedidos_Cola,RutaRecolec_Pedidos):
    #Almacenamos los indices de todas nuestras ubicaciones en donde se encuentran nuestros SKUS
    #Estas serán las posibles ubicaciones para cada SKU del pedido
    ListaIndices_TodosLosPedidos=[]
    IndicesPosibles_Un_Pedido_Separados=[]
    IndicesPosibles_Un_Pedido_Juntos=[]
    contador=0
    #Indices del producto de interes
    for z in Artic_Pedidos_Cola:
        for x in z:
            for i in File_Ubicaciones_List:
                for j in i:
                    if j==str(x):
                        IndicesPosibles_Un_Pedido_Juntos.append(contador)
                contador+=1
            IndicesPosibles_Un_Pedido_Separados.append(IndicesPosibles_Un_Pedido_Juntos)
            IndicesPosibles_Un_Pedido_Juntos=[]
            contador=0
        ListaIndices_TodosLosPedidos.append(IndicesPosibles_Un_Pedido_Separados)
        IndicesPosibles_Un_Pedido_Separados=[]
    #print(ListaIndices_TodosLosPedidos)
        
    #Extraemos los indices recolectados en el paso anterior para recuperar el SKU, Pasillo y Ubicacion
    UbicacionesPosibles_Varios_Pedido_Separados=[]
    UbicacionesPosibles_Varios_Pedido_Juntos=[]
    UbicacionesPosibles_Varios_Pedido_Separados_FINAL=[]
    
    for z in ListaIndices_TodosLosPedidos:
        for x in z:
            for i in x:
                UbicacionesPosibles_Varios_Pedido_Juntos.append(File_Ubicaciones_List[i])
            UbicacionesPosibles_Varios_Pedido_Separados.append(UbicacionesPosibles_Varios_Pedido_Juntos)
            UbicacionesPosibles_Varios_Pedido_Juntos=[]
        UbicacionesPosibles_Varios_Pedido_Separados_FINAL.append(UbicacionesPosibles_Varios_Pedido_Separados)
        UbicacionesPosibles_Varios_Pedido_Separados=[]
    
    #Recorremos las posibles ubicaciones para cada pedido
    #para cada articulo
    # Y nos quedamos con el último
    # Ya que esa es al forma en la que trabaja el algortimo que al tener diccionarios
    # que toman como llave los SKU, solo se quedan con la última ubicación posible del SKU
    
            

    UltimaUbicacionl_Separadas_VariosPedidos=[]
    UltimaUbicacion_Juntas_VariosPedidos=[]
    
    for i in UbicacionesPosibles_Varios_Pedido_Separados_FINAL:
        for j in i:
            UltimaUbicacion_Juntas_VariosPedidos.append(j[-1])
        UltimaUbicacionl_Separadas_VariosPedidos.append(UltimaUbicacion_Juntas_VariosPedidos)
        UltimaUbicacion_Juntas_VariosPedidos=[]
    #print(UltimaUbicacionl_Separadas_VariosPedidos)
    
    #Asignamos el SKU correspondiente a cada ubicación de la ruta de recolección basandonos en los articulos del pedido
    #Para todos los pedidos.
    
    
    TempoUbicFinal_VariosPedidos_Copia=UltimaUbicacionl_Separadas_VariosPedidos.copy()
    RutaRecolec_VariosPedidos_Copia=RutaRecolec_Pedidos.copy()
    RutaRecolecFinal_VariosPedidos_Juntos_SKUCorregido=[]
    RutaRecolecFinal_VariosPedidos_Separados_SKUCorregido=[]
    
    
    contadorPedidos=0

    for i in RutaRecolec_VariosPedidos_Copia:
        for j in i:
            for z in TempoUbicFinal_VariosPedidos_Copia[contadorPedidos]:
                if j==z[1:]:
                    RutaRecolecFinal_VariosPedidos_Juntos_SKUCorregido.append(z)
                    TempoUbicFinal_VariosPedidos_Copia[contadorPedidos].remove(z)
                    #print(z)
                RutaRecolecFinal_VariosPedidos_Separados_SKUCorregido.append(RutaRecolecFinal_VariosPedidos_Juntos_SKUCorregido)
                RutaRecolecFinal_VariosPedidos_Juntos_SKUCorregido=[]        
        contadorPedidos+=1
    #print(len(RutaRecolecFinal_VariosPedidos_Separados_SKUCorregido))
    #print(RutaRecolecFinal_VariosPedidos_Separados_SKUCorregido)
    
    #Removemos todas las listas vacías para poder agrupar por pedido las coordenadas de recolección
    LimpiezaPedidosJuntos = [x for x in RutaRecolecFinal_VariosPedidos_Separados_SKUCorregido if x != []]
    #print(LimpiezaPedidosJuntos)
    
    #Agrupamos en nuevas listas dada la longitud de los pedidos
    ListaPedidosSeparadosFinal=[]
    
    for i in RutaRecolec_Pedidos:
        ListaPedidosSeparadosFinal.append(LimpiezaPedidosJuntos[:len(i)])
        del LimpiezaPedidosJuntos[:len(i)]
    
    #print(ListaPedidosSeparadosFinal)
    
    
    
    return ListaPedidosSeparadosFinal

#Pedidos_Cola=[1085, 613090, 380, 612424, 612425, 613155, 613086, 613217, 613156]
#Artic_Pedidos_Cola=[[85, 39, 74819, 72942, 72949, 74817, 72950, 74650], [5525, 84, 38, 43, 8714, 39, 49, 40, 41, 2332, 2333, 85, 10965, 42, 44], [38, 52, 51, 18248, 44, 43, 18250, 53, 54, 18249, 18237, 41, 7703, 17171, 55, 18238, 17170, 7098, 9444, 40, 9320, 37, 9767], [18250, 9767, 9444, 17171, 51, 18237, 18249, 18248, 38, 53, 54, 55, 37, 41, 44, 18238, 52, 40, 43, 17170], [7703], [53, 55, 75, 51, 54, 38, 5525, 42, 73, 77, 78, 52, 37, 41, 2332, 74, 39, 81, 40], [89, 48, 51, 75, 26255, 42, 1920, 92, 39, 90, 5525, 389, 79, 41], [5525, 8508, 18238, 19231, 7703, 5630, 5936, 10965, 19228, 6280, 8200, 8502, 8507, 13127], [91, 89, 90, 49, 90, 91, 376, 376, 89, 49]]
#RutaRecolec_Pedidos=[[('A2', 30101), ('B1', 30136), ('D2', 9315), ('D2', 9350), ('G1', 16475), ('D2', 107605), ('D2', 107610), ('B2', 106885)], [('A2', 30101), ('D1', 7855), ('D1', 7865), ('D1', 7885), ('D1', 7895), ('D1', 7915), ('D2', 9280), ('D2', 9290), ('D2', 9305), ('D2', 9315), ('D2', 9320), ('D2', 9340), ('D2', 9345), ('D2', 9350), ('D2', 9370)], [('A2', 30101), ('D1', 7835), ('D1', 7840), ('D1', 7850), ('D1', 7855), ('D1', 7860), ('D2', 9285), ('D2', 9290), ('D2', 9300), ('D2', 9305), ('D2', 9345), ('D2', 9380), ('D2', 9385), ('D2', 9405), ('D2', 9415), ('D2', 9420), ('E1', 10730), ('E1', 10765), ('E2', 12250), ('D1', 7965), ('D1', 7970), ('D1', 7975), ('D1', 7980)], [('A2', 30101), ('D1', 7835), ('D1', 7840), ('D1', 7850), ('D1', 7855), ('D1', 7860), ('D2', 9285), ('D2', 9290), ('D2', 9300), ('D2', 9305), ('D2', 9345), ('D2', 9380), ('D2', 9385), ('D2', 9405), ('D2', 9415), ('D2', 9420), ('D1', 7965), ('D1', 7970), ('D1', 7975), ('D1', 7980)], [('E1', 10730)], [('A2', 30101), ('D1', 7835), ('D1', 7840), ('D1', 7845), ('D1', 7850), ('D1', 7860), ('D1', 7865), ('D1', 7870), ('D1', 7875), ('D1', 7885), ('D1', 7950), ('D2', 9280), ('D2', 9285), ('D2', 9290), ('D2', 9300), ('D2', 9305), ('D2', 9315), ('D2', 9355), ('D2', 9360)], [('D2', 9280), ('D2', 9285), ('D2', 9295), ('D2', 9305), ('D2', 9310), ('D2', 9315), ('E1', 10750), ('D1', 7870), ('D1', 7885), ('D1', 7905), ('D1', 7925), ('D2', 9445), ('C1', 5150), ('C1', 5160)], [('E1', 10730), ('E1', 10755), ('E1', 10775), ('E1', 10820), ('E1', 10850), ('E1', 10865), ('D2', 9340), ('D2', 9385), ('D2', 9500), ('D1', 7885), ('E2', 12285), ('E2', 12295), ('E2', 12310), ('E2', 12315)], [('D2', 9295), ('D2', 9295), ('D2', 9325), ('D2', 9325), ('D1', 7895), ('D1', 7895), ('D1', 7925), ('D1', 7925), ('E1', 10785), ('E1', 10785)]]
#Recolecc_OPT_SK_Correcto=AsignacionSKU_Correcto_RutaRecolec(Pedidos_Cola,Artic_Pedidos_Cola,RutaRecolec_Pedidos)





#Ahora trabajamos con la función para optimización de pedidos aplilados.
def AsignacionSKU_Correcto_RutaRecolec_Olas(Pedidos_Cola_Agrupados,Artic_Pedidos_Cola_Agrupados,RutaRecolec_Pedidos_Agrupados,cant_prod,agrupador):
    #Vamos a desempaquetar los articulos por pedido
    contador=0
    Lista_Interna=[]
    listaUno_Empaquetado_Juntos=[]
    listArticulos_Separados=[]
    for i in Artic_Pedidos_Cola_Agrupados:
        #print(contador)
        #print(i)
        for j in i:
            #print(j)
            for z in j:
                #print(z)
                Lista_Interna.append(z)
        listArticulos_Separados.append(Lista_Interna)
        Lista_Interna=[]
        contador+=1 #Indica el pedido en el que estamos
    #print(Artic_Pedidos_Cola_Agrupados)
    #print(listArticulos_Separados)
    
    Artic_Pedidos_Cola_Agrupados=listArticulos_Separados
    print("PEDIDOS AGRUPADOS EN N OLAS")
    print(len(Artic_Pedidos_Cola_Agrupados))
    print(Artic_Pedidos_Cola_Agrupados)
    #print(len(Artic_Pedidos_Cola_Agrupados[0]))
    
    #Hasya aquí vamos bien, ya desempaquetamos los articulos de los pedidos
    #Para que tengan el formato
    
    #Almacenamos los indices de todas nuestras ubicaciones en donde se encuentran nuestros SKUS
    #Estas serán las posibles ubicaciones para cada SKU del pedido
    ListaIndices_TodosLosPedidos=[]
    IndicesPosibles_Un_Pedido_Separados=[]
    IndicesPosibles_Un_Pedido_Juntos=[]
    contador=0
    #Indices del producto de interes
    for z in Artic_Pedidos_Cola_Agrupados:
        for x in z:
            for i in File_Ubicaciones_List:
                for j in i:
                    if j==str(x):
                        IndicesPosibles_Un_Pedido_Juntos.append(contador)
                contador+=1
            IndicesPosibles_Un_Pedido_Separados.append(IndicesPosibles_Un_Pedido_Juntos)
            IndicesPosibles_Un_Pedido_Juntos=[]
            contador=0
        ListaIndices_TodosLosPedidos.append(IndicesPosibles_Un_Pedido_Separados)
        IndicesPosibles_Un_Pedido_Separados=[]
    print("Función 1 Indices: ")
    #print(len(ListaIndices_TodosLosPedidos[1]))
    #print(ListaIndices_TodosLosPedidos[1])
    

    
    #Extraemos los indices recolectados en el paso anterior para recuperar el SKU, Pasillo y Ubicacion
    UbicacionesPosibles_Varios_Pedido_Separados=[]
    UbicacionesPosibles_Varios_Pedido_Juntos=[]
    UbicacionesPosibles_Varios_Pedido_Separados_FINAL=[]
    
    for z in ListaIndices_TodosLosPedidos:
        for x in z:
            for i in x:
                UbicacionesPosibles_Varios_Pedido_Juntos.append(File_Ubicaciones_List[i])
            UbicacionesPosibles_Varios_Pedido_Separados.append(UbicacionesPosibles_Varios_Pedido_Juntos)
            UbicacionesPosibles_Varios_Pedido_Juntos=[]
        UbicacionesPosibles_Varios_Pedido_Separados_FINAL.append(UbicacionesPosibles_Varios_Pedido_Separados)
        UbicacionesPosibles_Varios_Pedido_Separados=[]
    
    print("UbicacionesPosible Pedidos FINAL")
    print(len(UbicacionesPosibles_Varios_Pedido_Separados_FINAL))
    print(UbicacionesPosibles_Varios_Pedido_Separados_FINAL)
    print("SEPARADOR")
    #print(UbicacionesPosibles_Varios_Pedido_Separados_FINAL[1])
    #print(len((UbicacionesPosibles_Varios_Pedido_Separados_FINAL[1])))
    
    

    #Recorremos las posibles ubicaciones para cada pedido
    #para cada articulo
    # Y nos quedamos con el último
    # Ya que esa es al forma en la que trabaja el algortimo que al tener diccionarios
    # que toman como llave los SKU, solo se quedan con la última ubicación posible del SKU
    
    UltimaUbicacionl_Separadas_VariosPedidos=[]
    UltimaUbicacion_Juntas_VariosPedidos=[]
    for i in UbicacionesPosibles_Varios_Pedido_Separados_FINAL:
        for j in i:
            UltimaUbicacion_Juntas_VariosPedidos.append(j[-1])
        UltimaUbicacionl_Separadas_VariosPedidos.append(UltimaUbicacion_Juntas_VariosPedidos)
        UltimaUbicacion_Juntas_VariosPedidos=[]
    print("Ubicación Final Pedidos:")
    print(len(UbicacionesPosibles_Varios_Pedido_Separados_FINAL))
    print(UltimaUbicacionl_Separadas_VariosPedidos)
    
    
    #VERIFICADO HASTA ESTE PUNTO :)
    ###############################################################
    ###############################################################
    
    #Asignamos el SKU correspondiente a cada ubicación de la ruta de recolección basandonos en los articulos del pedido
    #Para todos los pedidos.
    
    TempoUbicFinal_VariosPedidos_Copia=UltimaUbicacionl_Separadas_VariosPedidos.copy()
    RutaRecolec_VariosPedidos_Copia=RutaRecolec_Pedidos_Agrupados.copy()
    RutaRecolecFinal_VariosPedidos_Juntos_SKUCorregido=[]
    RutaRecolecFinal_VariosPedidos_Separados_SKUCorregido=[]
    
    contadorPedidos=0
    
    for i in RutaRecolec_VariosPedidos_Copia:
        for j in i:
            for z in TempoUbicFinal_VariosPedidos_Copia[contadorPedidos]:
                if j==z[1:]:
                    RutaRecolecFinal_VariosPedidos_Juntos_SKUCorregido.append(z)
                    TempoUbicFinal_VariosPedidos_Copia[contadorPedidos].remove(z)
                    #print(z)
                RutaRecolecFinal_VariosPedidos_Separados_SKUCorregido.append(RutaRecolecFinal_VariosPedidos_Juntos_SKUCorregido)
                RutaRecolecFinal_VariosPedidos_Juntos_SKUCorregido=[]        
        contadorPedidos+=1
    print(len(RutaRecolecFinal_VariosPedidos_Separados_SKUCorregido))
    print(RutaRecolecFinal_VariosPedidos_Separados_SKUCorregido)
    
    #Removemos todas las listas vacías para poder agrupar por pedido las coordenadas de recolección
    LimpiezaPedidosJuntos = [x for x in RutaRecolecFinal_VariosPedidos_Separados_SKUCorregido if x != []]
    print("LIMPIEZAPEDIDOSJUNTOS")
    print(len(LimpiezaPedidosJuntos))
    print(LimpiezaPedidosJuntos)
    
    #Obtenemos una lista con cuantos articulos son por pedido.
    ListaCantidadArticulos_PorPedido=[]
    for i in Artic_Pedidos_Cola_Agrupados:
        print(len(i))
        ListaCantidadArticulos_PorPedido.append(len(i))
    
    #Agrupamos en nuevas listas dada la canitdad de articulos de los pedidos
    ListaPedidosSeparadosFinal=[]
    
    for i in range(0,len(Artic_Pedidos_Cola_Agrupados),1):
        ListaPedidosSeparadosFinal.append(LimpiezaPedidosJuntos[:ListaCantidadArticulos_PorPedido[i]])
        del LimpiezaPedidosJuntos[:ListaCantidadArticulos_PorPedido[i]]
    
    print("\n\nCoordenadas Recolección Final \n\nSKU CORREGIDO. OLA ",len(ListaPedidosSeparadosFinal)," Rutas \n")
    print(len(ListaPedidosSeparadosFinal))
    print(ListaPedidosSeparadosFinal)
    
    print("PRUEBA CANTIDAD")
    print("Pedidos Cola Agrupados",Pedidos_Cola_Agrupados)
    print("Articulos en cola separados",Artic_Pedidos_Cola_Agrupados)
    print("Cantidad Pedidos",cant_prod)
    print("Ruta Recoleccion Optimizada: ",ListaPedidosSeparadosFinal)
    print("Ruta Recoleccion Optimizada [0]: ",ListaPedidosSeparadosFinal[0])
    #Estructura : Producto, Pasillo , Ubicación
    print("\n\n")
    
    #Removemos los brackets externos y generamos una unica lista de producto rutas de recolección.
    
    #Lista de listas pedido y recolección
    listaRecolec=[]
    for i in ListaPedidosSeparadosFinal[0]:
        listaRecolec.append(list(i[0]))
    
    print("LISTA RECOLEC \n\n")
    print(listaRecolec)
    print(len(listaRecolec))
    
    #Para asignar correctamente la cantidad de productos genramos una lista con los diferentes productos y sus cantidades.
    listaCantidades=[]
    
    print("\n\n")
    int_cont=0
    for i in Artic_Pedidos_Cola_Agrupados:
        for j in i:
            listaCantidades.append([j,cant_prod[int_cont]])
            int_cont+=1
                            
    print("LISTA CANTIDADES")
    print(listaCantidades)
    print(len(listaCantidades))
    
    #Ahora simplemente compraramos los productos y asignamos la cantidad a recolectar para cada producto.
    print("\n\n")
    print("FINAL")
    ListaRecolecFinal_SKU_Cantidad=[]

    #Generamos una copia para borrar aquellos articulos que se repitan en diferentes pedidos y no repetir cantidades
    listaCantidadesTemp=listaCantidades.copy()
    for i in listaRecolec:
        ListaRecolecFinal_SKU_Cantidad.append([i+b for b in listaCantidadesTemp if i[0]==str(b[0])])
        for h in listaCantidadesTemp:
            if i[0]==str(h[0]):
                listaCantidadesTemp.remove(h)
                #Rompemos con la iteracion para no borrar todos los elementos de la lista y continuar con el ciclo de arriba
                break

    print("LIsta Recoleccion SKU FINAL CANTIDAD")
    print(ListaRecolecFinal_SKU_Cantidad)
    
    print("\n\n")
    #Removemos los brackets externos de cada elemento
    ListaRecolecFinal_SKU_Cantidad_wt_brack=[]
    for i in ListaRecolecFinal_SKU_Cantidad:
        ListaRecolecFinal_SKU_Cantidad_wt_brack.append(i[0])
    
    print(ListaRecolecFinal_SKU_Cantidad_wt_brack)
    
    #Removemos el primer elemento que se repite y tenemos
    # [Pasillo, Ubicación, Articulo, Cantidad ]
    
    listaRecolec_OPT_Articulo_Cantidad=[]
    for i in ListaRecolecFinal_SKU_Cantidad_wt_brack:
        listaRecolec_OPT_Articulo_Cantidad.append(i[1:])
    
    print("Indicaciones Recolección Finales")
    print(agrupador)
    print(type(agrupador))
    print(listaRecolec_OPT_Articulo_Cantidad)
            

    
    return agrupador,listaRecolec_OPT_Articulo_Cantidad

#Pedidos_Cola_Agrupados=[[1085, 613090, 380, 612424, 612425], [613155, 613086, 613217, 613156]]
#Artic_Pedidos_Cola_Agrupados=[[[85, 39, 74819, 72942, 72949, 74817, 72950, 74650], [5525, 84, 38, 43, 8714, 39, 49, 40, 41, 2332, 2333, 85, 10965, 42, 44], [38, 52, 51, 18248, 44, 43, 18250, 53, 54, 18249, 18237, 41, 7703, 17171, 55, 18238, 17170, 7098, 9444, 40, 9320, 37, 9767], [18250, 9767, 9444, 17171, 51, 18237, 18249, 18248, 38, 53, 54, 55, 37, 41, 44, 18238, 52, 40, 43, 17170], [7703]], [[53, 55, 75, 51, 54, 38, 5525, 42, 73, 77, 78, 52, 37, 41, 2332, 74, 39, 81, 40], [89, 48, 51, 75, 26255, 42, 1920, 92, 39, 90, 5525, 389, 79, 41], [5525, 8508, 18238, 19231, 7703, 5630, 5936, 10965, 19228, 6280, 8200, 8502, 8507, 13127], [91, 89, 90, 49, 90, 91, 376, 376, 89, 49]]]
#RutaRecolec_Pedidos_Agrupados=[[('A2', 30101), ('A2', 30101), ('A2', 30101), ('A2', 30101), ('B1', 30136), ('D1', 7835), ('D1', 7835), ('D1', 7840), ('D1', 7840), ('D1', 7850), ('D1', 7850), ('D1', 7855), ('D1', 7855), ('D1', 7855), ('D1', 7860), ('D1', 7860), ('D1', 7865), ('D1', 7885), ('D1', 7895), ('D1', 7915), ('D1', 7965), ('D1', 7965), ('D1', 7970), ('D1', 7970), ('D1', 7975), ('D1', 7975), ('D1', 7980), ('D1', 7980), ('D2', 9280), ('D2', 9285), ('D2', 9285), ('D2', 9290), ('D2', 9290), ('D2', 9290), ('D2', 9300), ('D2', 9300), ('D2', 9305), ('D2', 9305), ('D2', 9305), ('D2', 9315), ('D2', 9315), ('D2', 9320), ('D2', 9340), ('D2', 9345), ('D2', 9345), ('D2', 9345), ('D2', 9350), ('D2', 9350), ('D2', 9370), ('D2', 9380), ('D2', 9380), ('D2', 9385), ('D2', 9385), ('D2', 9405), ('D2', 9405), ('D2', 9415), ('D2', 9415), ('D2', 9420), ('D2', 9420), ('D2', 107605), ('D2', 107610), ('B2', 106885), ('E1', 10730), ('E1', 10730), ('E1', 10765), ('G1', 16475), ('E2', 12250), ('A2', 30101), ('D1', 7835), ('D1', 7840), ('D1', 7845), ('D1', 7850), ('D1', 7860), ('D1', 7865), ('D1', 7870), ('D1', 7870), ('D1', 7875), ('D1', 7885), ('D1', 7885), ('D1', 7885), ('D1', 7895), ('D1', 7895), ('D1', 7905), ('D1', 7925), ('D1', 7925), ('D1', 7925), ('D1', 7950), ('D2', 9280), ('D2', 9280), ('D2', 9285), ('D2', 9285), ('D2', 9290), ('D2', 9295), ('D2', 9295), ('D2', 9295), ('D2', 9300), ('D2', 9305), ('D2', 9305), ('D2', 9310), ('D2', 9315), ('D2', 9315), ('D2', 9325), ('D2', 9325), ('D2', 9340), ('D2', 9355), ('D2', 9360), ('D2', 9385), ('D2', 9445), ('D2', 9500), ('E1', 10730), ('E1', 10750), ('E1', 10755), ('E1', 10775), ('E1', 10785), ('E1', 10785), ('E1', 10820), ('E1', 10850), ('E1', 10865), ('E2', 12285), ('E2', 12295), ('E2', 12310), ('E2', 12315), ('C1', 5150), ('C1', 5160)], [('A2', 30101), ('A2', 30101), ('A2', 30101), ('A2', 30101), ('B1', 30136), ('D1', 7835), ('D1', 7835), ('D1', 7840), ('D1', 7840), ('D1', 7850), ('D1', 7850), ('D1', 7855), ('D1', 7855), ('D1', 7855), ('D1', 7860), ('D1', 7860), ('D1', 7865), ('D1', 7885), ('D1', 7895), ('D1', 7915), ('D1', 7965), ('D1', 7965), ('D1', 7970), ('D1', 7970), ('D1', 7975), ('D1', 7975), ('D1', 7980), ('D1', 7980), ('D2', 9280), ('D2', 9285), ('D2', 9285), ('D2', 9290), ('D2', 9290), ('D2', 9290), ('D2', 9300), ('D2', 9300), ('D2', 9305), ('D2', 9305), ('D2', 9305), ('D2', 9315), ('D2', 9315), ('D2', 9320), ('D2', 9340), ('D2', 9345), ('D2', 9345), ('D2', 9345), ('D2', 9350), ('D2', 9350), ('D2', 9370), ('D2', 9380), ('D2', 9380), ('D2', 9385), ('D2', 9385), ('D2', 9405), ('D2', 9405), ('D2', 9415), ('D2', 9415), ('D2', 9420), ('D2', 9420), ('D2', 107605), ('D2', 107610), ('B2', 106885), ('E1', 10730), ('E1', 10730), ('E1', 10765), ('G1', 16475), ('E2', 12250), ('A2', 30101), ('D1', 7835), ('D1', 7840), ('D1', 7845), ('D1', 7850), ('D1', 7860), ('D1', 7865), ('D1', 7870), ('D1', 7870), ('D1', 7875), ('D1', 7885), ('D1', 7885), ('D1', 7885), ('D1', 7895), ('D1', 7895), ('D1', 7905), ('D1', 7925), ('D1', 7925), ('D1', 7925), ('D1', 7950), ('D2', 9280), ('D2', 9280), ('D2', 9285), ('D2', 9285), ('D2', 9290), ('D2', 9295), ('D2', 9295), ('D2', 9295), ('D2', 9300), ('D2', 9305), ('D2', 9305), ('D2', 9310), ('D2', 9315), ('D2', 9315), ('D2', 9325), ('D2', 9325), ('D2', 9340), ('D2', 9355), ('D2', 9360), ('D2', 9385), ('D2', 9445), ('D2', 9500), ('E1', 10730), ('E1', 10750), ('E1', 10755), ('E1', 10775), ('E1', 10785), ('E1', 10785), ('E1', 10820), ('E1', 10850), ('E1', 10865), ('E2', 12285), ('E2', 12295), ('E2', 12310), ('E2', 12315), ('C1', 5150), ('C1', 5160)]]


#AsignacionSKU_Correcto_RutaRecolec_Olas(Pedidos_Cola_Agrupados,Artic_Pedidos_Cola_Agrupados,RutaRecolec_Pedidos_Agrupados)
