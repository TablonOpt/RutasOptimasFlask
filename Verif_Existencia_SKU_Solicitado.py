# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 17:50:38 2022

@author: lumen
"""

import pandas as pd

path="PedidosEnCola/"


#Programa que verifica que todos los SKU solicitados exístan dentro del almacen.

#Esta función se debe ejecutar una vez que ya existen los pedidos en el CSV
#Generados en Lectura_Pedidos.py, siempre después para que el CSV de pedidos exísta

def VerificandoExistenciaSKU_Pedidos():

    #Cargamos la lista de SKU solicitados en el agrupador consumido.
    #http://myonest.com:7090/ords/onewms/almacen/Pedidos
    pathPedidos="PedidosEnCola/"
    skus_solicitados=pd.read_csv(pathPedidos+"pedidos_SinVerificarExistencia_SKU.csv")
    #Recordemos que los conjuntos no tienen elementos repetidos, por lo que no se tendrá la lista completa de SKU solicitados, ya que muchos de ellos pueden estár repetidos en diferentes pedidos.
    Set_Sku_Solicitados=set(skus_solicitados["producto"])
    
    
    #Ahora generemos el Set de sku´s mapeados en almacen al consumir la geometría del mismo en 
    #http://myonest.com:7090/ords/onewms/almacen/layout
    skus_mapeados=pd.read_csv("Ubicaciones.csv")
    
    Set_Sku_Mapeados=set(skus_mapeados["SKU_PRODUCTO"])
    
    
    #Ahora encontramos que elementos de A no exísten en B
    #A = Set_Sku_Solicitados
    #B = Set_Sku_Mapeados
    # QUeremos encontrar A-B
    
    NoMapeadosSet=Set_Sku_Solicitados-Set_Sku_Mapeados
    
    
    
    #Verificamos el contenido de esta lista.
    #El contenido de la misma de agregará a al final de las instrucciones de recolección como 
    #Ubicación Cero- Sin Prioridad
    #La ubicación no se encuentra mapeada en almacen
    
    
    """
    #Imaginemos que los SKU solicitados que no existen en almacen (aunque si en la realidad) son los siguientes:
        
    #NoMapeadosSet={"481502","482880","493025","451425"}
    
    #En raw, existen 7 coincidencias de 481502
    #EN pedidos limpiados =0
    
    #EN raw existen 7 concidencias de 482880
    #EN pedidos limpiados =0
    
    #En raw existen 9 concidencias de 493025
    #En pedidos limpiados =0
    
    #En raw existen 9 concidencias de 451425
    #En pedidos limpiados =0
    """
    
    #Vamos a remover aquellas filas que contengas SKUS que no están mapeados en sistema para volver a actualizar la información
    #skus_solicitados = skus_solicitados[skus_solicitados["producto"].str.contains("482880") == False]
    
    for i in NoMapeadosSet:
        skus_solicitados = skus_solicitados[skus_solicitados["producto"].str.contains(i) == False]
    
    
    
    #Almacenamos la lista de pedido actualizada (SIN SKU No mapeados en almacen)
    
    skus_solicitados.to_csv(path+"pedidos.csv",index=False)
    
    return NoMapeadosSet















"""
A={"1","2","3","4","5","6","7","8","9","10"}
B={"3","4","5","6","7","8","9"}
C={"3","4","5","6","7","8","9"}


D=A-B

E=B-C
"""

