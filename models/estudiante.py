from models.persona import Persona
from models.programa_academico import Programa_academico


class Estudiante(Persona):
    """Estudiante de la universidad. Hereda nombre, identificacion y correo de Persona."""

    def __init__(self, nombre, identificacion, correo, codigo_estudiantil, programa, semestre, promedio):
        # lo común lo guarda Persona
        super().__init__(nombre, identificacion, correo)

        # valores vacíos por defecto, igual que en Persona: si el dato es inválido avisa y queda vacío
        self.__codigo_estudiantil = ""
        self.__programa = None
        self.__semestre = 0
        self.__promedio = 0.0

        # uso los setters para que pasen por las validaciones
        self.SetCodigoEstudiantil(codigo_estudiantil)
        self.SetPrograma(programa)
        self.SetSemestre(semestre)
        self.SetPromedio(promedio)

    # ---------- Getters ----------
    def GetCodigoEstudiantil(self):
        return self.__codigo_estudiantil

    def GetPrograma(self):
        return self.__programa

    def GetSemestre(self):
        return self.__semestre

    def GetPromedio(self):
        return self.__promedio

    # ---------- Setters con validaciones ----------
    def SetCodigoEstudiantil(self, codigo_estudiantil):
        if codigo_estudiantil is None or str(codigo_estudiantil).strip() == "":
            print("Error: el código estudiantil no puede estar vacío. No se aplicó el cambio.")
            return
        self.__codigo_estudiantil = str(codigo_estudiantil).strip()

    def SetPrograma(self, programa):
        # el programa tiene que ser un objeto Programa_academico, no un texto suelto
        if not isinstance(programa, Programa_academico):
            print("Error: el programa debe ser un objeto Programa_academico. No se aplicó el cambio.")
            return
        self.__programa = programa

    def SetSemestre(self, semestre):
        if not isinstance(semestre, int) or semestre <= 0:
            print("Error: el semestre debe ser un número entero mayor que 0. No se aplicó el cambio.")
            return
        self.__semestre = semestre

    def SetPromedio(self, promedio):
        # en Colombia la nota va de 0.0 a 5.0
        if not isinstance(promedio, (int, float)) or promedio < 0 or promedio > 5:
            print("Error: el promedio debe estar entre 0.0 y 5.0. No se aplicó el cambio.")
            return
        self.__promedio = float(promedio)

    # ---------- Métodos de la clase ----------
    def ShowInformation(self):
        nombre_programa = self.__programa.GetNombre() if self.__programa is not None else ""
        return (super().ShowInformation() + "\n"
                f"Código estudiantil: {self.__codigo_estudiantil}\n"
                f"Programa: {nombre_programa}\n"
                f"Semestre: {self.__semestre}\n"
                f"Promedio: {self.__promedio}")

    def PerformMainActivity(self):
       nombre_programa = self.__programa.GetNombre() if self.__programa is not None else "ningún programa"
       return f"{self.GetNombre()} cursa {nombre_programa} y está en el semestre {self.__semestre}."
    