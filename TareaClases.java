
package openbootcamp;


public class TareaClases {
    
    public static void main (String[] args){
        Cliente cliente = new Cliente();
        System.out.println(cliente.edad=41);
        System.out.println(cliente.nombre="Luis");
        System.out.println(cliente.telefono=876537465);
    }
    
    
    
    
}

class Persona {
    int edad;
    String nombre;
    int telefono;
}

class Cliente extends Persona {
    private int credito;
    
}

class Trabajadora extends Persona {
    private double salario;
}
