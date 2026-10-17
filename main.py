from models.programa_academico import Programa_academico
from models.asignaturas import asignaturas
from models.persona import Persona
from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo

## ===== Fase 1: programas academicos y asignaturas =====
print("===== Programas academicos y asignaturas =====")
programa1 = Programa_academico("Ingenieria de Sistemas", "ISIS01", "Ciencias e Ingenierias", 10, "virtual")
programa2 = Programa_academico("Ingenieria Industrial", "IIND01", "Ciencias e Ingenierias", 10, "presencial")
print(programa1.ShowInformation())
print(programa2.ShowInformation())

Asignaturas1 = asignaturas("Programacion 1", "600189", 3, programa1)
Asignaturas2 = asignaturas("Estadistica", "600245", 2, programa2)
print(Asignaturas1.ShowInformation())
print(Asignaturas2.ShowInformation())

## ===== Fase 2: validaciones de programa y asignatura =====
print("\n===== Validaciones de Programa y Asignatura =====")
# Valores invalidos: deben informar el error y NO cambiar el dato
programa1.SetNumero_Semestres(0)
programa1.SetNumero_Semestres(-3)
programa1.SetNombre("   ")
Asignaturas1.SetCreditos(0)
Asignaturas1.SetCreditos(-2)
Asignaturas1.SetPrograma_Academico("Ingenieria de Sistemas")   # un texto no es un Programa_academico
print(programa1.ShowInformation())                             # tiene que seguir igual
print(Asignaturas1.ShowInformation())                          # tiene que seguir igual

# Modificaciones validas si se aplican
programa2.SetNumero_Semestres(9)
Asignaturas1.SetCreditos(4)
print(programa2.ShowInformation())
print(Asignaturas1.ShowInformation())

## ===== Probando la clase persona =====
print("\n===== Persona =====")
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

## ===== Probando la clase Estudiante (hereda de Persona) =====
print("\n===== Estudiante valido =====")
estudiante1 = Estudiante("Carlos Ruiz", "1090", "carlos.ruiz@correo.com", "E001", programa1, 2, 4.2)
print(estudiante1.ShowInformation())
print(estudiante1.PerformMainActivity())

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

print("\n===== Estudiante con datos invalidos =====")
estudiante2 = Estudiante("Laura Gomez", "2077", "laura@mal", "", None, -2, 7)
print(estudiante2.ShowInformation())

## ===== Probando las clases Docente y Administrativo =====
print("\n===== Docente valido =====")
docente1 = Docente("Marta Salazar", "3001", "marta.salazar@correo.com", "D001", "Ciencias e Ingenierias", "planta", 40)
print(docente1.ShowInformation())
print(docente1.PerformMainActivity())

print("\n===== Validaciones de Docente =====")
docente1.SetHorasSemanales(60)
docente1.SetTipoContratacion("voluntario")
docente1.SetFacultad("")
print(docente1.ShowInformation())                   # tiene que seguir igual
docente1.SetHorasSemanales(36)                      # dato valido
print(docente1.GetHorasSemanales())

print("\n===== Administrativo valido =====")
admin1 = Administrativo("Jorge Mejia", "4001", "jorge.mejia@correo.com", "A001", "Admisiones", "Auxiliar", "mañana")
print(admin1.ShowInformation())
print(admin1.PerformMainActivity())

print("\n===== Validaciones de Administrativo =====")
admin1.SetJornada("noche")
admin1.SetCargo("")
admin1.SetNumeroEmpleado(None)
print(admin1.ShowInformation())                     # tiene que seguir igual
admin1.SetJornada("tarde")                          # dato valido
print(admin1.GetJornada())

## ===== Fase 5: recorrido polimorfico =====
# Personas que faltan para completar 2 estudiantes, 2 docentes y 2 administrativos
estudiante3 = Estudiante("Sofia Lopez", "1102", "sofia.lopez@correo.com", "E002", programa2, 5, 3.9)
docente2 = Docente("Pedro Castro", "3002", "pedro.castro@correo.com", "D002", "Ciencias e Ingenierias", "catedra", 12)
admin2 = Administrativo("Diana Rios", "4002", "diana.rios@correo.com", "A002", "Biblioteca", "Coordinadora", "completa")

# Una sola coleccion con los tres tipos de persona
personas = [estudiante1, estudiante3, docente1, docente2, admin1, admin2]

print("\n===== Reporte general de personas vinculadas =====")
for persona in personas:
    print(persona.ShowInformation())
    print(persona.PerformMainActivity())
    print("-" * 40)