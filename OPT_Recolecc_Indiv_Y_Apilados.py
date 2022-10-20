# -*- coding: utf-8 -*-
"""

@author: Alban Rodríguez


"""

import Generador_Coord as GC
import Shortest_Func as SF
import AsignacionSKU_Correccion as Asig_SKU

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import glob
import itertools


def OPT_Recolec_Optima_Indiv(nombreArchivo_pedidosCola):
    #Programa de optimización de distancias para recolección individual.
    #Generalizado
    
    #############################################################################
    #Cargamos la geometría del almacen
    #Generamos las coordenadas y el diccionario con ubicaciones y propiedades asignadas
    Dic_Prod,Dic_Prod_coordenadas,X_lis,Y_lis,ID_Pasillo_lis,ID_Ubicacion_lis,List_Coor=GC.Calc_Coord_desde_Excel("Ubicaciones")
    #Obtenemos todas las llaves disponibles y las metemos en una lista
    todas_ubic_disponibles=list(Dic_Prod.keys())
    #print(Dic_Prod_coordenadas)
    #print(Dic_Prod)
    #Generaremos un diccionario en donde se relaciona cad producto con sus ubicaciones en almacen
    name_col=["SKU_PRODUCTO","ID_Ubic"]
    ProdUbic = pd.read_csv("Ubicaciones.csv", usecols=name_col)
    #Casteamos a una lista
    SKU=ProdUbic['SKU_PRODUCTO'].tolist()
    ID_Ubic=ProdUbic['ID_Ubic'].tolist()
    #Generamos un diccionario con productos y sus ubicaciones
    DicProducUbic=dict(zip(SKU,ID_Ubic))
    #print(DicProducUbic)
    
    
    ########################################################################
    
    #Observamos la geometría y ubicaciones asignadas del almacen.
    plt.figure(1)
    plt.rcParams.update({'font.size': 28})
    plt.scatter(X_lis,Y_lis,color="red")
    plt.title("Geometría y Dimensiones del Almacen")
    plt.xlabel("Distancia entre pasillos [metros]")
    plt.ylabel("Longitud de los pasillos [metros]")
    plt.show()
    
    
    
    #leemos los pedidos que se ncuentran en cola
    name_col=["documento","producto","cantidad"]
    pedidos = pd.read_csv("PedidosEnCola/"+nombreArchivo_pedidosCola+".csv", usecols=name_col)
    
    #Agrupamos todos los productos que están pendientes
    producto_list=pedidos['producto'].tolist()
    
    #Almacenamos las ordenes pendientes sin importar si se repiten o no
    #Ya que cada renglon de producto nos indica a que pedido pertenece
    Pedidos_pendientes_rep=pedidos['documento'].tolist()
    print(Pedidos_pendientes_rep)
    Pedidos_pendientes=[] #Removemos los elementos repetidos sin alterar el orden
    [Pedidos_pendientes.append(i) for i in Pedidos_pendientes_rep if i not in Pedidos_pendientes]
    
    print("Todos Los pedidos pendintes Sin repetir: ",Pedidos_pendientes)
    
    
    print("Hay %1.0f ordenes en cola"%len(Pedidos_pendientes),"\nLos pedidos en cola son: ", Pedidos_pendientes,"\n")
    
    #Calculamos como booleanos los diferentes productos solicitados en lista para separarles por orden
    listaDiferentesOrdenes_bool=[]
    for i in Pedidos_pendientes:
        listaDiferentesOrdenes_bool.append((pedidos['documento'] == i).tolist())
    print(len(listaDiferentesOrdenes_bool))
   #print(listaDiferentesOrdenes_bool)
    
    #Generamos listas con los indices de cada pedido.
    #Agrupamos en una lista para cada pedido con los indices de cada pedido
    listaIndicesPedidos=[]
    numeroPedidos=len(Pedidos_pendientes)
    for i in listaDiferentesOrdenes_bool:
        listaIndicesPedidos.append([j for j, x in enumerate(i) if x])
    #print(listaIndicesPedidos)
    
    
    #Agrupamos los diferente  s productos de cada pedido dados los indices encontrados
    ListaProductosTodosLosPedidosSeparados=[]
    for i in listaIndicesPedidos:
        ListaProductosTodosLosPedidosSeparados.append([producto_list[j] for j in i])
    #Mostramos al usuario los pedidos y todos los artciculos de cada pedido
    cont1=0
    for i in Pedidos_pendientes:
        print("Pedido :",i)
        print("Articulos:\n",ListaProductosTodosLosPedidosSeparados[cont1],"\n")
        cont1+=1
    
    print("Pedidos Pendientes: ",Pedidos_pendientes)
    print("Articulos pendientes por pedido: ",ListaProductosTodosLosPedidosSeparados)
    
    #Ahora asignamos las ubicaciones para cada uno de los producos en los pedidos
    listaUbicacionesProductosPorPedido=[]
    for i in ListaProductosTodosLosPedidosSeparados:
        listaUbicacionesProductosPorPedido.append([DicProducUbic[str(x)] for x in i])
    
    
    #Generamos una lista donde se almacenan las coordenadas de recolección de cada pedido por separado
    ListaCoordRecolecNoOptim=[]
    for i in listaUbicacionesProductosPorPedido:
        ListaCoordRecolecNoOptim.append(SF.asig_coord_desde_pedido(i,Dic_Prod))
    #Podemos imprimir las corrdenadas de recolección antes de la optimización
    cont2=0    
    for i in Pedidos_pendientes:
        print("Pedido :",i)
        print("Recolección antes de optimizar:\n",ListaCoordRecolecNoOptim[cont2],"\n")
        cont2+=1
    ######
    ########
    ###########
    ############# Hasta aquí ya se cotejó que las salidas en terminal correspondan con las ubicaciones y productos por pedido comparando con el excel de ubicaicones
    
    #Asumiremos que el origen y en donde queremos que termine nuestro recorrido es
    #la coordenada (0,0), es decir Pasillo A, ID_Ubicacion 5
    origin_loc=(0,0)
    
    #Conocemos las dimensiones del almacen
    y_inf=0
    y_sup=76
    
    #Optimizamos ruta recollección
    
    ListaCoordRecolecOPTIMAS_PedidoIndividual_Distancia=[]
    for i in ListaCoordRecolecNoOptim:
        ListaCoordRecolecOPTIMAS_PedidoIndividual_Distancia.append(SF.generar_ruta_recog(origin_loc,i,y_inf,y_sup))
    print(ListaCoordRecolecOPTIMAS_PedidoIndividual_Distancia)# Hasta este punto seguimos considerando el origen como partida y retorno en el calculo de la distancia
    print("PedidosDistanciaLen: ",len(ListaCoordRecolecOPTIMAS_PedidoIndividual_Distancia))
    
    #Aqui tendremos una lista donde vienen como tuplas tanto la distancia total como las coordenadas de recolección optimas por cada pedido-
    ListaCoordRecolecOPTIMAS_Indvid_coord=[]
    for i in ListaCoordRecolecOPTIMAS_PedidoIndividual_Distancia:
        #print(i,"\n")
        ListaCoordRecolecOPTIMAS_Indvid_coord.append(i[1])
    #print(ListaCoordRecolecOPTIMAS_Indvid_coord)
    ######
    ########
    ###########
    ############# Hasta aquí ya se cotejó que las salidas en terminal correspondan con las ubicaciones y productos por pedido comparando con el excel de ubicaicones

    
    
    
    #Almacenaremos las indicaciones de recolección en un archivo .csv
    
    Indicaciones_Recolec_Sep=[]
    Indicaciones_Recolec_Sep_sin_Texto=[]
    Indicaciones_Recolec_Juntas=[]
    Indicaciones_Recolec_Juntas_sin_Texto=[]
    for i in ListaCoordRecolecOPTIMAS_Indvid_coord:
        #Indicaciones_Recolec_Sep.append(Indicaciones_Recolec_Juntas)
        Indicaciones_Recolec_Juntas=[]#Vaciamos la lista para no encimar los pedidos
        Indicaciones_Recolec_Juntas_sin_Texto=[]
        #Removemos el inicio y final si no se quiere temrinar donde se empezó
        i=i[1:-1]
        for j in i:
            Indicaciones_Recolec_Juntas.append(("Dirigete al Pasillo:",Dic_Prod_coordenadas.get(j)[0],"Ubicacion: ",Dic_Prod_coordenadas.get(j)[1],"Por el SKU: ",Dic_Prod_coordenadas.get(j)[2]))
            Indicaciones_Recolec_Juntas_sin_Texto.append((Dic_Prod_coordenadas.get(j)[0],Dic_Prod_coordenadas.get(j)[1]))
            print(j)
        Indicaciones_Recolec_Sep.append(Indicaciones_Recolec_Juntas)
        Indicaciones_Recolec_Sep_sin_Texto.append(Indicaciones_Recolec_Juntas_sin_Texto)
    
    
    print("Recoleccióin Sin Texto: ",Indicaciones_Recolec_Sep_sin_Texto )
    print(len(Indicaciones_Recolec_Sep))
    #Imprimimos la ruta de recolección para cada pedido con sus respectivos productos.
    cont3=0
    for i in Pedidos_pendientes:
        print("Pedido :",i)
        print("Articulos:\n",ListaProductosTodosLosPedidosSeparados[cont3],"\n")
        print("Instrucciones de recolección\n",Indicaciones_Recolec_Sep[cont3],"\n")
        
        cont3+=1
    print("Indicaciones Recolección Pedidos: ")
    
    #Asignamoc correctamente los SKU a las indicaciones de recolección.
    
    #Variables 
    #print(Pedidos_pendientes)
    #print(ListaProductosTodosLosPedidosSeparados)
    #print(Indicaciones_Recolec_Sep_sin_Texto)
    
    
    RutaRecolec_OPT_SKUcorregido=Asig_SKU.AsignacionSKU_Correcto_RutaRecolec(Pedidos_pendientes,ListaProductosTodosLosPedidosSeparados,Indicaciones_Recolec_Sep_sin_Texto)
    
    print(RutaRecolec_OPT_SKUcorregido)
    
    ##LLenamos Un archivo con la ruta de recolección de los pedidos:
    Indicaciones_Recolec_Sep_01=[]
    Indicaciones_Recolec_Juntas_01=[]
    
    for i in ListaCoordRecolecOPTIMAS_Indvid_coord:
        #Indicaciones_Recolec_Sep.append(Indicaciones_Recolec_Juntas)
        Indicaciones_Recolec_Juntas_01=[] #Vaciamos la lista para no encimar los pedidos
        #Removemos el inicio y final si no se quiere temrinar donde se empezó
        i=i[1:-1]
        for j in i:
            Indicaciones_Recolec_Juntas_01.append((Dic_Prod_coordenadas.get(j)[0],Dic_Prod_coordenadas.get(j)[1]))
            #print(j)
        Indicaciones_Recolec_Sep_01.append(Indicaciones_Recolec_Juntas_01)
    print(Indicaciones_Recolec_Sep_01)
    
    
    
    #Almacenamos las indicaciones de recolección para cada pedido en un archivo de excel
    
    csv_content = Pedidos_pendientes,ListaProductosTodosLosPedidosSeparados,Indicaciones_Recolec_Sep
    csv_file =  open("Recoleccion_Optima/OPT_recolec_INDV.csv", 'w')
    
    csv_writer = csv.writer(csv_file, delimiter=",")
    
    for row in csv_content:
        csv_writer.writerow(row)
        
    csv_file.close()
    
    print(ListaProductosTodosLosPedidosSeparados)
    
    
    return Pedidos_pendientes,ListaProductosTodosLosPedidosSeparados,Indicaciones_Recolec_Sep

