from tkinter import*
import random 
import os

class Interfaz:
  

    #La siguiente función nos ayudará con el despliegue de mapas por medio de Tkinter a la hora en la que el usuario
    #ingresa un destino para poder iniciar su viaje. Esta función, lo que hace, es tener agrupadas en una lista una
    #serie de imágenes con mapas y la interfaz de la aplicación. Al tenerlas ya agrupadas, elegirá una imagen al azar,
    #y será mostrada en pantalla, previo a que el usuario inicie su viaje.
    def mapa_de_ruta(self):
        ventana = Tk() # Protocolo para Tkinter
        ventana.title("Esta es tu ruta") #Título de la ventana donde será mostrada
        ventana.geometry("250x495") #Dimensiones de la ventana

        listaimagenes = [] #En esta lista serán alojadas las imágenes
        file_path = os.path.dirname(os.path.abspath(__file__)) #En las siguientes líneas se irán ingresando cada una de
        #las imágenes a utilizar; al estar ya alojadas dentro de variables, estas variables serán las que serán 
        #almacenadas en la lista.
        imagen_path = os.path.join(file_path, 'Imagenes', '7.png')
        imagen = PhotoImage(file=imagen_path) 
        imagen1 = imagen.subsample(3,3)
        listaimagenes.append(imagen1)
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'Imagenes', '8.png')
        imagen = PhotoImage(file=imagen_path)
        imagen2 = imagen.subsample(3,3)
        listaimagenes.append(imagen2)
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'Imagenes', '9.png')
        imagen = PhotoImage(file=imagen_path)
        imagen3 = imagen.subsample(3,3)
        listaimagenes.append(imagen3)
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'Imagenes', '10.png')
        imagen = PhotoImage(file=imagen_path)
        imagen4 = imagen.subsample(3,3)
        listaimagenes.append(imagen4)
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'Imagenes', '11.png')
        imagen = PhotoImage(file=imagen_path)
        imagen5 = imagen.subsample(3,3)
        listaimagenes.append(imagen5)
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'Imagenes', '12.png')
        imagen = PhotoImage(file=imagen_path)
        imagen6 = imagen.subsample(3,3)
        listaimagenes.append(imagen6)
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'Imagenes', '13.png')
        imagen = PhotoImage(file=imagen_path)
        imagen7 = imagen.subsample(3,3)
        listaimagenes.append(imagen7)
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'Imagenes', '14.png')
        imagen = PhotoImage(file=imagen_path)
        imagen8 = imagen.subsample(3,3)
        listaimagenes.append(imagen8)
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'Imagenes', 'Mapa_1.png')
        imagen = PhotoImage(file=imagen_path)
        imagen9 = imagen.subsample(3,3)
        listaimagenes.append(imagen9)
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'Imagenes', 'Mapa_2.png')
        imagen = PhotoImage(file=imagen_path)
        imagen10 = imagen.subsample(3,3)
        listaimagenes.append(imagen10)
        azar = random.choice(listaimagenes) #Ya teniendo todos los elementos en la lista, se utilizará la librería 
        #Random, con la cual se elegirá un elemento de esta misma lista.
        fondo = Label(ventana, image = azar).place(x = -140, y = -130) #Se indica que la imagen elegida será mostrada
        #bajo las siguientes condiciones y dimensiones.
        ventana.mainloop() 
        return ventana #Se devolverá la variable ventana, ya que fue la varaible que recibió todos los cambios 


    def menu(self):
        ventana = Tk() # Protocolo para Tkinter
        ventana.title("Menú principal")
        ventana.geometry("250x495")

        file_path = os.path.dirname(os.path.abspath(__file__)) #En las siguientes líneas se irán ingresando cada una de
        #las imágenes a utilizar; al estar ya alojadas dentro de variables, estas variables serán las que serán 
        #almacenadas en la lista.
        imagen_path = os.path.join(file_path, 'Imagenes', '1.png')
        imagen = PhotoImage(file=imagen_path) 
        imagen1 = imagen.subsample(3,3)
        fondo = Label(ventana, image = imagen1).place(x = -140, y = -130) #Se indica que la imagen elegida será mostrada
        #bajo las siguientes condiciones y dimensiones.
        ventana.mainloop() 
        return ventana #Se devolverá la variable ventana, ya que fue la varaible que recibió todos los cambios 

    def iniciar_sesion_image(self):
        ventana = Tk() # Protocolo para Tkinter
        ventana.title("Iniciar sesión")
        ventana.geometry("250x495")

        file_path = os.path.dirname(os.path.abspath(__file__)) #En las siguientes líneas se irán ingresando cada una de
        #las imágenes a utilizar; al estar ya alojadas dentro de variables, estas variables serán las que serán 
        #almacenadas en la lista.
        imagen_path = os.path.join(file_path, 'Imagenes', '3.png')
        imagen = PhotoImage(file=imagen_path) 
        imagen1 = imagen.subsample(3,3)
        fondo = Label(ventana, image = imagen1).place(x = -140, y = -130)#Se indica que la imagen elegida será mostrada
        #bajo las siguientes condiciones y dimensiones.
        ventana.mainloop() 
        return ventana #Se devolverá la variable ventana, ya que fue la variable que recibió todos los cambios tanto
        #de imagen como de dimensiones.

    def registrar(self):
        ventana = Tk() # Protocolo para Tkinter
        ventana.title("Registrarse")
        ventana.geometry("250x495")

        file_path = os.path.dirname(os.path.abspath(__file__)) #En las siguientes líneas se irán ingresando cada una de
        #las imágenes a utilizar; al estar ya alojadas dentro de variables, estas variables serán las que serán 
        #almacenadas en la lista.
        imagen_path = os.path.join(file_path, 'Imagenes', '2.png')
        imagen = PhotoImage(file=imagen_path) 
        imagen1 = imagen.subsample(3,3)
        fondo = Label(ventana, image = imagen1).place(x = -140, y = -130) #Se indica que la imagen elegida será mostrada
        #bajo las siguientes condiciones y dimensiones.
        ventana.mainloop() 
        return ventana #Se devolverá la variable ventana, ya que fue la varaible que recibió todos los cambios 

    def navegar(self):
        ventana = Tk() # Protocolo para Tkinter
        ventana.title("Navegar")
        ventana.geometry("250x495")

        file_path = os.path.dirname(os.path.abspath(__file__)) #En las siguientes líneas se irán ingresando cada una de
        #las imágenes a utilizar; al estar ya alojadas dentro de variables, estas variables serán las que serán 
        #almacenadas en la lista.
        imagen_path = os.path.join(file_path, 'Imagenes', '4.png')
        imagen = PhotoImage(file=imagen_path) 
        imagen1 = imagen.subsample(3,3)
        fondo = Label(ventana, image = imagen1).place(x = -140, y = -130) #Se indica que la imagen elegida será mostrada
        #bajo las siguientes condiciones y dimensiones.
        ventana.mainloop() 
        return ventana #Se devolverá la variable ventana, ya que fue la varaible que recibió todos los cambios 

    def informacion(self):
        ventana = Tk() # Protocolo para Tkinter
        ventana.title("Información")
        ventana.geometry("250x495")

        file_path = os.path.dirname(os.path.abspath(__file__)) #En las siguientes líneas se irán ingresando cada una de
        #las imágenes a utilizar; al estar ya alojadas dentro de variables, estas variables serán las que serán 
        #almacenadas en la lista.
        imagen_path = os.path.join(file_path, 'Imagenes', '16.png')
        imagen = PhotoImage(file=imagen_path) 
        imagen1 = imagen.subsample(3,3)
        fondo = Label(ventana, image = imagen1).place(x = -140, y = -130)#Se indica que la imagen elegida será mostrada
        #bajo las siguientes condiciones y dimensiones.
        ventana.mainloop() 
        return ventana #Se devolverá la variable ventana, ya que fue la varaible que recibió todos los cambios 

    def buscar(self):
        ventana = Tk() # Protocolo para Tkinter
        ventana.title("Buscar")
        ventana.geometry("250x495")

        file_path = os.path.dirname(os.path.abspath(__file__)) #En las siguientes líneas se irán ingresando cada una de
        #las imágenes a utilizar; al estar ya alojadas dentro de variables, estas variables serán las que serán 
        #almacenadas en la lista.
        imagen_path = os.path.join(file_path, 'Imagenes', '15.png')
        imagen = PhotoImage(file=imagen_path) 
        imagen1 = imagen.subsample(3,3)
        fondo = Label(ventana, image = imagen1).place(x = -140, y = -130)#Se indica que la imagen elegida será mostrada
        #bajo las siguientes condiciones y dimensiones.
        ventana.mainloop() 
        return ventana #Se devolverá la variable ventana, ya que fue la varaible que recibió todos los cambios 

