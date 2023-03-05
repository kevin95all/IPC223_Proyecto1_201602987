class Graphics:

    def __init__(self):
        self.muestra = []  # -----> [codigo, descripción, filas, columnas, celdas[x, y, id]]
        self.codigo = ''
        self.descripcion = ''
        self.filas = 0
        self.columnas = 0
        self.lista_celdas = []
        self.celda = []
        self.contenido = ''

    def graficar(self, muestra):
        self.muestra = muestra
        self.codigo = self.muestra[0]
        self.descripcion = self.muestra[1]
        self.filas = self.muestra[2]
        self.columnas = self.muestra[3]
        self.lista_celdas = self.muestra[4]
        self.contenido = ''