def OPT_Recolec_Optima_Apilar3Pedidos(nombreArchivo_pedidosCola):
    
    #############################################################################
    #Cargamos la geometría del almacen
    #Generamos las coordenadas y el diccionario con ubicaciones y propiedades asignadas
    Dic_Prod,Dic_Prod_coordenadas,X_lis,Y_lis,ID_Pasillo_lis,ID_Ubicacion_lis,List_Coor=GC.Calc_Coord_desde_Excel("Ubicaciones")
    #Obtenemos todas las llaves disponibles y las metemos en una lista
    todas_ubic_disponibles=list(Dic_Prod.keys())
    #print(Dic_Prod_coordenadas)
    #print(Dic_Prod)
    #Generaremos un diccionario en donde se relaciona cad producto con sus ubicaciones en almacen
    name_col=["SKU_PRODUCTO","ID_Ubic"]
    ProdUbic = pd.read_csv("Ubicaciones.csv", usecols=name_col)
    #Casteamos a una lista
    SKU=ProdUbic['SKU_PRODUCTO'].tolist()
    ID_Ubic=ProdUbic['ID_Ubic'].tolist()
    #Generamos un diccionario con productos y sus ubicaciones
    DicProducUbic=dict(zip(SKU,ID_Ubic))
    #print(DicProducUbic)
    
    
    ########################################################################
    
    #Observamos la geometría y ubicaciones asignadas del almacen.
    plt.figure(1)
    plt.rcParams.update({'font.size': 28})
    plt.scatter(X_lis,Y_lis,color="red")
    plt.title("Geometría y Dimensiones del Almacen")
    plt.xlabel("Distancia entre pasillos [metros]")
    plt.ylabel("Longitud de los pasillos [metros]")
    plt.show()
    
    
    
    #leemos los pedidos que sencuentran en cola
    name_col=["documento","producto","cantidad","Fecha_hora_ingreso"]
    pedidos = pd.read_csv("PedidosEnCola/"+nombreArchivo_pedidosCola+".csv", usecols=name_col)
    
    #Agrupamos todos los productos que están pendientes
    producto_list=pedidos['producto'].tolist()
    
    #Almacenamos las ordenes pendientes sin importar si se repiten o no
    Pedidos_pendientes_rep=pedidos['documento'].tolist()
    Pedidos_pendientes=[] #Removemos los elementos repetidos sin alterar el orden
    [Pedidos_pendientes.append(i) for i in Pedidos_pendientes_rep if i not in Pedidos_pendientes]
    
    
    
    
    print("Hay %1.3f ordenes en cola"%len(Pedidos_pendientes),"\nLos pedidos en cola son: ", Pedidos_pendientes,"\n")
    
    #Calculamos como booleanos los diferentes productos solicitados en lista para separarles por orden
    listaDiferentesOrdenes_bool=[]
    for i in Pedidos_pendientes:
        listaDiferentesOrdenes_bool.append((pedidos['documento'] == i).tolist())
    print(len(listaDiferentesOrdenes_bool))
    
    #Generamos listas con los indices de cada pedido.
    #Agrupamos en una lista para cada pedido con los indices de cada pedido
    listaIndicesPedidos=[]
    numeroPedidos=len(Pedidos_pendientes)
    for i in listaDiferentesOrdenes_bool:
        listaIndicesPedidos.append([j for j, x in enumerate(i) if x])
    #print(listaIndicesPedidos)
    
    
    #Agrupamos los diferentees productos de cada pedido dados los indices encontrados
    ListaProductosTodosLosPedidosSeparados=[]
    for i in listaIndicesPedidos:
        ListaProductosTodosLosPedidosSeparados.append([producto_list[j] for j in i])
    #Mostramos al usuario los pedidos y todos los artciculos de cada pedido
    cont1=0
    for i in Pedidos_pendientes:
        print("Pedido :",i)
        print("Articulos:\n",ListaProductosTodosLosPedidosSeparados[cont1],"\n")
        cont1+=1
    
    
    #Ahora asignamos las ubicaciones para cada uno de los producos en los pedidos
    listaUbicacionesProductosPorPedido=[]
    for i in ListaProductosTodosLosPedidosSeparados:
        listaUbicacionesProductosPorPedido.append([DicProducUbic[str(x)] for x in i])
    
    #Generamos una lista donde se almacenan las coordenadas de recolección de cada pedido por separado
    ListaCoordRecolecNoOptim=[]
    for i in listaUbicacionesProductosPorPedido:
        ListaCoordRecolecNoOptim.append(SF.asig_coord_desde_pedido(i,Dic_Prod))
    #Podemos imprimir las corrdenadas de recolección antes de la optimización
    cont2=0    
    for i in Pedidos_pendientes:
        print("Pedido :",i)
        print("Recolección antes de optimizar:\n",ListaCoordRecolecNoOptim[cont2],"\n")
        cont2+=1
        
        
    #Funcion que agrupa los pedidos por mes en olas de N pedidos cada una.
    def agruparPedidosOleadasNpedidos(listaPedidosSeparados,N):
        listapedidosAgrupadosOleada=[]
        CantidadPedidodsOrig=listaPedidosSeparados
        for i in range(0,len(listaPedidosSeparados),1):
            listapedidosAgrupadosOleada.append(listaPedidosSeparados[:N])
            listaPedidosSeparados=listaPedidosSeparados[N:]
            listapedidosAgrupadosOleada = [ele for ele in listapedidosAgrupadosOleada if ele != []]
        print("Cantidad de pedidos sin agrupar: ", len(CantidadPedidodsOrig))
        print("Los pedidos se agruparon en: ", len(listapedidosAgrupadosOleada),"olas", "\nCada ola tiene máximo ",N,"pedidos")
        #Juntamos las coordenadas de cada ola para manipularlas adecuadamente como una sola lista
        ListaCoordenadasOlas=[list(itertools.chain(i)) for i in listapedidosAgrupadosOleada]
        print(ListaCoordenadasOlas)
        return ListaCoordenadasOlas
    
    #Desempaquetamos las coordenadas en listas por pedido por .
    
    def funcionAgrupadora(lista_pedidosAgrupados):
        pedidosAgrupados2 = []
        for k in lista_pedidosAgrupados:
            lista2=[]
            for i in k:
                for j in range(len(i)):
                    elemento = k[k.index(i)][j]
                    lista2.append(elemento)
            pedidosAgrupados2.append(lista2)
        return pedidosAgrupados2
    
    pedidosAgrupadosOleada3_noOptim=funcionAgrupadora(agruparPedidosOleadasNpedidos(ListaCoordRecolecNoOptim,3))
    
    #Ahora alimentemos el programa generado con cada uno de estos pedidos_ENERO_2019 de forma individual

    #Asumiremos que el origen y en donde queremos que termine nuestro recorrido es
    #la coordenada (0,0), es decir Pasillo A, ID_Ubicacion 5
    origin_loc=(0,0)
    
    #Conocemos las dimensiones del almacen
    y_inf=0
    y_sup=76
    
    ListaCoordRecolecOPTIMAS_OLA_3_distancia=[]
    
    #OPTIMIZACIÓN OLAS 3 PEDIDOS
    for i in pedidosAgrupadosOleada3_noOptim:
        ListaCoordRecolecOPTIMAS_OLA_3_distancia.append(SF.generar_ruta_recog(origin_loc,i,y_inf,y_sup))
        
    
    
    
    
        
    
    print(ListaCoordRecolecOPTIMAS_OLA_3_distancia)# Hasta este punto seguimos considerando el origen como partida y retorno en el calculo de la distancia
    print("PedidosDistanciaLen: ",len(ListaCoordRecolecOPTIMAS_OLA_3_distancia))
    
    #Aqui tendremos una lista donde vienen como tuplas tanto la distancia total como las coordenadas de recolección optimas por cada pedido-
    ListaCoordRecolecOPTIMAS_Ola3_coord=[]
    #Separamos las distancias calculadas de las rutas de recolección
    for i in ListaCoordRecolecOPTIMAS_OLA_3_distancia:
        print(i,"\n")
        ListaCoordRecolecOPTIMAS_Ola3_coord.append(i[1])
    print(ListaCoordRecolecOPTIMAS_Ola3_coord)
    
    
    #Almacenaremos las indicaciones de recolección en un archivo .csv
    
    Indicaciones_Recolec_Sep=[]
    Indicaciones_Recolec_Juntas=[]
    Indicaciones_Recolec_Sep_sin_Texto=[]
    Indicaciones_Recolec_Juntas_sin_Texto=[]

    
    for i in ListaCoordRecolecOPTIMAS_Ola3_coord:
        #Indicaciones_Recolec_Sep.append(Indicaciones_Recolec_Juntas)
        Indicaciones_Recolec_Juntas=[] #Vaciamos la lista para no encimar los pedidos
        Indicaciones_Recolec_Juntas_sin_Texto=[]
        #Removemos el inicio y final si no se quiere temrinar donde se empezó
        i=i[1:-1]
        for j in i:
            Indicaciones_Recolec_Juntas.append(("Dirigete al Pasillo:",Dic_Prod_coordenadas.get(j)[0],"Ubicacion: ",Dic_Prod_coordenadas.get(j)[1],"Por el SKU: ",Dic_Prod_coordenadas.get(j)[2]))
            Indicaciones_Recolec_Juntas_sin_Texto.append((Dic_Prod_coordenadas.get(j)[0],Dic_Prod_coordenadas.get(j)[1]))
            print(j)
        Indicaciones_Recolec_Sep.append(Indicaciones_Recolec_Juntas)
        Indicaciones_Recolec_Sep_sin_Texto.append(Indicaciones_Recolec_Juntas_sin_Texto)
    
    print("Indicaciones Recolección Sin Texto \n\n")
    print(len(Indicaciones_Recolec_Sep_sin_Texto))
    print(Indicaciones_Recolec_Sep_sin_Texto)
    
    print(len(Indicaciones_Recolec_Sep))
    
    #Agrupamos los pedidos en N olas para su correcta visualización
    n = 3
    Pedidos_agrupados = [Pedidos_pendientes[i:i+n] for i in range(0, len(Pedidos_pendientes), n)]
    #print("Pedidossssssssssssssss Agrupados")
    #print(Pedidos_agrupados)
    print
    #Agrupamos todos los articulos en N olas para su correcta visualización
    n = 3
    Articulos_Agrupados = [ListaProductosTodosLosPedidosSeparados[i:i+n] for i in range(0, len(ListaProductosTodosLosPedidosSeparados), n)]
    #print("Articulossssssssss Agrupados")
    #print(Articulos_Agrupados)
    
    
    #Imprimimos la ruta de recolección para cada pedido con sus respectivos productos.
    cont3=0
    for i in Pedidos_agrupados:
        
        print("Pedido :",i)
        print("Articulos:\n",Articulos_Agrupados[cont3],"\n")
        print("Instrucciones de recolección\n",Indicaciones_Recolec_Sep[cont3],"\n")
        
        cont3+=1
    
    #Asignamos correctamente los SKU a las indicaciones de recolección.
    
    #Variables 
    print("Variablesssss")
    print(len(Pedidos_agrupados))
    print(Pedidos_agrupados)
    print(len(Articulos_Agrupados))
    print(Articulos_Agrupados)
    print(Indicaciones_Recolec_Sep_sin_Texto)
    
    
    RutaRecolec_OPT_SKUcorregido=Asig_SKU.AsignacionSKU_Correcto_RutaRecolec_Olas(Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep_sin_Texto)
    
    
    print("Recolección SKU FINAL: \n\n")
    print(RutaRecolec_OPT_SKUcorregido)
    
    #Almacenamos las indicaciones de recolección para cada pedido en un archivo de excel
    
    csv_content = Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep
    csv_file =  open("Recoleccion_Optima/OPT_recolec_Ola3.csv", 'w')
    
    csv_writer = csv.writer(csv_file, delimiter=",")
    
    for row in csv_content:
        csv_writer.writerow(row)
        
    csv_file.close()
    
    return Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep

