# Excepciones personalizadas del sistema de gestión académica.
# Todas heredan de Exception y guardan un mensaje claro de lo que pasó.


class EstudianteYaMatriculadoError(Exception):
    # Se lanza cuando se intenta matricular dos veces al mismo estudiante en un grupo
    def __init__(self, codigo_estudiantil, codigo_grupo):
        super().__init__(f"El estudiante {codigo_estudiantil} ya está matriculado en el grupo {codigo_grupo}.")


class GrupoLlenoError(Exception):
    # Se lanza cuando el grupo ya alcanzó su capacidad máxima
    def __init__(self, codigo_grupo, capacidad_maxima):
        super().__init__(f"El grupo {codigo_grupo} está lleno (capacidad máxima: {capacidad_maxima}).")


class EstudianteNoMatriculadoError(Exception):
    # Se lanza cuando se intenta retirar a un estudiante que no está en el grupo
    def __init__(self, codigo_estudiantil, codigo_grupo):
        super().__init__(f"El estudiante {codigo_estudiantil} no está matriculado en el grupo {codigo_grupo}.")


class AsignaturaNoEncontradaError(Exception):
    # Se lanza cuando se busca una asignatura que no existe
    def __init__(self, codigo_asignatura):
        super().__init__(f"No se encontró ninguna asignatura con el código {codigo_asignatura}.")


class ProgramaNoEncontradoError(Exception):
    # Se lanza cuando se busca un programa académico que no existe
    def __init__(self, codigo_programa):
        super().__init__(f"No se encontró ningún programa académico con el código {codigo_programa}.")