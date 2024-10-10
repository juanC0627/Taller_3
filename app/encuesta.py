class Encuesta:
    def __init__(self, titulo, fechaCreacion):
        self.titulo = titulo
        self.fechaCreacion = fechaCreacion
        self.preguntas = []
        self.grupo = None

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def aplicar_a_grupo(self, grupo):
        self.grupo = grupo
