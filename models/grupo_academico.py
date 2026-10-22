# Clase GrupoAcademico
# Un grupo de una asignatura: tiene un docente, estudiantes matriculados y su horario.
# El Horario se crea dentro del grupo (composición): si no existe el grupo, no existe el horario.

from models.asignaturas import asignaturas
from models.docente import Docente
from models.estudiante import Estudiante
from models.horario import Horario


class GrupoAcademico:
    def __init__(self, codigo_grupo, asignatura, docente, capacidad_maxima,
                 dia, hora_inicio, hora_fin, salon):
        # valores vacíos por defecto: si el dato es inválido avisa y queda vacío
        self.__codigo_grupo = ""
        self.__asignatura = None
        self.__docente = None
        self.__capacidad_maxima = 0
        self.__estudiantes_matriculados = []

        # uso los setters para que pasen por las validaciones
        self.SetCodigo_Grupo(codigo_grupo)
        self.SetAsignatura(asignatura)
        self.SetDocente(docente)
        self.SetCapacidad_Maxima(capacidad_maxima)

        # composición: el grupo crea su propio horario, no lo recibe ya hecho
        self.__horario = Horario(dia, hora_inicio, hora_fin, salon)

    # ---------- Getters ----------
    def GetCodigo_Grupo(self):
        return self.__codigo_grupo

    def GetAsignatura(self):
        return self.__asignatura

    def GetDocente(self):
        return self.__docente

    def GetCapacidad_Maxima(self):
        return self.__capacidad_maxima

    def GetHorario(self):
        return self.__horario

    # ---------- Setters con validaciones ----------
    def SetCodigo_Grupo(self, codigo_grupo):
        if codigo_grupo is None or str(codigo_grupo).strip() == "":
            print("Error: el código del grupo no puede estar vacío. No se aplicó el cambio.")
            return
        self.__codigo_grupo = str(codigo_grupo).strip()

    def SetAsignatura(self, asignatura):
        # tiene que ser un objeto asignaturas, no un texto suelto
        if not isinstance(asignatura, asignaturas):
            print("Error: la asignatura debe ser un objeto asignaturas. No se aplicó el cambio.")
            return
        self.__asignatura = asignatura

    def SetDocente(self, docente):
        # tiene que ser un objeto Docente, no un texto suelto
        if not isinstance(docente, Docente):
            print("Error: el docente debe ser un objeto Docente. No se aplicó el cambio.")
            return
        self.__docente = docente

    def SetCapacidad_Maxima(self, capacidad_maxima):
        if not isinstance(capacidad_maxima, int) or capacidad_maxima <= 0:
            print("Error: la capacidad máxima debe ser un entero mayor que 0. No se aplicó el cambio.")
            return
        self.__capacidad_maxima = capacidad_maxima

    # ---------- Métodos de la clase ----------
    def Matricular_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            print("Error: solo se pueden matricular objetos Estudiante.")
            return
        # OJO: estos dos if y el de Retirar_estudiante se cambian por excepciones en la Fase 4
        if self.__buscar_estudiante(estudiante.GetCodigoEstudiantil()) is not None:
            print("Error: el estudiante ya está matriculado en este grupo.")
            return
        if len(self.__estudiantes_matriculados) >= self.__capacidad_maxima:
            print("Error: el grupo ya está en su capacidad máxima.")
            return
        self.__estudiantes_matriculados.append(estudiante)
        print(f"Matrícula realizada: {estudiante.GetNombre()} en el grupo {self.__codigo_grupo}.")

    def Retirar_estudiante(self, codigo_estudiantil):
        estudiante = self.__buscar_estudiante(codigo_estudiantil)
        if estudiante is None:
            print("Error: ese estudiante no está matriculado en este grupo.")
            return
        self.__estudiantes_matriculados.remove(estudiante)
        print(f"Retiro realizado: {estudiante.GetNombre()} del grupo {self.__codigo_grupo}.")

    def __buscar_estudiante(self, codigo_estudiantil):
        # busca por código estudiantil y devuelve el objeto, o None si no está
        for estudiante in self.__estudiantes_matriculados:
            if estudiante.GetCodigoEstudiantil() == codigo_estudiantil:
                return estudiante
        return None

    def ShowInformationGrupo(self):
        nombre_asignatura = self.__asignatura.GetNombre() if self.__asignatura is not None else ""
        nombre_docente = self.__docente.GetNombre() if self.__docente is not None else ""
        return (f"Grupo: {self.__codigo_grupo}\n"
                f"Asignatura: {nombre_asignatura}\n"
                f"Docente: {nombre_docente}\n"
                f"Cupos: {len(self.__estudiantes_matriculados)}/{self.__capacidad_maxima}\n"
                f"{self.__horario.ShowInformation()}")

    def ShowInformationEstudiante(self):
        if len(self.__estudiantes_matriculados) == 0:
            return "El grupo no tiene estudiantes matriculados."
        texto = f"Estudiantes del grupo {self.__codigo_grupo}:"
        for estudiante in self.__estudiantes_matriculados:
            texto += "\n" + estudiante.ShowInformation() + "\n"
        return texto