from Estadisticas import Estadisticas
from Interfaz import Interfaz
import pandas as pd
import time
import requests
import json


class Controlador:

    def __init__(self,vista):
        self.vista = vista
        self.interfaz = Interfaz()
        self.estadisticas = Estadisticas()
        self.rutas=pd.read_csv('rutas.csv')

        self.estado_sesion = {
        'nombre_usuario': '',
        'clave': '', 
        'direccion_actual': '',
        'estado': False
        }

        self.direcciones = {}
        
        self.registrodata = pd.read_csv("Estado_Sesion.csv")
        #Almacenamos en una variable lo que contiene nuestro archivo.csv


    def main(self):
        #Almacena y muestra una imagen del menú.
        self.interfaz.menu()
        #Esta variable permite salir del ciclo en el que se encuentra. 
        estado = True

        while estado:
            #Despliegue de interfaz del menú principal dentro del código.
            self.vista.menuPrin()
            #Solicitamos que el usuario ingrese una opción
            opcion = input('Ingrese una opción del menu principal: ')
            #Evaluamos la decisión del usuario
            if opcion == '1':
                #Añade un nuevo usuario en el archivo correspondiente.
                self.registrarse()

            elif opcion == '2':
                #Este apartado se encarga de que el usuario inicie sesión.
                sesion=self.iniciarSesion()
                self.estado_sesion['estado'] = sesion[0]

            elif opcion == '3':
                #Esta opción se ejecuta si el usuario desea salir del programa.
                self.vista.grBT()
               
                #Convertimos la  variable a False para salir del menú y terminar el programa. 
                estado = False 
            #ACTUALIZACIÓN
            elif opcion == '21240':
                #Este apartado permite ingresar al modo de desarrollador. 
                self.estadisticas.estadisticas()
            else:
                #Este mensaje se desplegará si el usuario ingresa un valor incorrecto 
                self.vista.dtIC()
                input()
            #ACTUALIZACIÓN
            #Este apartado verifica que el usuario ha iniciado sesión y le permite continuar. 
            if self.estado_sesion['estado'] == True:
                self.main2(sesion[1], sesion[2])

                
    def registrarse(self):
        #Este apartado almacena y muestra una imagen del apartado de registro.
        self.interfaz.registrar()
        contador = 1
        nombre_usuario = (input('Ingrese su nombre de usuario:  ')).lower()
        clave = (input('Ingrese su clave: ')).lower()
        numerodedezplamiento = 1
        alfabeto = ("abcdefghijklmnopqrstuvwxyz")
        mensajecifrado = ('')

        for l in clave:
            if l in alfabeto:
                posicionletra = alfabeto.index(l)
                nuevaposicion = (posicionletra + numerodedezplamiento) % len(alfabeto) #se suma para moverse las unidades deseadas
                mensajecifrado+= alfabeto[nuevaposicion] #se crea el nuevo alfabeto como una cadena
            else: # si no se encuentra en el abecedario sólo se añade
                mensajecifrado+= l

        clave = mensajecifrado
        
        
        #Se verificará que no existe un usuario ya registrado con el nombre anteriormente escrito.
        usuario_repetido=self.registrodata[self.registrodata['usuarios']==nombre_usuario]['usuarios']
        #Se contará el número de usuarios que aparecen en la lista para observar si no existe algún usuario repetido. 
        repetido=len(usuario_repetido)
        #Con esto se determinará el número de veces que se encuentra el usuario repetido y devolverá un mensaje indicado lo sucedido. 
        if repetido>0:
            print('Este nombre de usuario esta repetido')


        else:
            #Con esto re recorren todos los datos que se encuentran en la lista para que el contador almacene el número de valores. 
            for posicion in list(self.registrodata.index):
                contador=contador+1
            #Almacenamos los datos que el usuario ingresó. 
            self.registrodata.loc[contador, 'usuarios']=nombre_usuario
            self.registrodata.loc[contador,'contrasenas']=clave
            self.registrodata.loc[contador,'ingresos a la aplicacion']=0
            self.registrodata.loc[contador,'tiempo pasado en la app']=0
            self.registrodata.to_csv('Estado_Sesion.csv',index=False)

            print("\nSe ha registrado satisfactoriamente")
            input("\nPresione ENTER para continuar...")

    def iniciarSesion(self):
         
         self.interfaz.iniciar_sesion_image()

         #Creamos un ciclo para verificar si existen usuarios registrados. 
         if len(self.registrodata['usuarios']) < 1 :
             print("No hay usuarios registrados")
             input("")
             inicio_sesion=False
             sesion =[inicio_sesion, 0]
             return sesion
         else:
             #Si el usuario se encuentra registrado, se le permitirá iniciar sesión
             existe=False
             nombre_usuario = (input('Ingrese su nombre de usuario:  ')).lower()
             #x=str(self.registrodata[self.registrodata['usuarios']==nombre_usuario]['contrasenas'])
             usuarios=list(self.registrodata['usuarios'])
             clave = (input('Ingrese su clave:  ')).lower()
             
             
             numerodedezplamiento = 1
             alfabeto = ("abcdefghijklmnopqrstuvwxyz")
             mensajecifrado = ('')
             mensajecifrado = ('') #se crea la variable donde se guardara el mensaje terminado
             for l in clave: #Iteramos por cara letra del mensaje
                 if l in alfabeto: #Si la letra está en el abecedario se reemplaza
                     posicionletra = alfabeto.index(l)
                     nuevaposicion = (posicionletra + numerodedezplamiento) % len(alfabeto) #se suma para moverse las unidades deseadas
                     mensajecifrado+= alfabeto[nuevaposicion] #se crea el nuevo alfabeto como una cadena
                 else: # si no se encuentra en el abecedario sólo se añade
                     mensajecifrado+= l

             clave = mensajecifrado
             
             
             posicon=0
             for i in usuarios:
                 if i == nombre_usuario:
                     existe=True
                     break
                 posicon=posicon+1   

             
             if existe==True:
                 x=self.registrodata[self.registrodata['usuarios']==nombre_usuario]['contrasenas']
                 for s in x:
                     y=str(s)

                 if y == clave:
                     inicio_sesion=True
                     ubicado = False

                                     
                     #Creamos un ciclo para determinar si el usuario puede continuar
                     #o no, dependiendo de lo que ingrese en la variable ubicación. 
                     while ubicado == False:
                     #Solicitamos la ubicación actual del usuario. 
                         ubicacion = (input('Ingrese su ubicación actual:  ')).lower()
                         if len(ubicacion)>0:
                             ubicado=True
                         else:
                             print('Es necesario introduccir una ubicación')
                             #En caso la variable ubicación no se encuentre vacía, el usuario podrá continuar. 
                         self.registrodata.loc[self.registrodata['usuarios']==nombre_usuario,'direccion']=ubicacion
                         #Se determina el número de veces que el usuario ingresa a la aplicación. 
                         conteo_ingresos= self.registrodata[self.registrodata['usuarios']==nombre_usuario]['ingresos a la aplicacion']
                         
                         #Se actualiza el DataFrame. 
                         self.registrodata.loc[self.registrodata['usuarios']==nombre_usuario,'ingresos a la aplicacion']= int(conteo_ingresos)+1
                     #Se guarda el DataFrame.
                     self.registrodata.to_csv('Estado_Sesion.csv',index=False)
                     #Se crea una lista que almacene el estado de la sesion y el nombre del usuario. 
                     sesion =[inicio_sesion, posicon, nombre_usuario]
                     return sesion #Retornamos la lista
                 else:
                     #Esta acción se ejecutará si se ingresa un dato erroneo
                     print('Escribio una contraseña incorrecta')
                     inicio_sesion=False 
                     #Se crea una lista que almacene el estado de la sesion. 
                     sesion =[inicio_sesion, 0]
                     return sesion #Retornamos la lista
             else:
                 
                 #Este acción se desplegará si se introduce un dato incorrecto. 
                 self.vista.dtIC()
                 input()
                 inicio_sesion=False
                 #Se crea una lista que almacene el estado de la sesion. 
                 sesion =[inicio_sesion, nombre_usuario]
                 return sesion #Retornamos la lista

    def main2(self, posicon, nombre): #Esta función despliega el menú secundario.
        #Esta acción empieza el contador con el tiempo. 
        starting_point = time.time()
        #Esta variable nos permite salir del ciclo. 
        estado = True
        #Se crea un ciclo que despliega las opciones del menú y lo reinicia cuando encuentra un error en los datos introducidos. 
        while estado:
            #Ejecutamos la función para mostrar la interfaz del menú en el código. 
            self.vista.menuSec()
            #Este variable almacena la ubicación del usuario acorde a su nombre. 
            ubica=self.registrodata[self.registrodata['usuarios']==nombre]['direccion']
            #Creamos un ciclo para guardar los valores de ubica en una variable tipo string. 
            for i in ubica:
                ubicacion = str(i)
            #Se convierten todas las letras a mayúsculas para una buena presentación. 
            ubicacion=ubicacion.upper()
            #Solicitamos el ingreso de una opción. 
            opcion2 =  input('Ingrese una opción del menu principal:  ')

            if opcion2 == '1':
                #Establecemos el estado de la sesión como inactiva. 
                self.estado_sesion['estado'] = False
                #Guarda el tiempo que se ha transcurrido desde que se empezó a contar. 
                tiempo_transcurrido = int(time.time() - starting_point)
                #Se guarda el tiempo transcurrido en la persona que ha iniciado sesión. 
                registro_tempo= self.registrodata.loc[self.registrodata['usuarios']==nombre,'tiempo pasado en la app']
                #Se actualiza el valor del tiempo. 
                self.registrodata.loc[self.registrodata['usuarios']==nombre,'tiempo pasado en la app']=registro_tempo+tiempo_transcurrido
                #Guardamos el DataFrame actualizado.
                self.registrodata.to_csv('Estado_Sesion.csv',index=False)
                estado = False #Salimos del ciclo
            elif opcion2 == '2':
                #Ejecutamos la función que despliega el modulo "parte2"
                self.Navegar_en_el_mapa(ubicacion)  


            elif opcion2 == '3':
                #Mostramos la ubicación actual del usuario 
                print(ubicacion)

            else: 
                
                #Mostramos un mensaje indicando que se ha ingresado un dato incorrecto y reiniciamos el ciclo
                self.vista.dtIC()
                input()
                
    def Navegar_en_el_mapa(self,direcciones): #Esta función es la pantalla del mapa que se presentó en el prototipo anterior
        opcion = "0"
        while opcion != "1":#Este ciclo sirve para regresar a donde se entaba en primer lugar
            #Mostramos la interfaz del programa del menú navegar.
            self.interfaz.navegar()
            #Mostramos la interzar del código. 
            self.vista.menuNaverMapa()
            opcion=input()#Estas son las opciones que en forma de botones aparecencen en la pantalla


            if opcion == "2":#Esta opcion lo manda a la pantalla de ingresar destino
                # ingresar_destino(direcciones)
                self.navegarmapa(direcciones) 

            elif opcion == "3":#Esta opcion le muestra que significan los iconos en la pantalla
                #La clave se esta ejemplificando de forma solo textual
                #Es por eso que solo se puso como se ve el icono y no la imagen como tal. 
                self.interfaz.informacion()
                self.vista.informacion()
                
                input("\nPresione ENTER para continuar...")

            elif opcion == "1":
                #Mostramos un mensaje para indicar que se regresará al menú anterior 
                print("Regresando...")

            else:
                #Se muestra un mensaje indicando que se ha cometido un error y se reinicia el programa. 
                self.vista.dtIC()
                
