# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:00:09 2022

@author: lumen
"""

#Generación Pedido


from OPT_Recolecc_Indiv_Y_Apilados import OPT_Recolec_Optima_Apilar_N_Pedidos_por_ola as Recolec_NpedidosPorOla

#Flujo principal

#OPTIMIZACIÓN INDIVIDUAL 

#OPT_DIST_MIN_RECOLEC_INDIVID almacena las indicaciones en un excel y regresa una lista de llas por si se quieren mostrar directamente en interfaz
#pedidosInd,productosInd,indicacionesInd=OPT_Rec.OPT_Recolec_Optima_Indiv("pedidos")

#pedidosOla3,productosOla3,indicacionesOla3=OPT_Rec.OPT_Recolec_Optima_Apilar3Pedidos("pedidos")

#pedidosOla5,productosOla5,indicacionesOla5,agrupador,rutaExplicita=OPT_Rec.OPT_Recolec_Optima_Apilar5Pedidos("10pedidos")

#Leemos la cantidad de pedidos que contiene el agrupador

def RutaOptima():

    #print(Npedidos,len(pedidosOlaN),len(productosOlaN))
    #print(Npedidos)
    
    #print(len(indicacionesOlaN[2]))
    #print(indicacionesOlaN[2])
    
       
    given_file = open('numeroPedidos_Oleada.txt', 'r')
    
    numPedidos = given_file.readlines()
    
    for line in numPedidos:
        for c in line:
            if c.isdigit() == True:
                print('Integer found : {}'.format(c))
    
    given_file.close()
    
    numPedidosAgrupador=int(numPedidos[0])
    
    
    pedidosOlaN,productosOlaN,indicacionesOlaN,agrupador,rutaExplicita=Recolec_NpedidosPorOla("pedidos",numPedidosAgrupador)
    
    agrupador=agrupador[0]
    
    #return agrupador,rutaExplicita
    return rutaExplicita

    pass

if __name__ == "__main__":
    
   # stuff only to run when not called via 'import' here

    
    
   RutaOptima()

