from tkinter import *
from Interfaz import Interfaz
#Se inicia con la función final, para que de esta manera éste sea leído 
#antes por el programa. Esto no servirá para que las variables de
#finalizar sean leídas y reconocidas.
class Parte4:
    def __init__(self):
        self.interfaz = Interfaz()

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
        ---------------------------------------------------------------------
        -                                                                   -
        -                                                                   -
        -      _____                            __  __                      -
        -     |_   _|  _ _   __ _   _ _    ___ |  \/  |  __ _   _ __        -
        -       | |   | '_| / _` | | ' \  |_ / | |\/| | / _` | | '_ \       -
        -       |_|   |_|   \__,_| |_||_| /__| |_|  |_| \__,_| | .__/       -
        -                                                      |_|          -
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
