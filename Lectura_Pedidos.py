# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:22:18 2022

@author: lumen
"""

def LectPedidos():
    """
    PedidoLectura= { 
       "Agrupador":"1002933004940",
      "Datos":[
    {
      "pedido":"1085",
      "detalle": [
        {
          "producto":"85",
          "cantidad":3
        },
        {
          "producto":"39",
          "cantidad":5
        },
        {
          "producto":"74819",
          "cantidad":10
        },
        {
          "producto":"72942",
          "cantidad":8
        }
      ]
    },
    {
      "pedido":"613090",
      "detalle": [
        {
          "producto":"5525",
          "cantidad":3
        },
        {
          "producto":"84",
          "cantidad":5
        },
        {
          "producto":"38",
          "cantidad":10
        },
        {
          "producto":"43",
          "cantidad":8
        }
      ]
    },
    {
      "pedido":"380",
      "detalle": [
        {
          "producto":"38",
          "cantidad":3
        },
        {
          "producto":"52",
          "cantidad":5
        },
        {
          "producto":"51",
          "cantidad":30
        },
        {
          "producto":"18248",
          "cantidad":8
        }
      ]
    },
    {
      "pedido":"612424",
      "detalle": [
        {
          "producto":"18250",
          "cantidad":3
        },
        {
          "producto":"7703",
          "cantidad":5
        },
        {
          "producto":"9767",
          "cantidad":10
        },
        {
          "producto":"9444",
          "cantidad":8
        }
      ]
    },
    {
      "pedido":"613086",
      "detalle": [
        {
          "producto":"89",
          "cantidad":3
        },
        {
          "producto":"48",
          "cantidad":5
        },
        {
          "producto":"51",
          "cantidad":10
        },
        {
          "producto":"75",
          "cantidad":8
        }
      ]
    }
    ]
    }

    
    Una vez en la máquina de ONEST y montado en el server o no

    """
    import urllib, json
    import requests


    # GET
    urlGET="http://myonest.com:7090/ords/onewms/almacen/Pedidos"
    
    
    
    #POST
    #make a POST request
    
    #Leemos los datos almacenados previamente de agrupador, fecha y hora
    
    import requests
    
    import json
  
    # Opening JSON file
    f = open('DatosAgrupador.json')
      
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    
    
    #Enviamos los datos del diccionari consumido como parte del POST
    
    response = requests.post('http://myonest.com:7090/ords/onewms/almacen/Pedidos', json=data)
    
    response=response.json()

    
    #response=urllib.request.urlopen(urlGET)
    #print(response)
    #PedidoLectura=json.loads(response.read())
    
    
    PedidoLectura=response

    # Closing file
    f.close()
    

    #print(pedidos)
    #PedidoLectura={'PedidoLectura': {'Agrupador': '0001', 'Datos': [{'pedido': 'P00003', 'detalle': [{'producto': '16105375', 'cantidad': 10}, {'producto': '123400', 'cantidad': 20}, {'producto': '122850', 'cantidad': 3}, {'producto': '107800', 'cantidad': 40}]}]}}

    



    #print(PedidoLectura.keys())

    #print(PedidoLectura.values())


    #print("Datos",PedidoLectura.get("Datos"))

    #Guardamos el nombre del agrupador en una variable para ser retornada con la ruta

    Agrupador=PedidoLectura.get("Agrupador")
        

    Datos=PedidoLectura.get("Datos")


    #Almacenamos los pedidos pendientes a agrupar
    pedidos=[]
    for i in range(0,len(Datos),1):
        pedidos.append(Datos[i].get("pedido"))
        
    #Almacenaremos producto y cantidad de cada pedido en listas diferentes.
    #Lista producto y cantidad.
    prod_quant=[]
    cont=0

    for i in pedidos:
        prod_quant.append(Datos[cont].get("detalle"))
        cont+=1
        
    #Generamos tuplas con los datos de cada producto y cantidad en listas separadas por pedido
    prod_quant_tupla=[]

    pedidoContador=0
    for i in prod_quant:
        prod_quant_tupla.append([(pedidos[pedidoContador],j.get("producto"),j.get("cantidad")) for j in i])
        pedidoContador+=1

    #Juntamos en una  sola lista para su registro en un CSV

    Lista_Fin=[]

    Lista_Fin.append(("documento","producto","cantidad",Agrupador))

    for i in prod_quant_tupla:
        for j in i:
            Lista_Fin.append(j)

    import csv 
    #Guardamos para el historial de agrupadores con el nombre del agrupador
    
    file = open('Historial_Agrupadores/Agrupador_%s.csv'%(Agrupador), 'w+', newline ='') 
    with file:
        write = csv.writer(file) 
        write.writerows(Lista_Fin) 

    #Guardamos para la lectura del algoritmo y su optimización.
    file = open("PedidosEnCola/pedidos_SinVerificarExistencia_SKU.csv", 'w+', newline ='') 

    with file:
        write = csv.writer(file) 
        write.writerows(Lista_Fin) 


    #Guardamos el entero que nos dice que cantidad de pedidos se tienen por agrupador.s

    with open('numeroPedidos_Oleada.txt', 'w') as f:
      f.write('%d' % pedidoContador)
      
      


    #Guardamos el entero que nos dice que cantidad de pedidos se tienen por agrupador.s

    with open('NumAgrupador.txt', 'w') as f:
      f.write('%s' % Agrupador)

LectPedidos()