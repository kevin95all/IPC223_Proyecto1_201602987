from Graphics import Graphics


class Operations:

    def __init__(self):
        self.muestra = []
        self.codigos = []
        self.nombres = []
        self.imagen = Graphics()

    def analizar(self, muestra, codigos, nombres):
        self.muestra = muestra
        self.codigos = codigos
        self.nombres = nombres

        self.imagen.nueva_grafica(self.muestra, self.codigos, self.nombres)

    def contenido(self):
        return self.muestra