def OPT_Recolec_Optima_Apilar5Pedidos(nombreArchivo_pedidosCola):
    
    #############################################################################
    #Cargamos la geometría del almacen
    #Generamos las coordenadas y el diccionario con ubicaciones y propiedades asignadas
    Dic_Prod,Dic_Prod_coordenadas,X_lis,Y_lis,ID_Pasillo_lis,ID_Ubicacion_lis,List_Coor=GC.Calc_Coord_desde_Excel("Ubicaciones")
    #Obtenemos todas las llaves disponibles y las metemos en una lista
    todas_ubic_disponibles=list(Dic_Prod.keys())
    #print(Dic_Prod_coordenadas)
    #print(Dic_Prod)
    #Generaremos un diccionario en donde se relaciona cad producto con sus ubicaciones en almacen
    name_col=["SKU_PRODUCTO","ID_Ubic"]
    ProdUbic = pd.read_csv("Ubicaciones.csv", usecols=name_col)
    #Casteamos a una lista
    SKU=ProdUbic['SKU_PRODUCTO'].tolist()
    ID_Ubic=ProdUbic['ID_Ubic'].tolist()
    #Generamos un diccionario con productos y sus ubicaciones
    DicProducUbic=dict(zip(SKU,ID_Ubic))
    #print(DicProducUbic)
    
    
    ########################################################################
    
    #Observamos la geometría y ubicaciones asignadas del almacen.
    plt.figure(1)
    plt.rcParams.update({'font.size': 28})
    plt.scatter(X_lis,Y_lis,color="red")
    plt.title("Geometría y Dimensiones del Almacen")
    plt.xlabel("Distancia entre pasillos [metros]")
    plt.ylabel("Longitud de los pasillos [metros]")
    plt.show()
    
    
    
    #leemos los pedidos que sencuentran en cola
    name_col=["documento","producto","cantidad"]
    pedidos = pd.read_csv("PedidosEnCola/"+nombreArchivo_pedidosCola+".csv", usecols=name_col)
    
    #Guardamos el número de agrupador
    df=pd.read_csv("PedidosEnCola/"+nombreArchivo_pedidosCola+".csv")
    agrupador=df.iloc[:, [3]]
    agrupador=agrupador.columns.values
    agrupador=list(agrupador)
    #Agrupamos todos los productos que están pendientes
    producto_list=pedidos['producto'].tolist()
    
    #Almacenamos las ordenes pendientes sin importar si se repiten o no
    Pedidos_pendientes_rep=pedidos['documento'].tolist()
    Pedidos_pendientes=[] #Removemos los elementos repetidos sin alterar el orden
    [Pedidos_pendientes.append(i) for i in Pedidos_pendientes_rep if i not in Pedidos_pendientes]
    
    
    
    
    print("Hay %1.3f ordenes en cola"%len(Pedidos_pendientes),"\nLos pedidos en cola son: ", Pedidos_pendientes,"\n")
    
    #Calculamos como booleanos los diferentes productos solicitados en lista para separarles por orden
    listaDiferentesOrdenes_bool=[]
    for i in Pedidos_pendientes:
        listaDiferentesOrdenes_bool.append((pedidos['documento'] == i).tolist())
    print(len(listaDiferentesOrdenes_bool))
    
    #Generamos listas con los indices de cada pedido.
    #Agrupamos en una lista para cada pedido con los indices de cada pedido
    listaIndicesPedidos=[]
    numeroPedidos=len(Pedidos_pendientes)
    for i in listaDiferentesOrdenes_bool:
        listaIndicesPedidos.append([j for j, x in enumerate(i) if x])
    #print(listaIndicesPedidos)
    
    
    #Agrupamos los diferentees productos de cada pedido dados los indices encontrados
    ListaProductosTodosLosPedidosSeparados=[]
    for i in listaIndicesPedidos:
        ListaProductosTodosLosPedidosSeparados.append([producto_list[j] for j in i])
    #Mostramos al usuario los pedidos y todos los artciculos de cada pedido
    cont1=0
    for i in Pedidos_pendientes:
        print("Pedido :",i)
        print("Articulos:\n",ListaProductosTodosLosPedidosSeparados[cont1],"\n")
        cont1+=1
    
    
    #Ahora asignamos las ubicaciones para cada uno de los productos en los pedidos
    listaUbicacionesProductosPorPedido=[]
    for i in ListaProductosTodosLosPedidosSeparados:
        listaUbicacionesProductosPorPedido.append([DicProducUbic[str(x)] for x in i])
    
    #Generamos una lista donde se almacenan las coordenadas de recolección de cada pedido por separado
    ListaCoordRecolecNoOptim=[]
    for i in listaUbicacionesProductosPorPedido:
        ListaCoordRecolecNoOptim.append(SF.asig_coord_desde_pedido(i,Dic_Prod))
    #Podemos imprimir las corrdenadas de recolección antes de la optimización
    cont2=0    
    for i in Pedidos_pendientes:
        print("Pedido :",i)
        print("Recolección antes de optimizar:\n",ListaCoordRecolecNoOptim[cont2],"\n")
        cont2+=1
        
        
    #Funcion que agrupa los pedidos por mes en olas de N pedidos cada una.
    def agruparPedidosOleadasNpedidos(listaPedidosSeparados,N):
        listapedidosAgrupadosOleada=[]
        CantidadPedidodsOrig=listaPedidosSeparados
        for i in range(0,len(listaPedidosSeparados),1):
            listapedidosAgrupadosOleada.append(listaPedidosSeparados[:N])
            listaPedidosSeparados=listaPedidosSeparados[N:]
            listapedidosAgrupadosOleada = [ele for ele in listapedidosAgrupadosOleada if ele != []]
        print("Cantidad de pedidos sin agrupar: ", len(CantidadPedidodsOrig))
        print("Los pedidos se agruparon en: ", len(listapedidosAgrupadosOleada),"olas", "\nCada ola tiene máximo ",N,"pedidos")
        #Juntamos las coordenadas de cada ola para manipularlas adecuadamente como una sola lista
        ListaCoordenadasOlas=[list(itertools.chain(i)) for i in listapedidosAgrupadosOleada]
        print(ListaCoordenadasOlas)
        return ListaCoordenadasOlas
    
    #Desempaquetamos las coordenadas en listas por pedido por .
    
    def funcionAgrupadora(lista_pedidosAgrupados):
        pedidosAgrupados2 = []
        for k in lista_pedidosAgrupados:
            lista2=[]
            for i in k:
                for j in range(len(i)):
                    elemento = k[k.index(i)][j]
                    lista2.append(elemento)
            pedidosAgrupados2.append(lista2)
        return pedidosAgrupados2
    
    pedidosAgrupadosOleada5_noOptim=funcionAgrupadora(agruparPedidosOleadasNpedidos(ListaCoordRecolecNoOptim,5))
    
    #Ahora alimentemos el programa generado con cada uno de estos pedidos_ENERO_2019 de forma individual

    #Asumiremos que el origen y en donde queremos que termine nuestro recorrido es
    #la coordenada (0,0), es decir Pasillo A, ID_Ubicacion 5
    origin_loc=(0,0)
    
    #Conocemos las dimensiones del almacen
    y_inf=0
    y_sup=76
    
    ListaCoordRecolecOPTIMAS_OLA_5_distancia=[]
    
    #OPTIMIZACIÓN OLAS 5 PEDIDOS
    for i in pedidosAgrupadosOleada5_noOptim:
        ListaCoordRecolecOPTIMAS_OLA_5_distancia.append(SF.generar_ruta_recog(origin_loc,i,y_inf,y_sup))
        
    
    
    
    
        
    
    print(ListaCoordRecolecOPTIMAS_OLA_5_distancia)# Hasta este punto seguimos considerando el origen como partida y retorno en el calculo de la distancia
    print("PedidosDistanciaLen: ",len(ListaCoordRecolecOPTIMAS_OLA_5_distancia))
    
    #Aqui tendremos una lista donde vienen como tuplas tanto la distancia total como las coordenadas de recolección optimas por cada pedido-
    ListaCoordRecolecOPTIMAS_Ola5_coord=[]
    #Separamos las distancias calculadas de las rutas de recolección
    for i in ListaCoordRecolecOPTIMAS_OLA_5_distancia:
        print(i,"\n")
        ListaCoordRecolecOPTIMAS_Ola5_coord.append(i[1])
    print(ListaCoordRecolecOPTIMAS_Ola5_coord)
    
    
    #Almacenaremos las indicaciones de recolección en un archivo .csv
    
    Indicaciones_Recolec_Sep=[]
    Indicaciones_Recolec_Juntas=[]
    Indicaciones_Recolec_Sep_sin_Texto=[]
    Indicaciones_Recolec_Juntas_sin_Texto=[]
    for i in ListaCoordRecolecOPTIMAS_Ola5_coord:
        #Indicaciones_Recolec_Sep.append(Indicaciones_Recolec_Juntas)
        Indicaciones_Recolec_Juntas=[] #Vaciamos la lista para no encimar los pedidos
        #Removemos el inicio y final si no se quiere temrinar donde se empezó
        i=i[1:-1]
        for j in i:
            Indicaciones_Recolec_Juntas.append(("Dirigete al Pasillo:",Dic_Prod_coordenadas.get(j)[0],"Ubicacion: ",Dic_Prod_coordenadas.get(j)[1],"Por el SKU: ",Dic_Prod_coordenadas.get(j)[2]))
            Indicaciones_Recolec_Juntas_sin_Texto.append((Dic_Prod_coordenadas.get(j)[0],Dic_Prod_coordenadas.get(j)[1]))
            print(j)
        Indicaciones_Recolec_Sep.append(Indicaciones_Recolec_Juntas)
        Indicaciones_Recolec_Sep_sin_Texto.append(Indicaciones_Recolec_Juntas_sin_Texto)
    
    
    print("Indicaciones Recolección Sin Texto \n\n")
    print(len(Indicaciones_Recolec_Sep_sin_Texto))
    print(Indicaciones_Recolec_Sep_sin_Texto)
    
    
    #Agrupamos los pedidos en N olas para su correcta visualización
    n = 5
    Pedidos_agrupados = [Pedidos_pendientes[i:i+n] for i in range(0, len(Pedidos_pendientes), n)]
    #print("Pedidos Agrupados")
    #print(Pedidos_agrupados)
    
    #Agrupamos todos los articulos en N olas para su correcta visualización
    n = 5
    Articulos_Agrupados = [ListaProductosTodosLosPedidosSeparados[i:i+n] for i in range(0, len(ListaProductosTodosLosPedidosSeparados), n)]
    #print("Articulossssssssss Agrupados")
    #print(Articulos_Agrupados)
    
    
    #Imprimimos la ruta de recolección para cada pedido con sus respectivos productos.
    cont3=0
    for i in Pedidos_agrupados:
        
        print("Pedido :",i)
        print("Articulos:\n",Articulos_Agrupados[cont3],"\n")
        print("Instrucciones de recolección\n",Indicaciones_Recolec_Sep[cont3],"\n")
        
        cont3+=1
    
    
    #Variables 
    #print("Variables")
    #print(len(Pedidos_agrupados))
    #print(Pedidos_agrupados)
    #print(len(Articulos_Agrupados))
    #print(Articulos_Agrupados)
    #print(len(Indicaciones_Recolec_Sep_sin_Texto))
    #print(Indicaciones_Recolec_Sep_sin_Texto)
    
    #Cantidad productos
    cant_prod=pedidos['cantidad'].tolist()
    
    agrupador,RutaRecolec_OPT_SKUcorregido_Cantidad=Asig_SKU.AsignacionSKU_Correcto_RutaRecolec_Olas(Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep_sin_Texto,cant_prod,agrupador)
    
    print("\n\n")
    print("Agrupador:",agrupador)
    print("Ruta Recoleccion:",RutaRecolec_OPT_SKUcorregido_Cantidad)
    
    #Introducimos texto a la ruta para volver más claro al usuario
    
    indicaciones_Explicitas=[]
    
    for i in RutaRecolec_OPT_SKUcorregido_Cantidad:
        indicaciones_Explicitas.append(["Ubicación: "+str(i[1])+" Producto: "+str(i[2])+" Cantidad: "+ str(i[3])])
    
    print("Indicaciones Explicitas:")
    print(indicaciones_Explicitas)
    
    #Es posible proponer un json de regreso con la misma estructura de entrada o my similar
    
    
    #Implicita
    print("\n\n")
    print("Propuesta JSON Regreso Implicito")
    RecoleccionOptimaImplicita={ 
       "Agrupador":agrupador,
      "Datos":RutaRecolec_OPT_SKUcorregido_Cantidad
    }
    
    print(RecoleccionOptimaImplicita)
    
    
    #Explicita
    print("\n\n")
    print("Propuesta JSON Regreso Explicito")
    RecoleccionOptimaExplicita={ 
       "Agrupador":agrupador,
      "Datos":indicaciones_Explicitas
    }
    
    print(RecoleccionOptimaExplicita) 
    


    
    
    
    
    #print("RUtaRecolec_OPT",RutaRecolec_OPT_SKUcorregido)
    #Almacenamos las indicaciones de recolección para cada pedido en un archivo de excel
    
    #csv_content = Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep
    #csv_file =  open("Recoleccion_Optima/OPT_recolec_Ola5.csv", 'w')
    
    
    #print("Recolección SKU FINAL: \n\n")
    #print(RutaRecolec_OPT_SKUcorregido)
    
    
    #csv_writer = csv.writer(csv_file, delimiter=",")
    
    #for row in csv_content:
    #    csv_writer.writerow(row)
    #    
    #csv_file.close()
    
    return Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep,agrupador,RecoleccionOptimaExplicita

