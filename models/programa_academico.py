# Clase Programa_academico
# Representa un programa de la universidad (ej: Ingenieria de
# Sistemas), con sus datos basicos.

class Programa_academico:
    def __init__(self, nombre, codigo, facultad, numero_semestres, modalidad):
        # valores vacios por defecto: si el dato es invalido avisa y queda vacio
        self._nombre = ""
        self._codigo = ""
        self._facultad = ""
        self._numero_semestres = 0
        self._modalidad = ""

        # uso los setters para que pasen por las validaciones
        self.SetNombre(nombre)
        self.SetCodigo(codigo)
        self.SetFacultad(facultad)
        self.SetNumero_Semestres(numero_semestres)
        self.SetModalidad(modalidad)

    # Get y Set de nombre
    def GetNombre(self):
        return self._nombre

    def SetNombre(self, nombre):
        if nombre is None or str(nombre).strip() == "":
            print("Error: el nombre del programa no puede estar vacio. No se aplico el cambio.")
            return
        self._nombre = str(nombre).strip()

    # Get y Set de codigo
    def GetCodigo(self):
        return self._codigo

    def SetCodigo(self, codigo):
        if codigo is None or str(codigo).strip() == "":
            print("Error: el codigo del programa no puede estar vacio. No se aplico el cambio.")
            return
        self._codigo = str(codigo).strip()

    # Get y Set de facultad
    def GetFacultad(self):
        return self._facultad

    def SetFacultad(self, facultad):
        if facultad is None or str(facultad).strip() == "":
            print("Error: la facultad no puede estar vacia. No se aplico el cambio.")
            return
        self._facultad = str(facultad).strip()

    # Get y Set de numero de semestres
    def GetNumero_Semestres(self):
        return self._numero_semestres

    def SetNumero_Semestres(self, numero_semestres):
        if not isinstance(numero_semestres, int) or numero_semestres <= 0:
            print("Error: el numero de semestres debe ser un entero mayor que 0. No se aplico el cambio.")
            return
        self._numero_semestres = numero_semestres

    # Get y Set de modalidad
    def GetModalidad(self):
        return self._modalidad

    def SetModalidad(self, modalidad):
        if modalidad is None or str(modalidad).strip() == "":
            print("Error: la modalidad no puede estar vacia. No se aplico el cambio.")
            return
        self._modalidad = str(modalidad).strip()

    def ShowInformation(self):
        # texto con todos los datos del programa, para verlo
        # completo en consola de una sola vez
        return (
            f"Codigo: {self._codigo} | "
            f"Nombre: {self._nombre} | "
            f"Facultad: {self._facultad} | "
            f"Semestres: {self._numero_semestres} | "
            f"Modalidad: {self._modalidad}"
        )
    