#----------------------------------------parte 2----------------------------------------------------------------------#
    def Navegar_en_el_mapa(self,direcciones): #Esta función es la pantalla del mapa que se presentó en el prototipo anterior
        opcion = "0"
        while opcion != "1":#Este ciclo sirve para regresar a donde se entaba en primer lugar
            #Mostramos la interfaz del programa del menú navegar.
            self.interfaz.navegar()
            #Mostramos la interzar del código. 
            opcion=input()#Estas son las opciones que en forma de botones aparecencen en la pantalla
            self.vista.NavegarEnMapa()

            if opcion == "2":#Esta opcion lo manda a la pantalla de ingresar destino
                # ingresar_destino(direcciones)
                self.navegarmapa(direcciones) 

            elif opcion == "3":#Esta opcion le muestra que significan los iconos en la pantalla
                #La clave se esta ejemplificando de forma solo textual
                #Es por eso que solo se puso como se ve el icono y no la imagen como tal. 
                self.interfaz.informacion()
                self.vista.informacion2()
                input("\nPresione ENTER para continuar...")

            elif opcion == "1":
                #Mostramos un mensaje para indicar que se regresará al menú anterior 
                print("Regresando...")

            else:
                #Se muestra un mensaje indicando que se ha cometido un error y se reinicia el programa. 
                self.vista.dtIC()
