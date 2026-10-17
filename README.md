Sistema de Gestión Académica

Universidad de Manizales - Facultad de Ciencias e Ingenierías Programación Orientada a Objetos (Python) - Actividad colaborativa N.° 1

Integrantes
Jonathan Gómez Salazar
Omar Picón Meza

De qué trata el proyecto

Es la primera versión de un sistema para una universidad que guarda la información de sus estudiantes, docentes y administrativos, y también la de los programas académicos y las asignaturas.

Todas las personas tienen datos en común (identificación, nombre y correo), pero cada tipo tiene datos propios y hace cosas distintas. Por eso lo fuimos armando por fases sobre un solo proyecto:

Primero las clases básicas: Persona, Programa_academico y asignaturas, cada una con su constructor y un método para mostrar la información.
Después el encapsulamiento. Los atributos se consultan y cambian con getters y setters, y los setters revisan que el dato sea válido (por ejemplo, que el correo tenga @ o que los créditos y semestres sean mayores que 0). Si el dato no sirve, el programa avisa del error y no hace el cambio.
Luego la herencia, con Estudiante, Docente y Administrativo como hijas de Persona.
Después la sobrescritura de ShowInformation() y PerformMainActivity() en cada hija.
Por último el polimorfismo, con una sola lista de personas recorrida con un solo ciclo.

Una aclaración: los métodos los dejamos en inglés, como en el ejemplo de la profesora. ShowInformation() es el mostrar_informacion() de la guía y PerformMainActivity() es el realizar_actividad_principal().

Estructura de archivos
storeProject/
├── main.py                       # programa principal, aquí están las pruebas
└── models/
    ├── persona.py                # clase padre Persona
    ├── estudiante.py             # Estudiante (hereda de Persona)
    ├── docente.py                # Docente (hereda de Persona)
    ├── administrativo.py         # Administrativo (hereda de Persona)
    ├── programa_academico.py     # clase Programa_academico
    └── asignaturas.py            # clase asignaturas (se asocia a un programa)
Cómo ejecutarlo

Se necesita tener Python 3 instalado. Se abre una terminal en la carpeta storeProject y se corre:

py main.py

(En Linux o Mac sería python3 main.py.)

Al ejecutarlo se ve en la consola cómo se crean los objetos, los cambios válidos, los intentos de poner datos inválidos (que salen como errores) y al final el reporte con todas las personas.

Herencia, sobrescritura y polimorfismo

Herencia: Persona guarda lo que tienen en común los tres tipos: identificación, nombre y correo, con sus getters, setters y validaciones. Estudiante, Docente y Administrativo heredan de ella y usan super().__init__() para no repetir esos atributos. Cada una agrega solo lo suyo. El estudiante tiene código estudiantil, programa, semestre y promedio. El docente tiene número de empleado, facultad, tipo de contratación y horas semanales. El administrativo tiene número de empleado, dependencia, cargo y jornada.

Sobrescritura: las tres hijas vuelven a escribir ShowInformation() y PerformMainActivity() con el mismo nombre que tienen en Persona. En ShowInformation() primero se llama al de Persona con super() y después se agregan los datos propios de cada clase. En PerformMainActivity() cada una devuelve algo diferente: el estudiante dice qué programa cursa y en qué semestre está, el docente en qué facultad dicta clases y el administrativo qué cargo tiene y en qué dependencia trabaja.

Polimorfismo: en main.py hay una lista llamada personas con dos estudiantes, dos docentes y dos administrativos. Se recorre con un solo for que llama a ShowInformation() y PerformMainActivity() sin preguntar de qué tipo es cada objeto. Python ejecuta solo la versión que le toca a cada uno, aunque los métodos se llamen igual.

## Uso de inteligencia artificial

Usamos Claude como apoyo durante el trabajo: para entender mejor los conceptos de herencia, sobrescritura y polimorfismo, para proponer cómo organizar las clases y para revisar errores de codigo.