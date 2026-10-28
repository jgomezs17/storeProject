# Clase RegistroAcademico
# Guarda las listas de programas y asignaturas y permite buscarlos por código.
# Si el código no existe, lanza una excepción personalizada.

from models.programa_academico import Programa_academico
from models.asignaturas import asignaturas
from exceptions.excepciones import (AsignaturaNoEncontradaError,
                                    ProgramaNoEncontradoError)


class RegistroAcademico:
    def __init__(self):
        self.__programas = []
        self.__asignaturas = []

    def AgregarPrograma(self, programa):
        # tiene que ser un objeto Programa_academico, no un texto suelto
        if not isinstance(programa, Programa_academico):
            print("Error: solo se pueden registrar objetos Programa_academico.")
            return
        self.__programas.append(programa)

    def AgregarAsignatura(self, asignatura):
        # tiene que ser un objeto asignaturas, no un texto suelto
        if not isinstance(asignatura, asignaturas):
            print("Error: solo se pueden registrar objetos asignaturas.")
            return
        self.__asignaturas.append(asignatura)

    def BuscarPrograma(self, codigo):
        for programa in self.__programas:
            if programa.GetCodigo() == codigo:
                return programa
        # si el for termina sin encontrarlo, se lanza la excepción
        raise ProgramaNoEncontradoError(codigo)

    def BuscarAsignatura(self, codigo):
        for asignatura in self.__asignaturas:
            if asignatura.GetCodigo() == codigo:
                return asignatura
        raise AsignaturaNoEncontradaError(codigo)