import tkinter as Tk
from Parte3 import Parte3
from Interfaz import Interfaz

class Parte2:
    

    def __init__(self):
        self.interfaz = Interfaz()
        self.parte3 = Parte3()
    
    def Navegar_en_el_mapa(self,direcciones): #Esta función es la pantalla del mapa que se presentó en el prototipo anterior
        opcion = "0"
        while opcion != "1":#Este ciclo sirve para regresar a donde se entaba en primer lugar
            #Mostramos la interfaz del programa del menú navegar.
            self.interfaz.navegar()
            #Mostramos la interzar del código. 
            opcion=input(''' 
        ----------------------------------------------------------------------
        -                                                                    -
        -                                                                    -
        -       _                        __  __                              -
        -      | |     ___   __ _   ___ |  \/  |  __ _   _ __                -
        -      | |__  / _ \ / _` | / _ \| |\/| | / _` | | '_ \               -
        -      |____| \___/ \__, | \___/|_|  |_| \__,_| | .__/               -
        -                   |___/                       |_|                  -
        -                                                                    -
        -                                                                    -
        -                                                                    -
        -                                                                    -
        -                                                                    -
        -      _____________                        ______________________   -
        -     |1. REGRESAR  |                      |2. INGRESAR DIRECCIÓN |  -
        -      ¯¯¯¯¯¯¯¯¯¯¯¯¯                        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   -
        -                     _______________________                        -
        -                    |3.¿QUÉ SON ESOS ÍCONOS?|                       -
        -                     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                        -
        ----------------------------------------------------------------------
    
        ''')#Estas son las opciones que en forma de botones aparecencen en la pantalla


            if opcion == "2":#Esta opcion lo manda a la pantalla de ingresar destino
                # ingresar_destino(direcciones)
                self.parte3.navegarmapa(direcciones) 

            elif opcion == "3":#Esta opcion le muestra que significan los iconos en la pantalla
                #La clave se esta ejemplificando de forma solo textual
                #Es por eso que solo se puso como se ve el icono y no la imagen como tal. 
                self.interfaz.informacion()
                print(''' 
        ---------------------------------------------------------------------
        -                                                                   -
        -                                                                   -
        -       _                        __  __                             -
        -      | |     ___   __ _   ___ |  \/  |  __ _   _ __               -
        -      | |__  / _ \ / _` | / _ \| |\/| | / _` | | '_ \              -
        -      |____| \___/ \__, | \___/|_|  |_| \__,_| | .__/              -
        -                   |___/                       |_|                 -
        ----------------------------Nuestra clave----------------------------
        -                 ___________________________________               -
        -                | Nuestros Íconos, nuestra adicción |              -
        -                 -----------------------------------               -
        -     __________________________________________________________    -
        -    |1) [Bus amarillo]. Vías de transpote público              |   -
        -    |2) [Bus rojo]. Vías de transpote gubernamental            |   -
        -    |3) [Bus negro]. Ruta del bus a tu destino                 |   -
        -    |4) [G]oblo celeste con una bici]. Estaciones de biciceta  |   -
        -    |5) [Globo rojo]. Tú estas aquí                            |   -
        -    |6) [Estación de bus]. Estación de bus                     |   -
        -     ----------------------------------------------------------    -
        ---------------------------------------------------------------------

                ''')
                input("\nPresione ENTER para continuar...")

            elif opcion == "1":
                #Mostramos un mensaje para indicar que se regresará al menú anterior 
                print("Regresando...")

            else:
                #Se muestra un mensaje indicando que se ha cometido un error y se reinicia el programa. 
                print('''
        ---------------------------------------------------------------------
        -                                                                   -
        -                  ¡Ingresó una opción incorrecta!                  -
        -                                                                   -
        ---------------------------------------------------------------------
                ''')

