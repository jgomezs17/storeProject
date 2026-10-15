from models.programa_academico import Programa_academico
from models.asignaturas import asignaturas
from models.persona import Persona
from models.estudiante import Estudiante
 
programa1 = Programa_academico("Ingenieria de Sistemas", "ISIS01", "Ciencias e Ingenierias", 10, "virtual")
print(programa1.ShowInformation())
 
Asignaturas1 = asignaturas("Programacion 1", "600189", "3", programa1)
 
print(Asignaturas1.ShowInformation())
 
## Probando la clase persona
persona1 = Persona("Ana Torres", "1053", "ana.torres@correo.com")
print(persona1.ShowInformation())
print(persona1.PerformMainActivity())
 
# Pruebas de validacion: deben informar el error y NO cambiar el dato
persona1.SetCorreo("correo-sin-arroba")
persona1.SetNombre("   ")
persona1.SetIdentificacion("")
print(persona1.ShowInformation())
 
# Un dato valido si se aplica
persona1.SetNombre("Ana Maria Torres")
print(persona1)
 
# Persona creada con un dato invalido: avisa y deja ese campo vacio
persona2 = Persona("Luis Perez", "2045", "@mal.com")
print(persona2.ShowInformation())
 
## Probando la clase Estudiante (hereda de Persona)
print("\n===== Estudiante valido =====")
estudiante1 = Estudiante("Carlos Ruiz", "1090", "carlos.ruiz@correo.com", "E001", programa1, 2, 4.2)
print(estudiante1.ShowInformation())
print(estudiante1.PerformMainActivity())
 
# Pruebas de validacion: deben informar el error y NO cambiar el dato
print("\n===== Validaciones de Estudiante =====")
estudiante1.SetSemestre(0)
estudiante1.SetSemestre("tres")
estudiante1.SetPromedio(6.5)
estudiante1.SetPromedio(-1)
estudiante1.SetCodigoEstudiantil("")
estudiante1.SetPrograma("Ingenieria de Sistemas")   # un texto no es un Programa_academico
print(estudiante1.ShowInformation())                # tiene que seguir igual
 
# Datos validos si se aplican
estudiante1.SetSemestre(3)
estudiante1.SetPromedio(4.5)
estudiante1.SetNombre("Carlos Andres Ruiz")         # este viene de Persona
print(estudiante1)
 
# Estudiante creado con datos invalidos: avisa y deja esos campos vacios
print("\n===== Estudiante con datos invalidos =====")
estudiante2 = Estudiante("Laura Gomez", "2077", "laura@mal", "", None, -2, 7)
print(estudiante2.ShowInformation())
 