def OPT_Recolec_Optima_Apilar_N_Pedidos_por_ola(nombreArchivo_pedidosCola,agrupar_en_N_pedidos):
    
    #############################################################################
    #Cargamos la geometría del almacen
    #Generamos las coordenadas y el diccionario con ubicaciones y propiedades asignadas
    Dic_Prod,Dic_Prod_coordenadas,X_lis,Y_lis,ID_Pasillo_lis,ID_Ubicacion_lis,List_Coor=GC.Calc_Coord_desde_Excel("Ubicaciones")
    #Obtenemos todas las llaves disponibles y las metemos en una lista
    todas_ubic_disponibles=list(Dic_Prod.keys())
    #print(Dic_Prod_coordenadas)
    #print(Dic_Prod)
    #Generaremos un diccionario en donde se relaciona cad producto con sus ubicaciones en almacen
    name_col=["SKU_PRODUCTO","ID_Ubic"]
    ProdUbic = pd.read_csv("Ubicaciones.csv", usecols=name_col)
    #Casteamos a una lista
    SKU=ProdUbic['SKU_PRODUCTO'].tolist()
    ID_Ubic=ProdUbic['ID_Ubic'].tolist()
    #Generamos un diccionario con productos y sus ubicaciones
    DicProducUbic=dict(zip(SKU,ID_Ubic))
    #print(DicProducUbic)
    
    
    ########################################################################
    
    #Observamos la geometría y ubicaciones asignadas del almacen.
    plt.figure(1)
    plt.rcParams.update({'font.size': 28})
    plt.scatter(X_lis,Y_lis,color="red")
    plt.title("Geometría y Dimensiones del Almacen")
    plt.xlabel("Distancia entre pasillos [metros]")
    plt.ylabel("Longitud de los pasillos [metros]")
    plt.show()
    
    
    
    #leemos los pedidos que sencuentran en cola
    name_col=["documento","producto","cantidad"]
    pedidos = pd.read_csv("PedidosEnCola/"+nombreArchivo_pedidosCola+".csv", usecols=name_col)
    
    #Guardamos el número de agrupador
    df=pd.read_csv("PedidosEnCola/"+nombreArchivo_pedidosCola+".csv")
    agrupador=df.iloc[:, [3]]
    
    agrupador=agrupador.columns.values
    agrupador=list(agrupador)

    #Agrupamos todos los productos que están pendientes
    producto_list=pedidos['producto'].tolist()

    #Almacenamos las ordenes pendientes sin importar si se repiten o no
    Pedidos_pendientes_rep=pedidos['documento'].tolist()
    Pedidos_pendientes=[] #Removemos los elementos repetidos sin alterar el orden
    [Pedidos_pendientes.append(i) for i in Pedidos_pendientes_rep if i not in Pedidos_pendientes]
    
    
    
    
    print("Hay %1.3f ordenes en cola"%len(Pedidos_pendientes),"\nLos pedidos en cola son: ", Pedidos_pendientes,"\n")
    
    #Calculamos como booleanos los diferentes productos solicitados en lista para separarles por orden
    listaDiferentesOrdenes_bool=[]
    for i in Pedidos_pendientes:
        listaDiferentesOrdenes_bool.append((pedidos['documento'] == i).tolist())
    print(len(listaDiferentesOrdenes_bool))
    
    #Generamos listas con los indices de cada pedido.
    #Agrupamos en una lista para cada pedido con los indices de cada pedido
    listaIndicesPedidos=[]
    numeroPedidos=len(Pedidos_pendientes)
    for i in listaDiferentesOrdenes_bool:
        listaIndicesPedidos.append([j for j, x in enumerate(i) if x])
    #print(listaIndicesPedidos)
    
    
    #Agrupamos los diferentees productos de cada pedido dados los indices encontrados
    ListaProductosTodosLosPedidosSeparados=[]
    for i in listaIndicesPedidos:
        ListaProductosTodosLosPedidosSeparados.append([producto_list[j] for j in i])
    #Mostramos al usuario los pedidos y todos los artciculos de cada pedido
    cont1=0
    for i in Pedidos_pendientes:
        print("Pedido :",i)
        print("Articulos:\n",ListaProductosTodosLosPedidosSeparados[cont1],"\n")
        cont1+=1
    
    
    #Ahora asignamos las ubicaciones para cada uno de los productos en los pedidos
    listaUbicacionesProductosPorPedido=[]
    for i in ListaProductosTodosLosPedidosSeparados:
        listaUbicacionesProductosPorPedido.append([DicProducUbic[str(x)] for x in i])
    
    #Generamos una lista donde se almacenan las coordenadas de recolección de cada pedido por separado
    ListaCoordRecolecNoOptim=[]
    for i in listaUbicacionesProductosPorPedido:
        ListaCoordRecolecNoOptim.append(SF.asig_coord_desde_pedido(i,Dic_Prod))
    #Podemos imprimir las corrdenadas de recolección antes de la optimización
    cont2=0    
    for i in Pedidos_pendientes:
        print("Pedido :",i)
        print("Recolección antes de optimizar:\n",ListaCoordRecolecNoOptim[cont2],"\n")
        cont2+=1
        
        
    #Funcion que agrupa los pedidos por mes en olas de N pedidos cada una.
    def agruparPedidosOleadasNpedidos(listaPedidosSeparados,N):
        listapedidosAgrupadosOleada=[]
        CantidadPedidodsOrig=listaPedidosSeparados
        for i in range(0,len(listaPedidosSeparados),1):
            listapedidosAgrupadosOleada.append(listaPedidosSeparados[:N])
            listaPedidosSeparados=listaPedidosSeparados[N:]
            listapedidosAgrupadosOleada = [ele for ele in listapedidosAgrupadosOleada if ele != []]
        print("Cantidad de pedidos sin agrupar: ", len(CantidadPedidodsOrig))
        print("Los pedidos se agruparon en: ", len(listapedidosAgrupadosOleada),"olas", "\nCada ola tiene máximo ",N,"pedidos")
        #Juntamos las coordenadas de cada ola para manipularlas adecuadamente como una sola lista
        ListaCoordenadasOlas=[list(itertools.chain(i)) for i in listapedidosAgrupadosOleada]
        print(ListaCoordenadasOlas)
        return ListaCoordenadasOlas
    
    #Desempaquetamos las coordenadas en listas por pedido por .
    
    def funcionAgrupadora(lista_pedidosAgrupados):
        pedidosAgrupados2 = []
        for k in lista_pedidosAgrupados:
            lista2=[]
            for i in k:
                for j in range(len(i)):
                    elemento = k[k.index(i)][j]
                    lista2.append(elemento)
            pedidosAgrupados2.append(lista2)
        return pedidosAgrupados2
    
    pedidosAgrupadosOleada_N_noOptim=funcionAgrupadora(agruparPedidosOleadasNpedidos(ListaCoordRecolecNoOptim,agrupar_en_N_pedidos))
    
    #Ahora alimentemos el programa generado con cada uno de estos pedidos_ENERO_2019 de forma individual

    #Asumiremos que el origen y en donde queremos que termine nuestro recorrido es
    #la coordenada (0,0), es decir Pasillo A, ID_Ubicacion 5
    origin_loc=(0,0)
    

    #Leemos las dimensiones del almacen y las almacenamos en diferentes variables
    import json
    given_file = open('dimensionesAlmacen.txt', 'r')

    dimAlmacenRawDict = given_file.readlines()

    for line in dimAlmacenRawDict:
        for c in line:
            if c.isdigit() == True:
                print('Integer found : {}'.format(c))

    given_file.close()


    DimAlmacen=json.loads(dimAlmacenRawDict[0].replace("\'", "\""))

    #y_inf=DimAlmacen["y_inferior"]
    y_inf=0
    y_sup=int(DimAlmacen["y_superior"])


    
    ListaCoordRecolecOPTIMAS_OLA_N_distancia=[]
    
    #OPTIMIZACIÓN OLAS N PEDIDOS
    for i in pedidosAgrupadosOleada_N_noOptim:
        ListaCoordRecolecOPTIMAS_OLA_N_distancia.append(SF.generar_ruta_recog(origin_loc,i,y_inf,y_sup))
        
    
    
    
    print(ListaCoordRecolecOPTIMAS_OLA_N_distancia)# Hasta este punto seguimos considerando el origen como partida y retorno en el calculo de la distancia
    print("PedidosDistanciaLen: ",len(ListaCoordRecolecOPTIMAS_OLA_N_distancia))
    
    #Aqui tendremos una lista donde vienen como tuplas tanto la distancia total como las coordenadas de recolección optimas por cada pedido-
    ListaCoordRecolecOPTIMAS_Ola_N_coord=[]
    #Almacenamos la distancia total de recolección de todos los pedidos (dada la geeometra y dimensiones del almacen)
    ListaDistanciasFinalesRecolecOptima=[]
    #Separamos las distancias calculadas de las rutas de recolección
    for i in ListaCoordRecolecOPTIMAS_OLA_N_distancia:
        print(i,"\n")
        ListaCoordRecolecOPTIMAS_Ola_N_coord.append(i[1])
        ListaDistanciasFinalesRecolecOptima.append(i[0])

    print(ListaCoordRecolecOPTIMAS_Ola_N_coord)
    print(ListaDistanciasFinalesRecolecOptima)



    #Sumamos la distancia total de recorrido y alamcenamos

    totalDistancia=sum(ListaDistanciasFinalesRecolecOptima)


    with open('DistanciaTotalRecoleccion.txt','w') as f:
        f.write("%d" %totalDistancia)

 #Podemos estimar un tiempo de recorrido promedio (sin tomar en cuenta el tiempo de recoleccin)
    tiempoMinutos=(totalDistancia/1.46)/60


    print("Tiempo de recoleccion: ",tiempoMinutos," minutos")
    with open('TiempoFinalEnMinutosRecorrido.txt','w') as f:
        f.write('%f' %tiempoMinutos)

    
    ##############################################################################################################
    #Asignando correctamente el SKU para aquellas ubicaciones en donde se tiene más de un producto asignado.
    
    #Almacenaremos las indicaciones de recolección en un archivo .csv
    
    Indicaciones_Recolec_Sep=[]
    Indicaciones_Recolec_Juntas=[]
    Indicaciones_Recolec_Sep_sin_Texto=[]
    Indicaciones_Recolec_Juntas_sin_Texto=[]
    
    for i in ListaCoordRecolecOPTIMAS_Ola_N_coord:
        #Indicaciones_Recolec_Sep.append(Indicaciones_Recolec_Juntas)
        Indicaciones_Recolec_Juntas=[] #Vaciamos la lista para no encimar los pedidos
        #Removemos el inicio y final si no se quiere temrinar donde se empezó
        i=i[1:-1]
        for j in i:
            Indicaciones_Recolec_Juntas.append(("Dirigete al Pasillo:",Dic_Prod_coordenadas.get(j)[0],"Ubicacion: ",Dic_Prod_coordenadas.get(j)[1],"Por el SKU: ",Dic_Prod_coordenadas.get(j)[2]))
            print(j)
            Indicaciones_Recolec_Juntas_sin_Texto.append((Dic_Prod_coordenadas.get(j)[0],Dic_Prod_coordenadas.get(j)[1]))
        Indicaciones_Recolec_Sep.append(Indicaciones_Recolec_Juntas)
        Indicaciones_Recolec_Sep_sin_Texto.append(Indicaciones_Recolec_Juntas_sin_Texto)
    
    print(len(Indicaciones_Recolec_Sep))
    
    #Agrupamos los pedidos en N olas para su correcta visualización
    
    Pedidos_agrupados = [Pedidos_pendientes[i:i+agrupar_en_N_pedidos] for i in range(0, len(Pedidos_pendientes), agrupar_en_N_pedidos)]
    #print("Pedidossssssssssssssss Agrupados")
    print(Pedidos_agrupados)

    print("Indicaciones Recolección Sin Texto \n\n")
    print(len(Indicaciones_Recolec_Sep_sin_Texto))
    print(Indicaciones_Recolec_Sep_sin_Texto)
    
    
    #Agrupamos todos los articulos en N olas para su correcta visualización
    
    Articulos_Agrupados = [ListaProductosTodosLosPedidosSeparados[i:i+agrupar_en_N_pedidos] for i in range(0, len(ListaProductosTodosLosPedidosSeparados), agrupar_en_N_pedidos)]
    #print("Articulossssssssss Agrupados")
    print(Articulos_Agrupados)
    
    
    #Imprimimos la ruta de recolección para cada pedido con sus respectivos productos.
    cont3=0
    for i in Pedidos_agrupados:
        
        print("Pedido :",i)
        print("Articulos:\n",Articulos_Agrupados[cont3],"\n")
        print("Instrucciones de recolección\n",Indicaciones_Recolec_Sep[cont3],"\n")
        
        cont3+=1

    #Cantidad productos
    cant_prod=pedidos['cantidad'].tolist()

    #Correción de SKU a recoger. (ÚLTIMO SKU QUE APARCE EN EL EXCEL)
    agrupador,RutaRecolec_OPT_SKUcorregido_Cantidad=Asig_SKU.AsignacionSKU_Correcto_RutaRecolec_Olas(Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep_sin_Texto,cant_prod,agrupador)
    print("RUTA RECOLECCION SKU CORREGIDO: ", len(RutaRecolec_OPT_SKUcorregido_Cantidad))
    

    print("\n\n")
    print("Agrupador:",agrupador)
    print("Ruta Recoleccion:",RutaRecolec_OPT_SKUcorregido_Cantidad)
    
    #Introducimos texto a la ruta para volver más claro al usuario
    
    indicaciones_Explicitas=[]
    
    for i in RutaRecolec_OPT_SKUcorregido_Cantidad:
        indicaciones_Explicitas.append(["Ubicación: "+str(i[1])+" Producto: "+str(i[2])+" Cantidad: "+ str(i[3])])
    
    print("Indicaciones Explicitas:")
    print(indicaciones_Explicitas)
    
    #Es posible proponer un json de regreso con la misma estructura de entrada o my similar
    
    
    #Implicita
    print("\n\n")
    print("Propuesta JSON Regreso Implicito")
    RecoleccionOptimaImplicita={ 
       "Agrupador":agrupador,
      "Datos":RutaRecolec_OPT_SKUcorregido_Cantidad
    }
    
    print(RecoleccionOptimaImplicita)
    
    
    #Explicita
    print("\n\n")
    print("Propuesta JSON Regreso Explicito")
    RecoleccionOptimaExplicita={ 
       "Agrupador":agrupador,
      "Datos":indicaciones_Explicitas
    }
    
    print(RecoleccionOptimaExplicita) 
    


    
    
    
    
    #print("RUtaRecolec_OPT",RutaRecolec_OPT_SKUcorregido)
    #Almacenamos las indicaciones de recolección para cada pedido en un archivo de excel
    
    #csv_content = Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep
    #csv_file =  open("Recoleccion_Optima/OPT_recolec_Ola5.csv", 'w')
    
    
    #print("Recolección SKU FINAL: \n\n")
    #print(RutaRecolec_OPT_SKUcorregido)
    
    
    #csv_writer = csv.writer(csv_file, delimiter=",")
    
    #for row in csv_content:
    #    csv_writer.writerow(row)
    #    
    #csv_file.close()
    
    print("\n\n")
    print("Agrupador:",agrupador)
    print("Ruta Recoleccion:",RutaRecolec_OPT_SKUcorregido_Cantidad)
    
    #Introducimos texto a la ruta para volver más claro al usuario
    
    indicaciones_Explicitas=[]
    
    for i in RutaRecolec_OPT_SKUcorregido_Cantidad:
        indicaciones_Explicitas.append(["Ubicación: "+str(i[1])+" Producto: "+str(i[2])+" Cantidad: "+ str(i[3])])
    
    print("Indicaciones Explicitas:")
    print(indicaciones_Explicitas)
    
    #Es posible proponer un json de regreso con la misma estructura de entrada o my similar
    
    
    #Implicita
    print("\n\n")
    print("Propuesta JSON Regreso Implicito")
    RecoleccionOptimaImplicita={ 
       "Agrupador":agrupador,
      "Datos":RutaRecolec_OPT_SKUcorregido_Cantidad
    }
    
    print(RecoleccionOptimaImplicita)
    
    
    #Explicita
    print("\n\n")
    print("Propuesta JSON Regreso Explicito")
    """
    RecoleccionOptimaExplicita={ 
       "Agrupador":agrupador,
      "Datos":indicaciones_Explicitas
    }
    """
    RecoleccionOptimaExplicita={
      "Datos":indicaciones_Explicitas
    }
    
    
    print(RecoleccionOptimaExplicita) 
    
    
    """
    
    print("RUtaRecolec_OPT",RutaRecolec_OPT_SKUcorregido)
    Almacenamos las indicaciones de recolección para cada pedido en un archivo de excel
    
    csv_content = Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep
    csv_file =  open("Recoleccion_Optima/OPT_recolec_Ola5.csv", 'w')
    
    
    print("Recolección SKU FINAL: \n\n")
    print(RutaRecolec_OPT_SKUcorregido)
    
    
    csv_writer = csv.writer(csv_file, delimiter=",")
    
    for row in csv_content:
        csv_writer.writerow(row)
        
    csv_file.close()
    """




    #Almacenamos las indicaciones de recolección para cada pedido en un archivo de excel
    
    #csv_content = Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep
    #csv_file =  open("Recoleccion_Optima/"+str(agrupador)+"_OPT_recolec_Ola_de_"+str(agrupar_en_N_pedidos)+"_pedidos.csv", 'w')
    
    #csv_file =  open("Recoleccion_Optima/%s_OPT_recolec_Ola_de_%s_pedidos.csv"%(agrupador,agrupar_en_N_pedidos), 'w')

    
    #csv_writer = csv.writer(csv_file, delimiter=",")
    
    #for row in csv_content:
    #    csv_writer.writerow(row)
        
    #csv_file.close()
    
    return Pedidos_agrupados,Articulos_Agrupados,Indicaciones_Recolec_Sep,agrupador,RecoleccionOptimaExplicita




