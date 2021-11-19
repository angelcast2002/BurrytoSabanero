import tkinter as Tk
import pandas as pd
import numpy as np
from tkinter import*
from Interfaz import Interfaz
import matplotlib.pyplot as plt

class Estadisticas:
    def __init__(self):
        self.interfaz = Interfaz()

    #Esta función realiza un cálculo del promedio del tiempo y de los ingresos.
    def promedio(self, data, funcion):
        promedio=0 #Se crea una variable y se le asigna el un valor 0.
        numero=0 #Se crea una variable y se le asigna el un valor 0.
        ingresos= list(data[funcion]) #Almacenamos en una variable el resultado de lista los datos en la posicion "función".
        for i in ingresos: #Se crea un ciclo para contar el número de elementos que posee la lista. 
            promedio=promedio+i
            numero=numero+1
        promedio=promedio/numero #Se realizan los calculos para determinar el promedio de datos. 
        promedio=str(promedio) #El resultado se convierte en una variable tipo "string"
        return promedio #Retornamos la variable
    
    def Organiza_mas(self, data, funcion):#Función que devuelve el DataFrame para generar la gráfica.
        dic_top={}
        list_top=[]
        #Se declaran el diccionario y la lista vacíos que se planean utilizar.
        usuario=list(data['rutas'])#Se guardan en un listado los lugares en el Data Frame.
        for c in usuario:
            #Se buscan los datos de la cantidad de veces que aparece en una lista.
            d=list(data[data['rutas']==c][funcion])
            for i in d:
                s=i
            list_top.append((s, c))#Se guarda como una lista en la lista.
        #Se ordena para obtener los mejores 5.
        list_top.sort(reverse=True)
        #Se declaran las listas finales para almacenar los datos que se usaran en el DataFrame para la gráfica.
        #Se realiza un ciclo for que detecte los datos para la gráfica.
        if len (list_top)<3:
            limite=len(list_top)
        else:
            limite=3
        mejores_usuarios=[]
        max_funcion=[]
        #de los 5 lugares más frecuentados...
        for s in list_top[:limite]:
            #Se añade a una lista el nombre del lugar.
            mejores_usuarios.append(s[1])
            #Se hacen listas filtrando los datos para obtener
            #las listas de las veces en las que se han seleccionado.
            #Se añade la lista de las veces a una lista.
            max_funcion.append(s[0])
           
        #Se añaden las listas a unas llaves en el diccionario para solo hacerlo en DataFrame.
        
        dic_top['Rutas']=mejores_usuarios
        dic_top['No. Busquedas']=max_funcion
        #Se convierte el diccionario en un DataFrame.   
        graf=pd.DataFrame(dic_top)
        #Se debe mover el índice porque de esta manera se acomodan los datos para hacer la gráfica.
        graf.set_index('Rutas',inplace=True)
        return graf #Se regresa el DataFrame.
        
    
    def Organiza_menos(self, data, funcion):#Función que devuelve el DataFrame para la gráfica.
        dic_top={}
        list_top=[]
        #Se declaran el diccionario y la lista vacíos que se planean utilizar.
        usuario=list(data['rutas'])#Se guardan en un listado los lugares en el DataFrame.
        for c in usuario:
            #Se buscan los datos de la cantidad de veces seleccionadas en una lista.
            d=list(data[data['rutas']==c][funcion])
            for i in d:
                s=i
            list_top.append((s, c))#Se guarda como una lista en la lista.
        #Se ordena para obtener los menores 5.
        list_top.sort()
        #Se declaran las listas finales para almacenar los datos que se usaran en el DataFrame para la gráfica.
        #Se realiza un ciclo for que detecte los datos para la gráfica.
        if len (list_top)<3:
            limite=len(list_top)
        else:
            limite=3
        mejores_usuarios=[]
        max_funcion=[]
        #de los 5 lugares menos frecuentados...
        for s in list_top[:limite]:
            #Se añade a una lista el nombre del lugar.
            mejores_usuarios.append(s[1])
            #Se hacen listas filtrando los datos para obtener
            #las listas de las veces en las que se han seleccionado.
            #Se añade la lista de las veces a una lista.
            max_funcion.append(s[0])
            
        #Se añaden las listas a unas llaves en el diccionario para solo hacerlo en DataFrame.
        
        dic_top['Rutas']=mejores_usuarios
        dic_top['No. Busquedas']=max_funcion
        #Se convierte el diccionario en un DataFrame.   
        graf=pd.DataFrame(dic_top)
        #Se debe mover el índice porque de esta manera se acomodan los datos para hacer la gráfica
        graf.set_index('Rutas',inplace=True)
        return graf #Se regresa el DataFrame.
        
    
    def Organizar_mas(self, data, funcion):#Función que devuelve el DataFrame para la grafica.
        dic_top={}
        list_top=[]
        #Se declaran el diccionario y la lista vacíos que se planea utilizar.
        usuario=list(data['usuarios'])#Se guardan en un listado los usuarios en el DataFrame.
        for c in usuario:
            #Se buscan los datos de la cantidad de veces ingresadas en una lista.
            d=list(data[data['usuarios']==c][funcion])
            for i in d:
                s=i
            list_top.append((s, c))#Se guarda como una lista en la lista.
        #Se ordena para obtener los mejores 5.
        list_top.sort(reverse=True)
        #Se declaran las listas finales para almacenar los datos que se usaran en el DataFrame para la gráfica.
        #Se realiza un ciclo for que detecte los datos para la gráfica.
        if len (list_top)<5:
            limite=len(list_top)
        else:
            limite=5
        mejores_usuarios=[]
        max_funcion=[]
        #de los 5 usuarios que más han ingresado a la aplicación...
        for s in list_top[:limite]:
            #Se añade a una lista el nombre del usuario.
            mejores_usuarios.append(s[1])
            #Se hacen listas filtrando los datos para obtener
            #las listas de cantidad de veces en las que se ha ingresado.
            #Se añade la lista de las veces en las que se ha ingresado.
            max_funcion.append(s[0])
            
        #Se añaden las listas a unas llaves en el diccionario para solo hacerlo en DataFrame.
        
        dic_top['usuarios']=mejores_usuarios
        dic_top[funcion]=max_funcion
        #Se convierte el diccionario en un DataFrame.   
        graf=pd.DataFrame(dic_top)
        #Se debe mover el índice porque, de esta manera, se acomodan los datos para hacer la gráfica.
        graf.set_index('usuarios',inplace=True)
        return graf #Se regresa el DataFrame.
        
    
    def Organizar_menos(self, data, funcion):#Función que devuelve el data frame para la gráfica.
        dic_top={}
        list_top=[]
        #Se declaran el diccionario y la lista vacios que se planea utilizar.
        usuario=list(data['usuarios'])#Se guardan en un listado los usuarios en el Data Frame.
        for c in usuario:
            #Se buscan los datos de la cantidad de veces ingresadas en una lista.
            d=list(data[data['usuarios']==c][funcion])
            for i in d:
                s=i
            list_top.append((s, c))#Se guarda como una lista en la lista.
        #Se ordena para obtener los menores 5.
        list_top.sort()
        #Se declaran las listas finales para almacenar los datos que se usaran en el DataFrame para la gráfica.
        #Se realiza un ciclo for que detecte los datos para la gráfica.
        if len (list_top)<5:
            limite=len(list_top)
        else:
            limite=5
        peores_usuarios=[]
        menos_funcion=[]
        #de los 5 usuarios que menos han ingresado a la aplicación...
        for s in list_top[:limite]:
            #Se añade a una lista el nombre del usuario.
            peores_usuarios.append(s[1])
            #Se hacen listas filtrando los datos para obtener
            #las listas de cantidad de veces en las que se ha ingresado.
            #Se añade la lista de las veces en las que se ha ingresado.
            menos_funcion.append(s[0])
            
        #Se añaden las listas a unas llaves en el diccionario para solo hacerlo en Data Frame.
        
        dic_top['usuarios']=peores_usuarios
        dic_top[funcion]=menos_funcion
        #Se convierte el diccionario en un DataFrame.   
        graf=pd.DataFrame(dic_top)
        #Se debe mover el índice porque de esta manera se acomodan los datos para hacer la gráfica.
        graf.set_index('usuarios',inplace=True)
        return graf #Se regresa el DataFrame.
        
    
    def trafico_usu(self, data): #Función utilizada para graficar todo lo relacionado con el tráfico de usuarios; esta función
    #mostrará los cinco mayores y menores ingresos a la aplicación, así también como el promedio de todos los 
    #ingresos, dependiendo de lo que pida el desarrollador por medio de su menú integrado.
        estado=False
        if len(list(data['usuarios']))<1: #Si no hay ningún dato dentro del archivo en donde están los datos guardados,
        #será mostrado en pantalla el siguiente mensaje.
            estado=True
            print('No se han investigado rutas hasta el momento')
        while estado==False: #la varaible Estado será utilizada para el siguiente, en el cual están el menú y el
        #desarrollo de cada una de sus opciones.
            opcion=input('''
        Quiere que se le prensente una grafica con:
        [1] Los cinco mayores ingresos a la aplicacion
        [2] Los cinco menores ingresos a la aplicacion
        [3] El promedio de ingresos por usuario 
            - ''')
            if opcion == '1': #Si se elije esta opción, se mostrará en pantalla la gráfica con los cinco mayores 
            #ingresos a la aplicacion.
                grafi=self.Organizar_mas(data, 'ingresos a la aplicacion')
                estado=True
                grafi.plot(kind = 'bar', stacked = 'True',alpha =1, width = 0.73,figsize=(4,6))
                plt.show()
            elif opcion == '2': #Si se elije esta opción, se mostrará en pantalla la gráfica con los cinco menores 
            #ingresos a la aplicacion.
                grafi=self.Organizar_menos(data, 'ingresos a la aplicacion')
                estado=True
                grafi.plot(kind = 'bar', stacked = 'True',alpha =1, width = 0.73,figsize=(4,6))
                plt.show()
            elif opcion == '3': #Si se elije esta opción, se mostrará en pantalla el promedio de ingresos por usuario.
                estado=True
                print('El promedio de ingresos a la aplicacion por usuario es: ' + self.promedio(data,'ingresos a la aplicacion' ))
            else: #Si ninguna de las opciones anteriores es elegida, se mostrará el siguiente mensaje.
            #Seguidamente, se volverá a mostrar de forma cíclica el menú de opciones.
                print('Presionó una opcion incorrecta, pruebe de nuevo')
            
        
    
    def rutas_mas(self): #Esta función filtra las 3 rutas más y menos buscadas con la ayuda de su menú integrado. 
        estado=False #Esta variable nos permite salir del menú.
        rutas=pd.read_csv('rutas.csv')
        if len(list(rutas['rutas']))<1: #si el listado de rutas contiene más de un valor, se mostrará el siguiente mensaje: 
            print('No se han investigado rutas hasta el momento')
        else:
            #Se creará un ciclo para que se reinicie cada vez que el usuario cometa un error. 
            while estado==False:
                #Mostramos el siguiente mensaje y guardamos lo que el usuario introduzca. 
                opcion=input('''
        Quiere que se le prensente cuales son:
        [1] Las tres rutas mas buscadas
        [2] Las tres rutas menos buscadas
                - ''')
                if opcion == '1':
                    #Esta acción ordena el DataFrame que la gráfica mostrará con las rutas más buscadas
                    grafi=self.Organiza_mas(rutas, 'conteo')
                    presentar=list(grafi.index) #Almacenamos en una lista los indices del DataFrame
                    print('''
        Las rutas que se han buscado mas veces hasta ahora son:''')
                    for i in presentar: #Creamos un ciclo para presentar los datos.
                        print('''
        - '''+i)
                    grafi.plot(kind = 'bar', stacked = 'True',alpha =1, width = 0.73,figsize=(4,6)) #Presentamos los datos de forma gráfica
                    plt.show()
                    estado=True #Salimos del ciclo. 
                elif opcion == '2':
                    #Esta acción ordena el DataFrame que la gráfica mostrará con las rutas menos buscadas
                    grafi=self.Organiza_menos(rutas, 'conteo')
                    presentar=list(grafi.index) #Almacenamos en una lista los indices del DataFrame
                    print('''
        Las rutas que se han buscado menos veces hasta ahora son:''')
                    for i in presentar: #Creamos un ciclo para presentar los datos.
                        print('''
        - '''+i)
                    grafi.plot(kind = 'bar', stacked = 'True',alpha =1, width = 0.73,figsize=(4,6)) #Presentamos los datos de forma gráfica
                    plt.show()
                    estado=True  #Salimos del ciclo. 
                else:
                    #Este mensaje se desplegará si el usuario ingresa un dato erroneo y reinicia el ciclo. 
                    print('Presionó una opcion incorrecta, pruebe de nuevo')
    
    
    
                    
    def tiempo_rel(self, data): #Esta función se encarga de filtrar los cinco mayores y menores tiempos registrados en la aplicación
    #así como el promedio de los tiempos registrados con la ayuda de su menú integrado.  
        estado=False
        if len(list(data['usuarios']))<1: #si el listado de rutas contiene más de un valor, se mostrará el siguiente mensaje: 
            estado=True
            print('No se han investigado rutas hasta el momento')
        #Se creará un ciclo para que se reinicie cada vez que el usuario cometa un error. 
        while estado==False:
            #Mostramos el siguiente mensaje y guardamos lo que el usuario introduzca.
            opcion=input('''
        Quiere que se le prensente una grafica con:
        [1] Los cinco mayores tiempos registrados en la aplicacion
        [2] Los cinco menores tiempos registrados en la aplicacion
        [3] El promedio de tiempos registrados en la aplicacion
            - ''')
            if opcion == '1':
                #Esta acción ordena el DataFrame que la gráfica mostrará con los cinco mayores tiempos. 
                grafi=self.Organizar_mas(data, 'tiempo pasado en la app')
                grafi.plot(kind = 'bar', stacked = 'True',alpha =1, width = 0.73,figsize=(4,6))
                plt.show() #Mostramos los datos en una gráfica. 
                estado=True #Salimos del ciclo. 
            elif opcion == '2':
                #Esta acción ordena el DataFrame que la gráfica mostrará con los cinco menores tiempos. 
                grafi=self.Organizar_menos(data, 'tiempo pasado en la app')
                grafi.plot(kind = 'bar', stacked = 'True',alpha =1, width = 0.73,figsize=(4,6))
                plt.show() #Mostramos los datos en una gráfica.
                estado=True #Salimos del ciclo. 
            elif opcion == '3':
                print('El promedio de tiempo invertido en la aplicacion por usuario es de ' + self.promedio(data, 'tiempo pasado en la app')+' segundos')
                estado=True #Salimos del ciclo. 
            else:
                #Si el usuario ingresa un dato incorrecto, entonces el ciclo se reiniciará. 
                print('Presionó una opcion incorrecta, pruebe de nuevo')
    
    
                
    
    def estadisticas(self): #Esta función despliega el menú que permite acceder a toda las funciones que se encargan de 
    #realizar calculos estadísticos para que el usuario los pueda observar gracias a su menú integrado. 
        estado=False #Esta variable permite salir del ciclo.
        #Creamos un ciclo para que se pueda ejecutar cada vez que no introduzca uno de los datos solicitados. 
        data=pd.read_csv('Estado_Sesion.csv')
        while estado == False:
            print('''
        Bienvenido al apartado del desarrollador las opciones que puedes verificar son:
        [1] Trafico de usuarios
        [2] Tiempo que ha sido usada la aplicacion
        [3] Salir del apartado desarrollador''')
            opcion=input()
            #Evaluamos las opcione con respecto a lo que el usuario ingrese y ejecutamos una función acorde a los solicitado. 
            if opcion=='1':
                self.trafico_usu(data)
            elif opcion=='2':
                self.tiempo_rel(data)
            elif opcion == '3':
                estado=True
            else:
                #Esta opción indica que se cometió un error al ingresar los datos y reinicia el ciclo.
                print('Escogio una opcion incorrecta, vuelva a escoger')
    
    
    
    
    
    
    
    
    