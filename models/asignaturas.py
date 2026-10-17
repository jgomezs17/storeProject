"""
Clase Asignaturas
Fase 1: modelo inicial de una asignatura, asociada a un programa
academico (relacion de asociacion: Asignaturas -> Programa_academico).
Fase 2: los datos se modifican con setters que validan.
"""
from models.programa_academico import Programa_academico


class asignaturas:
    def __init__(self, nombre, codigo, creditos, programa_academico):
        # valores vacios por defecto: si el dato es invalido avisa y queda vacio
        self._nombre = ""
        self._codigo = ""
        self._creditos = 0
        # Se guarda el objeto Programa_academico completo (asociacion),
        # no solo su nombre, para poder consultar cualquiera de sus datos.
        self._programa_academico = None

        self.SetNombre(nombre)
        self.SetCodigo(codigo)
        self.SetCreditos(creditos)
        self.SetPrograma_Academico(programa_academico)

    def GetNombre(self):
        return self._nombre

    def SetNombre(self, nombre):
        if nombre is None or str(nombre).strip() == "":
            print("Error: el nombre de la asignatura no puede estar vacio. No se aplico el cambio.")
            return
        self._nombre = str(nombre).strip()

    def GetCodigo(self):
        return self._codigo

    def SetCodigo(self, codigo):
        if codigo is None or str(codigo).strip() == "":
            print("Error: el codigo de la asignatura no puede estar vacio. No se aplico el cambio.")
            return
        self._codigo = str(codigo).strip()

    def GetCreditos(self):
        return self._creditos

    def SetCreditos(self, creditos):
        if not isinstance(creditos, int) or creditos <= 0:
            print("Error: los creditos deben ser un entero mayor que 0. No se aplico el cambio.")
            return
        self._creditos = creditos

    def GetPrograma_Academico(self):
        return self._programa_academico

    def SetPrograma_Academico(self, programa_academico):
        # tiene que ser un objeto Programa_academico, no un texto suelto
        if not isinstance(programa_academico, Programa_academico):
            print("Error: el programa debe ser un objeto Programa_academico. No se aplico el cambio.")
            return
        self._programa_academico = programa_academico

    def ShowInformation(self):
        """Presenta la informacion de la asignatura."""
        nombre_programa = self._programa_academico.GetNombre() if self._programa_academico is not None else ""
        return (
            f"Codigo: {self._codigo} | "
            f"Nombre: {self._nombre} | "
            f"Creditos: {self._creditos} | "
            f"Programa: {nombre_programa}"
        )