#----------------------------------------parte 3----------------------------------------------------------------------#
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
                

            else:     
                #Esta acción se ejecuta si el usuario ingresa una opción incorrecta, y se reinicia el programa.
                self.vista.dtIC()



    def menuPrin(self):#Esta funcion imprime la imagen de la pantalla de carga y al mismo tiempo lo imprime en
        #la consola
        self.interfaz.buscar()
        self.vista.buscar()

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

        self.empezarviaje () #Se llama a la funcion navegar por el mapa


    def información(self):       
        #Mostramos la interfaz del menú del código. 
        self.vista.informacion3()
        input("\nPresione ENTER para continuar...")

#----------------------------------------parte 4----------------------------------------------------------------------#
    def finalizar(self,elecciondeviaje):
        arribo = False
        opcionviaje = 0
        finalizar = False
        while finalizar != True:
            if elecciondeviaje == 1:
                # Cuando el usuario acepte el viaje, se desplegará esta
                #pantalla para que él o ella confirme si ya ha terminado su
                #viaje o si aún esta en ello. El mensaje se desplegará cíclicamente
                #ante un no y terminará cuando la respuesta sea un Sí.
                opcionviaje = int(input("""
        
        -        -----------------------------------------------------      - 
        -                     -¿Ha llegado a su destino?                    -
        -        -----------------------------------------------------      -
        -                 ______                        _____               -
        -                |1. SÍ |                      |2. NO|              -
        -                 ¯¯¯¯¯¯                        ¯¯¯¯¯               -
        ---------------------------------------------------------------------
            """))
                if opcionviaje == 2:
                    arribo = False
                elif opcionviaje == 1:
                    print ("Gracias, que todo haya sido de su agrado.") #Cuando el resultado de la anterior
                    #pantalla sea Sí, se desplegará esta parte del algoritmo
                    arribo = True
                    finalizar=True
                    input("\nPresione ENTER para continuar...")
                else:
                    #Pantalla mostrada si se ingresa un texto o número que no
                    #sea 1 o 2.
                    print('''
        ---------------------------------------------------------------------
        -                                                                   -
        -                  ¡Ingresó una opción incorrecta!                  -
        -                                                                   -
        ---------------------------------------------------------------------
                        ''')
            else:
                finalizar = True
        return arribo
        #La variable booleana Arribo regresa a los módulos previos para desplegar nuevamente
        #el menú de inicio sin cerrar la sesión ingresada

    def empezarviaje (self): #parámetro recibido del módulo Parte3
        #Se utiliza Int para asegurar carácter numérico
        arribo = False
        self.interfaz.mapa_de_ruta()
        eleccionviaje=0
         #Se imprime la variable mapadestino según su valor adquirido previamente.
        fin=False
        while fin==False:
            print ("¿Iniciar viaje?") #Se confirma el viaje cuando el usuario ya ha visto su recorrido.
            print ("1 = Sí")
            print ("2 = No")
            eleccionviaje = (input())
            if eleccionviaje == "2":
                fin=True
            elif eleccionviaje== "1":
                fin=True
            else: #Si su respuesta no es ni 1 ni 2, se mostrará esta pantalla.
                print('''
            ---------------------------------------------------------------------
            -                                                                   -
            -                  ¡Ingresó una opción incorrecta!                  -
            -                                                                   -
            ---------------------------------------------------------------------
                            ''')
        eleccionviaje = int(eleccionviaje)

        arribo = self.finalizar(eleccionviaje) #Se aplica la última función (la primera que fue mostrada),
        #cuyos valores ya fueron leídos por el programa. Su parámetro será el valor de la elección
        #sobre la confirmación del viaje.
        return arribo #La variable Arribo se regresa a los otros módulos nuevamente.
