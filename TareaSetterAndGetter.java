
package openbootcamp;


public class TareaSetterAndGetter {
    
    public static void main (String[] args){
        
    // Crear un objeto persona en el main.
        Persona persona = new Persona();
    
    /*
    Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, 
    por último muéstralas por consola.
    */
        persona.setEdad(40);
        persona.setNombre("Luis");
        persona.setTelefono(123456789);
    
        System.out.println("Mi nombre es: "+persona.getNombre());
        System.out.println("Mi edad es: "+persona.getEdad());
        System.out.println("Mi telefono es: "+persona.getTelefono());
    
        
        
    }
}
//Crear clase Persona.
class Persona{
    
// Crear variables las privadas edad, nombre y telefono de la clase Persona.
    private int edad;
    private String nombre;
    private int telefono;
    
    
//Crear gets y sets de cada propiedad.
    public void setEdad(int edad){
        this.edad=edad;
    }
    public int getEdad(){
        return this.edad;
    }
    public void setNombre(String nombre){
        this.nombre=nombre;
    }
    public String getNombre(){
        return this.nombre;
    }
    public void setTelefono(int telefono){
        this.telefono=telefono;
    }
    public int getTelefono(){
        return this.telefono;
    }
}
