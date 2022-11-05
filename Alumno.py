class Alumno:
    _nombre = None
    _nota = None
    


    def enter_name(self):
        self._nombre = input("Introduce tu nombre: ")
        return self._nombre
    
    def enter_score(self):
        self._nota = int(input("introduce tu nota: "))
        return self._nota

    def resultado (self):
        if self._nota > 6:
            return(f"El alumno {self._nombre} ha aprobado con la nota {self._nota}")
        else:
            return ("Vuelve en Septiembre")



alumnos = Alumno()
alumnos.enter_name()
alumnos.enter_score()
print(alumnos.resultado())