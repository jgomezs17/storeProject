from models.programa_academico import Programa_academico
from models.asignaturas import asignaturas
from models.persona import Persona

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