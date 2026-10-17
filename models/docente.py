from models.persona import Persona


class Docente(Persona):
    """Docente de la universidad. Hereda nombre, identificacion y correo de Persona."""

    # tipos de contratación que acepto (se puede ampliar)
    TIPOS_CONTRATACION = ["planta", "catedra", "tiempo completo", "medio tiempo"]

    def __init__(self, nombre, identificacion, correo, numero_empleado, facultad, tipo_contratacion, horas_semanales):
        super().__init__(nombre, identificacion, correo)

        # valores vacíos por defecto: si el dato es inválido avisa y queda vacío
        self.__numero_empleado = ""
        self.__facultad = ""
        self.__tipo_contratacion = ""
        self.__horas_semanales = 0

        self.SetNumeroEmpleado(numero_empleado)
        self.SetFacultad(facultad)
        self.SetTipoContratacion(tipo_contratacion)
        self.SetHorasSemanales(horas_semanales)

    # ---------- Getters ----------
    def GetNumeroEmpleado(self):
        return self.__numero_empleado

    def GetFacultad(self):
        return self.__facultad

    def GetTipoContratacion(self):
        return self.__tipo_contratacion

    def GetHorasSemanales(self):
        return self.__horas_semanales

    # ---------- Setters con validaciones ----------
    def SetNumeroEmpleado(self, numero_empleado):
        if numero_empleado is None or str(numero_empleado).strip() == "":
            print("Error: el número de empleado no puede estar vacío. No se aplicó el cambio.")
            return
        self.__numero_empleado = str(numero_empleado).strip()

    def SetFacultad(self, facultad):
        if facultad is None or str(facultad).strip() == "":
            print("Error: la facultad no puede estar vacía. No se aplicó el cambio.")
            return
        self.__facultad = str(facultad).strip()

    def SetTipoContratacion(self, tipo_contratacion):
        if tipo_contratacion is None or str(tipo_contratacion).strip().lower() not in Docente.TIPOS_CONTRATACION:
            print(f"Error: el tipo de contratación debe ser uno de {Docente.TIPOS_CONTRATACION}. No se aplicó el cambio.")
            return
        self.__tipo_contratacion = str(tipo_contratacion).strip().lower()

    def SetHorasSemanales(self, horas_semanales):
        # 48 horas es el máximo semanal de trabajo en Colombia
        if not isinstance(horas_semanales, (int, float)) or horas_semanales <= 0 or horas_semanales > 48:
            print("Error: las horas semanales deben ser mayores que 0 y máximo 48. No se aplicó el cambio.")
            return
        self.__horas_semanales = horas_semanales

    # ---------- Métodos de la clase ----------
    def ShowInformation(self):
        return (super().ShowInformation() + "\n"
                f"Número de empleado: {self.__numero_empleado}\n"
                f"Facultad: {self.__facultad}\n"
                f"Tipo de contratación: {self.__tipo_contratacion}\n"
                f"Horas semanales: {self.__horas_semanales}")

    def PerformMainActivity(self):
      return f"{self.GetNombre()} orienta clases en la facultad de {self.__facultad}."
