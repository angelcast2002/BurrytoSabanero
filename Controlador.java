import java.util.Scanner;
import java.util.ArrayList;

public class Controlador {
    
    ArrayList<Usuario> usuario = new ArrayList<>();

    public String Ubicaciones(int ubicacionDestino){
        
        String mensaje = "";

        if (usuario.get(0).getdireccionActual() == 1){

            mensaje = "\n\n Para llegar a la UVG tome la ruta del 'Mercado Central' y bajese en la parada 'Paseo de la letras' y por ultimo tome la ruta'Fegua'con dirección ";

            switch(ubicacionDestino){
            
            case 1:

                mensaje = "\n\nNo puede ir a la misma ubicacion donde se encuentre";
                break;
                
            case 2:

                mensaje = "\n\n Para llegar a la UVG tome la ruta del 'Mercado Central' y bajese en la parada 'Paseo de la letras' y por ultimo tome la ruta'Fegua'con dirección a zona 16 ";
                break;

            case 3:
                
                mensaje = "\n\nPara llegar a Miraflores tome la ruta del 'Pasaje Aycinena' y bajese en la parada 'Cejusa' ";
                break;
                
            default:
            
                mensaje = "\n\nElija una opcion correcta";
                break;
                
            } 
        }

        else if(usuario.get(0).getdireccionActual() == 2) {

            switch(ubicacionDestino){
            
            case 1:

                mensaje = "\n\nPara llegar al Parque Central tome la ruta 'fegua ' y bajese en la parada 'Paseo de la letras' y por ultimo tome la ruta'Mercado Centra'";
                break;

            case 2:

                mensaje = "\n\nNo puede ir a la misma ubicacion donde se encuentre";
                break;

            case 3:

                mensaje = "\n\nPara llegar al Parque Central tome la ruta 'fegua ' y bajese en la parada 'Paseo de la letras' luego tome la ruta 'Parque Centenario'  y tome la ruta 'Archivo General' y  en la parada 'Cejusa'";
                break;

            default:
            
                mensaje = "\n\nElija una opcion correcta";
                break;
                
            }
        }

        else if(usuario.get(0).getdireccionActual() == 3){

            switch(ubicacionDestino){
            
            case 1:

                mensaje = "\n\nPara llegar al Parque Central tome la ruta 'Cejusa' y bajese en la parada 'Parque Centenario'";
                
                break;

            case 2:

                mensaje = "\n\nPara llegar a la UVG tome la ruta 'Cejusa' y bajese en la parada 'Paseo de la letras' luego tome la ruta 'Parque Centenario' y por ultimo tome la ruta'Fegua'con dirección a zona 16 ";
                break;
            
            case 3:

                mensaje = "\n\nNo puede ir a la misma ubicacion donde se encuentre";
                break;

            default:
            
                mensaje = "\n\nElija una opcion correcta";
                break;
                
            }
        }

        return mensaje;
        
    }

    
}