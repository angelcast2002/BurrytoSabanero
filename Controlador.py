from Parte2 import Parte2
from Estadisticas import Estadisticas
from Interfaz import Interfaz
import pandas as pd
import time


class Controlador:

    def __init__(self,vista):
        self.vista = vista
        self.interfaz = Interfaz()
        self.estadisticas = Estadisticas()
        self.parte2 = Parte2()

        self.estado_sesion = {
        'nombre_usuario': '',
        'clave': '', 
        'direccion_actual': '',
        'estado': False
        }

        self.direcciones = {}
        

    #Almacenamos en una variable lo que contiene nuestro archivo.csv
        self.registrodata = pd.read_csv("Estado_Sesion.csv")

        
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
                print('''
        ---------------------------------------------------------------------
        -                                                                   -
        -                   ¡Gracias por usar TranzMap!                     -
        -                                                                   -
        ---------------------------------------------------------------------
                ''')
                #Convertimos la  variable a False para salir del menú y terminar el programa. 
                estado = False 
            #ACTUALIZACIÓN
            elif opcion == '21240':
                #Este apartado permite ingresar al modo de desarrollador. 
                self.estadisticas.estadisticas()
            else:
                #Este mensaje se desplegará si el usuario ingresa un valor incorrecto 
                print("""
        ---------------------------------------------------------------------
        -                   ¡Ha ingresado un dato incorrecto!               -
        -                           Intente de nuevo.                       -
        ---------------------------------------------------------------------
                        """)
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

        #ACTUALIZACIÖN
        #Se verificará que no existe un usuario ya registrado con el nombre anteriormente escrito.
        usuario_repetido=self.registrodata[self.registrodata['usuarios']==nombre_usuario]['usuarios']
        #Se contará el número de usuarios que aparecen en la lista para observar si no existe algún usuario repetido. 
        repetido=len(usuario_repetido)
        #Con esto se determinará el número de veces que se encuentra el usuario repetido y devolverá un mensaje indicado lo sucedido. 
        if repetido>0:
            print('Este nombre de usuario esta repetido')

        #CAMBIOS
        #Formato anteriormente empleado cuando no se contaba con persistencia de datos. 
        #estado_sesion['nombre_usuario'] = nombre_usuario 
        #estado_sesion['clave'] = clave 
        #estado_sesion['direccion_actual'] = ubicacion

        else:
            #ACTUALIZACIÓN+
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
         #ACTUALIZACIÓN
         #Le permite al usuario ingresar a la aplicación.
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
             posicon=0
             for i in usuarios:
                 if i == nombre_usuario:
                     existe=True
                     break
                 posicon=posicon+1   

             #ACTUALIZACIÓN
             if existe==True:
                 x=self.registrodata[self.registrodata['usuarios']==nombre_usuario]['contrasenas']
                 for s in x:
                     y=str(s)

                 if y == clave:
                     inicio_sesion=True
                     ubicado = False

                     #ACTUALIZACIÓN                
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
                 #ACTUALIZACIÓN 
                 #Este acción se desplegará si se introduce un dato incorrecto. 
                 print("""
         ---------------------------------------------------------------------
         -                   ¡Ha ingresado un dato incorrecto!               -
         -                           Intente de nuevo.                       -
         ---------------------------------------------------------------------
                 """)
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
                self.parte2.Navegar_en_el_mapa(ubicacion)  


            elif opcion2 == '3':
                #Mostramos la ubicación actual del usuario 
                print(ubicacion)

            else: 

                #ACTUALIZACIÓN 
                #Mostramos un mensaje indicando que se ha ingresado un dato incorrecto y reiniciamos el ciclo
                print("""
        ---------------------------------------------------------------------
        -                   ¡Ha ingresado un dato incorrecto!               -
        -                           Intente de nuevo.                       -
        ---------------------------------------------------------------------
                """)
                input()