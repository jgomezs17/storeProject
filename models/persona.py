def validar_texto_no_vacio(valor, campo):
    # Revisa que el dato no venga vacío; si está bien, lo devuelve sin espacios de sobra
    if valor is None or not str(valor).strip():
        raise ValueError(f"El {campo} no puede estar vacío.")
    return str(valor).strip()
 
 
class Persona:
    # Clase padre de Docente, Estudiante y Administrativo.
    # Aquí van los datos que tienen en común las tres.
 
    def __init__(self, nombre, identificacion, correo):
        # Uso los setters para que las validaciones también se apliquen al crear el objeto
        self._nombre = ""
        self._identificacion = ""
        self._correo = ""
        self.SetNombre(nombre)
        self.SetIdentificacion(identificacion)
        self.SetCorreo(correo)
 
    # ---------- Getters y setters ----------
    # Si el dato no es válido se informa y no se aplica el cambio
 
    def GetIdentificacion(self):
        return self._identificacion
 
    def SetIdentificacion(self, identificacion):
        try:
            self._identificacion = validar_texto_no_vacio(identificacion, "identificacion")
        except ValueError as error:
            print(f"Error: {error} No se cambió.")
 
    def GetNombre(self):
        return self._nombre
 
    def SetNombre(self, nombre):
        try:
            self._nombre = validar_texto_no_vacio(nombre, "nombre")
        except ValueError as error:
            print(f"Error: {error} No se cambió.")
 
    def GetCorreo(self):
        return self._correo
 
    def SetCorreo(self, correo):
        try:
            correo = validar_texto_no_vacio(correo, "correo electronico")
            # El correo debe tener un @ y no puede estar ni al principio ni al final
            if "@" not in correo or correo.startswith("@") or correo.endswith("@"):
                raise ValueError(f"El correo '{correo}' no es válido.")
            self._correo = correo
        except ValueError as error:
            print(f"Error: {error} No se cambió.")
 
    # ---------- Métodos de la clase ----------
 
    def ShowInformation(self):
        # Las hijas lo sobrescriben y le agregan sus propios datos
        return (f"Identificacion: {self._identificacion} | "
                f"Nombre: {self._nombre} | Correo: {self._correo}")
 
    def PerformMainActivity(self):
        # Las hijas lo sobrescriben con lo que hace cada una
        return f"{self._nombre} es una persona vinculada a la universidad."
 
    def __str__(self):
        return self.ShowInformation()
 
 
if __name__ == "__main__":
    # Prueba rápida de la clase
    p = Persona("Ana Torres", "123", "ana@correo.com")
    print(p)
    print(p.PerformMainActivity())
 
    # Datos inválidos: se informa y no se cambian
    p.SetCorreo("correo-sin-arroba")
    p.SetNombre("   ")
    print(p)