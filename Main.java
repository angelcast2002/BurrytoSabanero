import java.util.Scanner;

import javax.swing.text.html.parser.DTD;

import java.util.ArrayList;
import java.util.Arrays;
public class Main{
    /* Angel Castellanos POO seccion 21 carnet 21700*/
    public static void main(String[] args){ 

        /* Aqui creamos las variables a usar*/
        int desicion;
        int UbicacionActual, UbicacionDestino;
        boolean salir=false;
        int e;
        e = 0;


        Scanner sc = new Scanner(System.in);
        Usuario usuario = new Usuario();
        Controlador controlador = new Controlador();


        System.out.println("+-----------------------------------------------------------------------");
        System.out.println("  :: :: :: :: :: :: :: :: BURRITOSABANERO S.A. :: :: :: :: :: :: :: :: ::");
        System.out.println("  :: :: :: :: :: :: :: !Bienvenido a BURITOSABANERO¡ :: :: :: :: :: :: :: ");
        System.out.println("  :: :: :: :: :: :: Por favor, Ingrese los datos del usuario =) :: :: :: ::");
        System.out.println("+-----------------------------------------------------------------------");
            
            /* para que no se deban de ingresar todos los canes al mismo tiempo
            se ingresa 1 a las vez usando la variable e como nuestro indice*/
            System.out.println("\nIngresando un nuevo usuario.....");
            System.out.println("\nPor favor, Ingrese los siguientes datos:\n ");

            System.out.println("\nNombre de usuario");
            String NombreUsuario = sc.nextLine();

            System.out.println("\nClave");
            String Clave = sc.nextLine();
            
            System.out.println("\n\nSeleccione una de las siguientes ubicaciones para establecerla como la actual");
            System.out.println("\n\n1 Para Parque Central\n2 Para UVG\n3 Para Miraflores\n");
            int SeleccionUbicacion = sc.nextInt();
            UbicacionActual = 0;

            if(SeleccionUbicacion == 1){

                UbicacionActual = 1;

            }

            else if (SeleccionUbicacion == 2){

                UbicacionActual = 2;

            }

            else if (SeleccionUbicacion == 3){

                UbicacionActual = 3;

            }

            controlador.usuario.add(new Usuario(NombreUsuario, Clave, UbicacionActual));
            

        
        /* el menu se ingresa en un bucle para que no se termine el programa hasta que el usuario lo decida*/
        while (salir==false) {
            
            /* Se pregunta que se desea hacer*/
            System.out.println("\n\nQue desea hacer? \n1 Para iniciar un viaje \n2 Para cambiar la ubicacion actual\n3 Para salir\n");
            /* segun lo decidido se hara algo distinto*/
            desicion = sc.nextInt();
            sc.nextLine();
            
            if(desicion==1){
                System.out.println("\n\nA donde desea ir?");
                System.out.println("\n\n1 Para Parque Central\n2 Para UVG\n3 Para Miraflores\n");
                SeleccionUbicacion = sc.nextInt();
                UbicacionDestino = 0;

                if(SeleccionUbicacion == 1){

                    UbicacionDestino = 1;

                }

                else if (SeleccionUbicacion == 2){

                    UbicacionDestino = 2;

                }

                else if (SeleccionUbicacion == 3){

                    UbicacionDestino = 3;

                }
               
                System.out.println(controlador.Ubicaciones(UbicacionDestino));

            }

            if(desicion==2){

                System.out.println("\n\nQue ubicacion desea elegir?");
                System.out.println("\n\n1 Para Parque Central\n2 Para UVG\n3 Para Miraflores");
                SeleccionUbicacion = sc.nextInt();
                UbicacionActual = 0;

                if(SeleccionUbicacion == 1){

                    UbicacionActual = 1;

                }

                else if (SeleccionUbicacion == 2){

                    UbicacionActual = 2;

                }

                else if (SeleccionUbicacion == 3){

                    UbicacionActual = 3;

                }

                controlador.usuario.get(0).setdireccionActual(UbicacionActual);

            }

            if(desicion==3){
                System.out.println("\n\nCerrando el programa");
                salir = true;
            }


        }
    }
}





