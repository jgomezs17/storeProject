# Sistema de Gestión Académica

Proyecto en Python desarrollado para el curso de Programación Orientada a Objetos de la Universidad de Manizales (Facultad de Ciencias e Ingenierías).

**Integrantes:** Jonathan Gómez Salazar y Omar Picón Meza

Este repositorio contiene las dos primeras actividades colaborativas, construidas sobre el mismo proyecto:

- **AC1:** modelado de clases, encapsulamiento, herencia y polimorfismo.
- **AC2 (versión actual):** clase abstracta, composición y excepciones personalizadas.

---

## Descripción

El sistema modela la gestión académica básica de una universidad: programas académicos, asignaturas, personas vinculadas (estudiantes, docentes y administrativos), grupos académicos con su horario, y la matrícula de estudiantes en esos grupos.

## Qué cambió en AC2

| Fase | Cambio |
|---|---|
| 1 | `Persona` pasa a ser una clase **abstracta**. `PerformMainActivity()` es un método abstracto y ya no se puede crear una `Persona` directamente. |
| 2 | Nueva clase `GrupoAcademico`, que recibe objetos `asignaturas` y `Docente`, guarda los `Estudiante` matriculados y permite matricular y retirar estudiantes. |
| 3 | Nueva clase `Horario`, relacionada con `GrupoAcademico` por **composición**. |
| 4 | Cinco **excepciones personalizadas** que se lanzan desde los métodos donde se detecta cada situación y se capturan en `main.py`. |

El polimorfismo de AC1 se conserva sin cambios (ver sección correspondiente).

## Estructura del proyecto

```
storeProject/
├── main.py                        # Archivo principal: ejecuta todas las pruebas
├── README.md
├── controllers/
│   └── registro_academico.py      # Búsqueda de programas y asignaturas por código
├── exceptions/
│   └── excepciones.py             # Las 5 excepciones personalizadas
└── models/
    ├── persona.py                 # Clase abstracta (padre)
    ├── estudiante.py
    ├── docente.py
    ├── administrativo.py
    ├── programa_academico.py
    ├── asignaturas.py
    ├── horario.py
    └── grupo_academico.py
```

## Clases principales

| Clase | Responsabilidad |
|---|---|
| `Persona` (abstracta) | Datos comunes: nombre, identificación y correo. Define el método abstracto `PerformMainActivity()`. |
| `Estudiante` | Hereda de `Persona`. Código estudiantil, programa, semestre y promedio. |
| `Docente` | Hereda de `Persona`. Número de empleado, facultad, tipo de contratación y horas semanales. |
| `Administrativo` | Hereda de `Persona`. Número de empleado, dependencia, cargo y jornada. |
| `Programa_academico` | Datos de un programa de la universidad. |
| `asignaturas` | Asignatura asociada a un objeto `Programa_academico`. |
| `Horario` | Día, hora de inicio, hora de fin y salón. |
| `GrupoAcademico` | Código, asignatura, docente, capacidad máxima, estudiantes matriculados y horario. |
| `RegistroAcademico` | Guarda listas de programas y asignaturas y las busca por código. |

## Persona como clase abstracta

`Persona` hereda de `ABC` y declara `PerformMainActivity()` con `@abstractmethod`. Se hizo abstracta porque en la universidad no existe una "persona" genérica: siempre es un estudiante, un docente o un administrativo. `Persona` solo reúne lo que las tres tienen en común y obliga a cada hija a implementar su propia actividad principal. Si se intenta crear una `Persona` directamente, Python lanza un `TypeError`, que se demuestra en `main.py`.

## Grupo académico y horario: composición, no herencia

`GrupoAcademico` **contiene** un `Horario`: crea su propio objeto `Horario` dentro del constructor, a partir del día, las horas y el salón que recibe. Es una relación de composición ("tiene un") porque el horario no tiene sentido por separado: describe cuándo y dónde se dicta ese grupo, y si el grupo deja de existir, su horario también.

No corresponde a herencia porque un grupo académico **no es un** horario, ni un horario es un grupo. La herencia modela relaciones "es un" (un `Estudiante` es una `Persona`). Si `GrupoAcademico` heredara de `Horario`, el grupo tendría atributos y métodos que no le pertenecen y se confundirían dos conceptos distintos.

Las demás relaciones del grupo son de asociación: recibe objetos `asignaturas` y `Docente` que ya existen por separado, y guarda una lista de objetos `Estudiante`.

## Excepciones personalizadas

Todas heredan de `Exception`, están definidas en `exceptions/excepciones.py` y se capturan con `try/except` en `main.py`, de modo que el programa continúa después de cada error.

| Excepción | Situación que controla | Dónde se lanza |
|---|---|---|
| `EstudianteYaMatriculadoError` | Matricular dos veces al mismo estudiante en un grupo | `GrupoAcademico.Matricular_estudiante()` |
| `GrupoLlenoError` | Matricular cuando el grupo ya alcanzó su capacidad máxima | `GrupoAcademico.Matricular_estudiante()` |
| `EstudianteNoMatriculadoError` | Retirar a un estudiante que no está en el grupo | `GrupoAcademico.Retirar_estudiante()` |
| `AsignaturaNoEncontradaError` | Buscar una asignatura con un código que no existe | `RegistroAcademico.BuscarAsignatura()` |
| `ProgramaNoEncontradoError` | Buscar un programa con un código que no existe | `RegistroAcademico.BuscarPrograma()` |

Las validaciones de los setters (por ejemplo, un correo sin `@` o créditos menores que 1) siguen funcionando como en AC1: informan el error y no aplican el cambio.

## Herencia, sobrescritura y polimorfismo

- **Herencia:** `Estudiante`, `Docente` y `Administrativo` heredan de `Persona` y no repiten nombre, identificación ni correo.
- **Sobrescritura:** las tres clases sobrescriben `ShowInformation()` (agregando sus datos propios con `super()`) e implementan `PerformMainActivity()` con un comportamiento distinto cada una.
- **Polimorfismo:** en `main.py` hay una única lista `personas` con los tres tipos, recorrida con un solo ciclo que llama a `ShowInformation()` y `PerformMainActivity()` sin condicionales por tipo. Sigue funcionando en AC2 porque las clases hijas conservan esos métodos; hacer abstracta a `Persona` solo obliga a implementar `PerformMainActivity()`, que las tres ya implementaban.

## Cómo ejecutar

Requisitos: Python 3.

Desde la carpeta del proyecto:

```
py main.py
```

(o `python main.py`, según el sistema). El archivo `main.py` ejecuta las pruebas de todas las fases y muestra en consola los resultados, incluyendo las excepciones controladas.

## Versiones

- `Entrega_AC1`: versión de la Actividad Colaborativa 1.
- `Entrega_AC2`: versión de la Actividad Colaborativa 2.

## Uso de herramientas de inteligencia artificial

Se utilizó Claude (Anthropic) como apoyo para comprender conceptos (clases abstractas, composición y excepciones), proponer la estructura de las clases nuevas y revisar errores. El código fue probado, adaptado al estilo del proyecto y ejecutado por los integrantes. El detalle de este uso se declara en el Documento de Decisiones de Diseño.
