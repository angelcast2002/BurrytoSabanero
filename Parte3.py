from Vista import Vista
import tkinter as Tk
from Parte4 import Parte4
from Interfaz import Interfaz
import requests
import json
import pandas as pd
from Estadisticas import Estadisticas


class Parte3:

    def __init__(self):
        self.vista = Vista()
        self.interfaz = Interfaz()
        self.parte4 = Parte4()
        self.estadisticas = Estadisticas()
        self.rutas=pd.read_csv('rutas.csv')
        
    #Crearemos una función que permita navegar y seleccionar los destinos disponibles en el mapa.
    #Además, se presentará la información de lo que realiza cada botón para ayudar al usuario. 
    def navegarmapa(self,direcciones): 
        #Esta variable permite salir del ciclo.
        estado = True
        #Creamos un ciclo que permitirá desplegar el menú 
        while estado==True:
            #Mostramos la interfaz del menú en el código. 
            self.menuPrin()
            #Solicitamos le ingreso de una opción del menú
            opcion = input('Ingrese una opción del menu principal:  ')

            if opcion == '1':
                #Salimos del ciclo. 
                estado = False 

            elif opcion == '2':
                #Ejecutamos la función que nos permite ingresar un destino. 
                self.destinos()

            elif opcion == '3':
                #Ejecutamos las funcione que nos permiten obtener información acerca del 
                self.información()
                self.estadisticas.rutas_mas()

            else:     
                #Esta acción se ejecuta si el usuario ingresa una opción incorrecta, y se reinicia el programa.
                print ("""
            ---------------------------------------------------------------------
            -                   ¡Ingresó una opción incorrecta!                 -
            --------------------------------------------------------------------- 
            """)



    def menuPrin(self):#Esta funcion imprime la imagen de la pantalla de carga y al mismo tiempo lo imprime en
        #la consola
        self.interfaz.buscar()
        print("""
            ---------------------------------------------------------------------------
            -                                                                         -
            -       _                        __  __                                   -
            -      | |     ___   __ _   ___ |  \/  |  __ _   _ __                     -
            -      | |__  / _ \ / _` | / _ \| |\/| | / _` | | '_ \                    -
            -      |____| \___/ \__, | \___/|_|  |_| \__,_| | .__/                    -
            -                   |___/                       |_|                       -
            -                                                                         -
            -                                                                         -
            -                                                                         -
            -                                                                         -
            -      _____________                        _________________________     -
            -     |1. REGRESAR  |                      |2. INGRESAR UNA DIRECCIÓN|    -
            -      ¯¯¯¯¯¯¯¯¯¯¯¯¯                        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯     -
            -                     ______________________                              -
            -                    |    3. INFORMACIÓN    |                             -
            -                     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                              -
            ---------------------------------------------------------------------------
            """)

    def buscar_destinos(self,destino): 
        #Esta función permite buscar el destino mediante una API. 
        lista_destinos = [] #Esta lista almacenará los destinos que el API devuelva
        #En esta linea busca en la api los datos que tiene sobre el detino y se guarda en una variable


        # estya es la url con los parametros para buscar el destino que uno desea
        res = requests.get("http://api.geonames.org/search?q=%22" + destino + "&username=uvgfinal&type=json&isNameRequired=true&maxRows=10")


        if res: # si el codigo es  200
            res_json = res.json() #JSON es un formato de texto sencillo para el intercambio de datos.

            lista_destinos = res_json["geonames"]#"geonames" es la Api la cual se esta utilizando para buscar los datos


        else:
            #Esto se devolverá si existe un error. 
            print("[Error]")

        return lista_destinos #Retornamos el listado de los destinos. 

    def destinos(self):#Sirve para hacer la investigación del destino 
    #Un Web API  hace una petición HTTP (generalmente desde algún lenguaje de programación) y este le retorna un dato de respuesta

        destino_deseado = input("-> Ingrese el destino al que desea ir: ")# se pide el destino al cual desea ir el usuario
        destinos = self.buscar_destinos(destino_deseado)
        destinados=list(self.rutas['rutas'])
        existe=False
        for i in destinados:
            if i == destino_deseado:
                existe=True
        if existe ==True:
            conteo= self.rutas[self.rutas['rutas']==destino_deseado]['conteo']
            conteo=conteo+1
            self.rutas.loc[self.rutas['rutas']==destino_deseado, 'conteo']=conteo
        else:
            posicon=0
            for i in (self.rutas.index):
                posicon=i
            posicon=posicon+1
            self.rutas.loc[posicon]=[destino_deseado,1]
        self.rutas.to_csv('rutas.csv',index=False) #guarda cada cosa que busque el usuario en un archivo .csv
        for i in range(len(destinos)):
            nombre_destino = destinos[i]["name"]
            distancia_destino = float(destinos[i]["lat"]) * 37
            tiempo_destino =  float(destinos[i]["lat"]) * 15


            print(f"{i+1}) {nombre_destino} - {distancia_destino} kms    - {tiempo_destino} min ")# le da una lista de lugares con similitudes al nombre de la ciudad que eligio 


        opcion = int(input(" -> Ingrese el numero del destino: "))
        nombre = destinos[opcion - 1]["name"]
        distancia = int(float(destinos[opcion - 1]["lat"]) *37)
        tiempo =  int(float(destinos[opcion - 1]["lat"]) * 15)


        print(f" Su destino final desde su ubicación es : {nombre} - {distancia} kms - {tiempo} min" )    

        self.parte4.empezarviaje () #Se llama a la funcion navegar por el mapa


    def información(self):       
        #Mostramos la interfaz del menú del código. 
        print("""
            -------------------------------------------------------------------------------------
            -                                                                                   -
            -       _                        __  __                                             -
            -      | |     ___   __ _   ___ |  \/  |  __ _   _ __                               -
            -      | |__  / _ \ / _` | / _ \| |\/| | / _` | | '_ \                              -
            -      |____| \___/ \__, | \___/|_|  |_| \__,_| | .__/                              -
            -                   |___/                       |_|                                 -
            -   _____________________                                                           -
            -  |Información:         |                                                          -
            -   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                                           -
            -   _____________________________________________________________________________   -
            -  |[Iniciar sesión]. Si seleccionas esta opción te llevará a un menú que te     |  -
            -  |permitirá entrar al la aplicación con tu nombre de usuario y contraseña.     |  -
            -  |[Registrarse]. Este boton te permite crear un nuevo usuario para que puedas  |  -
            -  |ingresar y utilizar la aplicación.                                           |  -
            -  |[Salir]. Este botón se utiliza para cerrar la aplicación cuendo desees.      |  -
            -  |[Cerrar sesión]. Este botón permite cerrar la sesión de tu cuenta.           |  -
            -  |[Navegar]. Esta opción te envía al menú principal de la aplicación en el que |  -
            -  |podrás decidir la acción que quieras realizar.                               |  -
            -  |[Regresar]. Este botón te permitirá regresar al menú anterior.               |  -
            -  |[Ingresar dirección]. Esta opción te permitirá ingresar al menú de selección |  -
            -  |de destino.                                                                  |  -
            -  |[¿QUÉ SON ESOS ÍCONOS?]. Este botón te explica qué significa cada icono.     |  -
            -  |[Ingresar dirección]. Esta opción te permitirá ingresar al menú de selección |  -
            -  |de destino.                                                                  |  -
            -  |[Ingresar una dirección]. Este botón te permitirá seleccionar uno de los     |  -
            -  |destinos disponibles.                                                        |  -
            -  |[Información]. Esta opción te explicará el funcionamiento de cada botón      |  -
            -   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   -
            -------------------------------------------------------------------------------------
                    """)
        input("\nPresione ENTER para continuar...")

