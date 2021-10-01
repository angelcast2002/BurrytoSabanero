public class Usuario{
    private String nombreUsuario;
    private String contra;
    private int direccionActual;
    
    public Usuario() {
    }

    public Usuario(String nombreUsuario, String clave, int direccionActual){
        this.nombreUsuario = nombreUsuario;
        this.contra = clave;
        this.direccionActual = direccionActual;
    }

    /* Setters y Getters*/
    public void setNombreUsuario(String nombre){
        this.nombreUsuario = nombre;
    }
    public String getNombreUsuario() {
        return nombreUsuario;
    }

    public void setcontra(String contra){
        this.contra = contra;
    }
    public String getcontra() {
        return contra;
    }
    
    public void setdireccionActual(int direccionActual){
        this.direccionActual = direccionActual;
    }
    public int getdireccionActual() {
        return direccionActual;
    }
    
}

   
