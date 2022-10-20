# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 07:28:39 2021

@author: Alban A. Rodríguez.


Este codigo lee lee el archivo de excel con la estructura y genera las coordenadas necesarias con sus respectivos 
números de lote.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Importamos las funciones de optimización




def Calc_Coord_desde_Excel(Archivo_ubic):
    '''
    Parameters
    ----------
    Archivo_ubic : TYPE
        DESCRIPTION.

    Returns
    -------
    Dic_Prod : TYPE
        DESCRIPTION.
    X_lis : TYPE
        DESCRIPTION.
    Y_lis : TYPE
        DESCRIPTION.
    ID_Pasillo_lis : TYPE
        DESCRIPTION.
    ID_Ubicacion_lis : TYPE
        DESCRIPTION.
    List_Coor : TYPE
        DESCRIPTION.

    '''
    
    
    #Nombres de las columnas a importar
    name_col=["ID_Pasillo","X","Y","ID_Ubic","SKU_PRODUCTO"]
    
    #Importamos el archivo excel como un data frame
    
    df = pd.read_csv(Archivo_ubic+".csv", usecols=name_col)
    
    '''
    print(df["X"])
    print(df["Y"])
    print(df["ID_Pasillo"])
    print(df["ID_Ubic"])
    '''
    
    #Generamos lístas de cada columna
    
    X_lis=list(df["X"]) # El cambio de pasillo se da del 0 al 27
    
    Y_lis=list(df["Y"])
    
    ID_Pasillo_lis=list(df["ID_Pasillo"])
    
    ID_Ubicacion_lis=list(df["ID_Ubic"])
    
    SKU=list(df["SKU_PRODUCTO"])
    
    #Coordenadas como tuplas
    
    List_Coor=list(zip(X_lis,Y_lis))
    
    #print(List_Coor)
    #plt.scatter(X_lis,Y_lis)
    #plt.grid()
    
    #Generamos un diccionario con el ID de ubicación  como llave primaria y como valores las coordenadas correspondientes en el almacen y ID_ubicacón.
    
    Dic_Prod={}
    
    for i in range(0,len(List_Coor),1):
        Dic_Prod[ID_Ubicacion_lis[i]]=[List_Coor[i],ID_Pasillo_lis[i]]
        
   #print(Dic_Prod)
   #########################################################################################################
   #Generamos otro diccionario con las coordenadas como llaves para obtener el pasillo y la ubicación
   
    Dic_Prod_coordenadas={}
    
    for i in range(0,len(List_Coor),1):
        Dic_Prod_coordenadas[List_Coor[i]]=[ID_Pasillo_lis[i],ID_Ubicacion_lis[i],SKU[i]]   
    
    #Probamos con una lista para poder manejar varios SKU por ubicacion, ya que el diccionario borra los SKUS iguales como llave, ya que no puede haber dos llaves iguales.
    
    #Dic_Prod_coordenadas=[]
    
    #for i in range(0,len(List_Coor),1):
    #    Dict_proof={}
    #    Dict_proof[List_Coor[i]]=[ID_Pasillo_lis[i],ID_Ubicacion_lis[i],SKU[i]]
    #    Dic_Prod_coordenadas.append(Dict_proof.copy())
    #print(Dic_Prod_coordenadas)
    
    
    return Dic_Prod,Dic_Prod_coordenadas,X_lis,Y_lis,ID_Pasillo_lis,ID_Ubicacion_lis,List_Coor



#Dic_Prod,Dic_Prod_coordenadas,X_lis,Y_lis,ID_Pasillo_lis,ID_Ubicacion_lis,List_Coor=Calc_Coord_desde_Excel('Ubicaciones')

