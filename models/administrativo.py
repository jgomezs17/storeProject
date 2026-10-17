from models.persona import Persona


class Administrativo(Persona):
    """Personal administrativo de la universidad. Hereda nombre, identificacion y correo de Persona."""

    JORNADAS = ["mañana", "tarde", "completa"]

    def __init__(self, nombre, identificacion, correo, numero_empleado, dependencia, cargo, jornada):
        super().__init__(nombre, identificacion, correo)

        # valores vacíos por defecto: si el dato es inválido avisa y queda vacío
        self.__numero_empleado = ""
        self.__dependencia = ""
        self.__cargo = ""
        self.__jornada = ""

        self.SetNumeroEmpleado(numero_empleado)
        self.SetDependencia(dependencia)
        self.SetCargo(cargo)
        self.SetJornada(jornada)

    # ---------- Getters ----------
    def GetNumeroEmpleado(self):
        return self.__numero_empleado

    def GetDependencia(self):
        return self.__dependencia

    def GetCargo(self):
        return self.__cargo

    def GetJornada(self):
        return self.__jornada

    # ---------- Setters con validaciones ----------
    def SetNumeroEmpleado(self, numero_empleado):
        if numero_empleado is None or str(numero_empleado).strip() == "":
            print("Error: el número de empleado no puede estar vacío. No se aplicó el cambio.")
            return
        self.__numero_empleado = str(numero_empleado).strip()

    def SetDependencia(self, dependencia):
        if dependencia is None or str(dependencia).strip() == "":
            print("Error: la dependencia no puede estar vacía. No se aplicó el cambio.")
            return
        self.__dependencia = str(dependencia).strip()

    def SetCargo(self, cargo):
        if cargo is None or str(cargo).strip() == "":
            print("Error: el cargo no puede estar vacío. No se aplicó el cambio.")
            return
        self.__cargo = str(cargo).strip()

    def SetJornada(self, jornada):
        if jornada is None or str(jornada).strip().lower() not in Administrativo.JORNADAS:
            print(f"Error: la jornada debe ser una de {Administrativo.JORNADAS}. No se aplicó el cambio.")
            return
        self.__jornada = str(jornada).strip().lower()

    # ---------- Métodos de la clase ----------
    def ShowInformation(self):
        return (super().ShowInformation() + "\n"
                f"Número de empleado: {self.__numero_empleado}\n"
                f"Dependencia: {self.__dependencia}\n"
                f"Cargo: {self.__cargo}\n"
                f"Jornada: {self.__jornada}")

    def PerformMainActivity(self):
      return f"{self.GetNombre()} trabaja como {self.__cargo} en la dependencia de {self.__dependencia}."
