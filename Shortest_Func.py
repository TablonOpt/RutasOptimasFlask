00# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 16:01:39 2021

"""
import pandas as pd
import numpy as np
from ast import literal_eval



#Definimos una función que encuentre las coordenadas en el almacen dado cada ID_Ubicacion de un pedido

def asig_coord_desde_pedido(pedido_ID_Ubicacion,Dict_Prod):
    listaCoordenadas=[Dict_Prod[i][0] for i in pedido_ID_Ubicacion]
    return listaCoordenadas
    
def distancia_minima(Ubic1,Ubic2,y_inf,y_sup):
    """
    Esta función calcula la trayectoria mas corta entre dos rutas
    potenciales para ir de un punto i a un punto j

    Parameters
    ----------
    Ubic1 : TYPE
        DESCRIPTION.
    Ubic2 : TYPE
        DESCRIPTION.
    y_inf : Flotante
        Cota inferior de "y".
    y_sup : Flotante
        Cota superior de "y".

    Returns
    -------
    distancia : TYPE
        DESCRIPTION.

    """
    
    #Punto de inicio
    x1,y1=Ubic1[0],Ubic1[1]
    
    #Punto final
    x2,y2= Ubic2[0],Ubic2[1]

    #Distancia en el eje X
    distancia_x= abs(x2-x1)
    
    #Distancia en el eje Y
    if x1==x2:
        distancia_y1=abs(y2-y1)
        distancia_y2=distancia_y1
    else:
        distancia_y1=(y_sup-y1)+(y_sup-y2)
        distancia_y2= (y1-y_inf)+(y2-y_inf)
    
    #Devolvemos la distancia mínima en el eje y
    distancia_y=min(distancia_y1,distancia_y2)
    
    #Distancia total (x+y)
    
    distancia= distancia_x+distancia_y
    
    return distancia


def siguiente_ubicacion(loc_inicio,lista_ubicaciones,y_inf,y_sup):
    """
    Esta función se utiliza para calcular la siguiente ubicación a visitar
    entre todos los posibles candidatos

    Parameters
    ----------
    loc_inicio : TYPE
        DESCRIPTION.
    lista ubicaciones : TYPE
        DESCRIPTION.
    y_inf : TYPE
        DESCRIPTION.
    y_sup : TYPE
        DESCRIPTION.
        
    Returns
    
    Devuelve la ubicación más cercana como mejor candidato a visitar.
    -------
    lista_locaciones : TYPE
        DESCRIPTION.
    loc_inicio : TYPE
        DESCRIPTION.
    sig_ubic : TYPE
        DESCRIPTION.

    """
    #Distancia a todos los puntos candidatos para recolección.
    list_dist=[distancia_minima(loc_inicio,i,y_inf,y_sup) for i in lista_ubicaciones]
    
    # Distancia Minima
    distancia_sig=min(list_dist)
    
    #Ubicación de la zona con la distancia minima
    index_min=list_dist.index(min(list_dist))
    
    #La siguiente ubicación a visitar es aquella con la distancia mínima
    sig_ubic=lista_ubicaciones[index_min]
    
    #Removemos de la lista de ubicaciones la última ubicación asignada dado que ya la hemos considrado en la ruta.
    lista_ubicaciones.remove(sig_ubic)
    
    return lista_ubicaciones, loc_inicio, sig_ubic, distancia_sig


def generar_ruta_recog(origin_loc,lista_ubicaciones,y_inf,y_sup):
    
    #Variable donde se almacena la distancia total del recorrido.
    distancia_ola=0
    
    #Variable que almacena la ubicación actual que se usará como "pivote para calcular la siguiente ubicación mas cercana
    loc_inicio= origin_loc
    
    # Lista donde almacenaremos la ruta más optima de recolección
    list_optim=[]
    list_optim.append(loc_inicio)
    
    
    #Recorremos todas las ubicaciones disponibles a recolectar, hasta que se hayan visitado todas
    
    while len(lista_ubicaciones)> 0:
        
        #Siguiente ubicación-
        lista_ubicaciones,loc_inicio,sig_ubic,distancia_sig=siguiente_ubicacion(loc_inicio,lista_ubicaciones,y_inf,y_sup)
        
        #Actualizamos la ubicacion de inicio
        loc_inicio= sig_ubic
        
        list_optim.append(loc_inicio)
        
        #Actualizamos la distancia a recorrer
        
        distancia_ola= distancia_ola + distancia_sig
        
    # Calculamos la distancia de la última ubicación visitada al origen que fue el punto de partida inicia.
    
    distancia_ola= distancia_ola + distancia_minima(loc_inicio,origin_loc,y_inf,y_sup)
    
    list_optim.append(origin_loc)
    
    return distancia_ola,list_optim
    


