# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:15:21 2022

@author: Alban Rodríguez

REST API que genera las rutas de recolección en almacen más optimas.

"""

import csv
from flask import Flask,jsonify,request,render_template


"""
Función que extrae tiempo y distancia calculadas
"""
#Extraemos el tiempo calculado del archivo
###########################################
###########################################
def DistanciaTiempo():
    given_file1 = open('TiempoFinalEnMinutosRecorrido.txt', 'r')
    
    tiempo = given_file1.readlines()
    
    for line in tiempo:
        for c in line:
            if c.isdigit() == True:
                    print('Integer found : {}'.format(c))
                    
    given_file1.close()
    
    TiempoFloat=float(tiempo[0])
    
    
    print("Tiempo unicamente de recorrido: ",TiempoFloat," minutos")
    
    ########################
    ###### Extraemos la distancia Calculada
    
    given_file2 = open('DistanciaTotalRecoleccion.txt', 'r')
    
    distancia = given_file2.readlines()
    
    for line in distancia:
        for c in line:
            if c.isdigit() == True:
                    print('Integer found : {}'.format(c))
                    
    given_file2.close()
    
    DistanciaFloat=float(distancia[0])
    
    
    print("Distancia Recorrida en Metros: ",DistanciaFloat)
    
    return TiempoFloat,DistanciaFloat







#Creamos un app
app=Flask(__name__) #__name__ nombre especifico y unico.


@app.route("/RutasOptimas", methods=["POST"]) #Solo será accesible a través de una solicitud de POST
#Creará una nueva tienda con un nombre dado
def rutaRecoleccionExplicita():
    
        
    req_json = request.get_json()
    #Almacenamos los datos consumidos de agrupador, fecha y hora en un .txt
    agrupador=req_json["agrupador"]
    fecha=req_json["fecha"]
    hora=req_json["hora"]
    
    
    #ALmacenamos, pero aquí mismo podemos hacer la petición
    import json
    with open('DatosAgrupador_%s.txt'%(agrupador), 'w') as f:
        json.dump(req_json, f)
        
    #Solamente almacenamos el agrupador
    with open('DatosAgrupador.json', 'w') as f:
        json.dump({"agrupador":req_json["agrupador"]}, f)
    
    #Solicitamos pedidos y almacen.
    from Lectura_Pedidos import LectPedidos
    from Lectura_Almacen import Lectura_geometriaAlmacen

    from Verif_Existencia_SKU_Solicitado import VerificandoExistenciaSKU_Pedidos as Verif_SKU_Exist

    import requests

    import json


    def recolecPedidosAlmacen():
        print("Recolectando Pedidos")
        LectPedidos()
        print("Recolectando Geometría Almacen")
        Lectura_geometriaAlmacen()

    #Primero Recuperamos la información de almacen:
    #Geometría, dimensiones y distrubución espacial
    recolecPedidosAlmacen()

    #Verificamos existencia de SKU

    #A continuación verificamos que todos los pedidos que vienen en el pedido existan en ubicaciones físicas en almacen

    ConjuntoSku_NoMapeados=Verif_SKU_Exist()
    #una vez cargada la infromación del almacén y pedidos


    #Importamos todas las funciones que necesitamos para generar la ruta

    from GeneracionRutaOptima import RutaOptima


    #Definimos una función que recolecta información

    def GenerandoRutaOptima():
        print("Generando Ruta Optima")
        rutaExplicita=RutaOptima()
        return rutaExplicita
    
    
    rutaExplicita=GenerandoRutaOptima()
    TiempoFloat,DistanciaFloat=DistanciaTiempo()
    
    """
    #Descubrir el error al almacenar en un CSV, no solicitado por eso el comentario
    #Almacenamos la información de recolección
    
    #Almacenamos las indicaciones de recolección para cada pedido en un archivo de excel
    
    csv_content = agrupador,rutaExplicita,"Tiempo_en_Minutos",TiempoFloat,"DistanciaRecorrido_metros",DistanciaFloat,"SKU UBICACION 0- SIN PRIORIDAD",list(ConjuntoSku_NoMapeados)
    csv_file =  open("Historial_RutaRecolec/"+str(agrupador)+".csv", 'w')
    

    csv_writer = csv.writer(csv_file, delimiter=",")
    
    for row in csv_content:
        csv_writer.writerow(row)
        
    csv_file.close()
    """
    return jsonify({agrupador:rutaExplicita,"Tiempo_en_Minutos":TiempoFloat,"DistanciaRecorrido_metros":DistanciaFloat,"SKU UBICACION 0- SIN PRIORIDAD":list(ConjuntoSku_NoMapeados),"fecha":fecha,"hora":hora})


@app.route("/RutasOptimas", methods=["GET","PUT","PATCH","DELETE"]) #Solo será accesible a través de una solicitud de POST
def ErrorHandling():
    return("El método no está implementado. Verifica tu petición")


"""
    def rutaRecoleccionExplicitaGET():
    agrupador,rutaExplicita=GenerandoRutaOptima()
    TiempoFloat,DistanciaFloat=DistanciaTiempo()

    return jsonify({agrupador:rutaExplicita,"Tiempo_en_Minutos":TiempoFloat,"DistanciaRecorrido_metros":DistanciaFloat,"SKU UBICACION 0: SIN PRIORIDAD":list(ConjuntoSku_NoMapeados)})
"""


# app name
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
# defining function
  return render_template("404.html")

#app.run(debug=True, use_debugger=False, use_reloader=False)

if __name__ == "__main__":
    from waitress import serve
    serve(app,host="127.0.0.1",port=5000)







