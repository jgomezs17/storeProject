# Clase Horario
# Representa cuándo y dónde se dicta un grupo. Se crea desde GrupoAcademico (composición).

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin, salon):
        # valores por defecto: si el dato es inválido avisa y queda así
        self.__dia = ""
        self.__hora_inicio = 0
        self.__hora_fin = 0
        self.__salon = ""

        # uso los setters para que pasen por las validaciones
        # la hora fin va antes porque el setter de inicio la compara con fin
        self.SetDia(dia)
        self.SetHora_Fin(hora_fin)
        self.SetHora_Inicio(hora_inicio)
        self.SetSalon(salon)

    # Get y Set de día
    def GetDia(self):
        return self.__dia

    def SetDia(self, dia):
        if dia is None or str(dia).strip() == "":
            print("Error: el día no puede estar vacío. No se aplicó el cambio.")
            return
        self.__dia = str(dia).strip()

    # Get y Set de hora de inicio
    def GetHora_Inicio(self):
        return self.__hora_inicio

    def SetHora_Inicio(self, hora_inicio):
        if not isinstance(hora_inicio, int) or hora_inicio < 0 or hora_inicio > 23:
            print("Error: la hora de inicio debe ser un entero entre 0 y 23. No se aplicó el cambio.")
            return
        if hora_inicio >= self.__hora_fin:
            print("Error: la hora de inicio debe ser menor que la hora de fin. No se aplicó el cambio.")
            return
        self.__hora_inicio = hora_inicio

    # Get y Set de hora de fin
    def GetHora_Fin(self):
        return self.__hora_fin

    def SetHora_Fin(self, hora_fin):
        if not isinstance(hora_fin, int) or hora_fin < 1 or hora_fin > 24:
            print("Error: la hora de fin debe ser un entero entre 1 y 24. No se aplicó el cambio.")
            return
        if hora_fin <= self.__hora_inicio:
            print("Error: la hora de fin debe ser mayor que la hora de inicio. No se aplicó el cambio.")
            return
        self.__hora_fin = hora_fin

    # Get y Set de salón
    def GetSalon(self):
        return self.__salon

    def SetSalon(self, salon):
        if salon is None or str(salon).strip() == "":
            print("Error: el salón no puede estar vacío. No se aplicó el cambio.")
            return
        self.__salon = str(salon).strip()

    def ShowInformation(self):
        return (f"Horario: {self.__dia} de {self.__hora_inicio}:00 a "
                f"{self.__hora_fin}:00 | Salón: {self.__salon}")