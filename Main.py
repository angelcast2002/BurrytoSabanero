from Controlador import Controlador
from Vista import Vista

def main():

    vista = Vista()
    controlador = Controlador(vista)
    controlador.main()
 


if __name__ == '__main__':
    main()
    
