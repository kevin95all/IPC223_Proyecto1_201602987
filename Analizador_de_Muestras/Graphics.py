from colorama import Fore
import os


class Graphics:

    def __init__(self):
        self.muestra = []  # -----> [codigo, descripción, filas, columnas, celdas[x, y, id]]
        self.codigo = ''
        self.descripcion = ''
        self.filas = 0
        self.columnas = 0
        self.lista_celdas = []
        self.celda = []
        self.codigos = []
        self.nombres = []
        self.xy = []
        self.id = []
        self.contenido = ''

    def graficar(self, muestra, codigos, nombres):
        self.muestra = muestra
        self.codigo = self.muestra[0]
        self.descripcion = self.muestra[1]
        self.filas = self.muestra[2]
        self.columnas = self.muestra[3]
        self.lista_celdas = self.muestra[4]
        self.codigos = codigos
        self.nombres = nombres
        self.contenido = ''

        if int(self.filas) > 10000 or int(self.columnas) > 10000:
            print('                                                           ')
            print(Fore.RED + '--> No se puede graficar, dimenciones no validas')
        elif len(self.codigos) > 1000:
            print('                                                          ')
            print(Fore.RED + '--> No se puede graficar, organismos no validos')
        else:
            for celda in range(len(self.lista_celdas)):
                self.celda = self.lista_celdas[celda]
                fila = self.celda[0]
                columna = self.celda[1]
                cod = self.celda[2]

                self.celda = []
                self.celda.append(fila)
                self.celda.append(columna)
                self.xy.append(self.celda)
                self.id.append(cod)
                self.celda = []

            for fila in range(int(self.filas)):
                self.contenido = self.contenido + '<TR>'
                for columna in range(int(self.columnas)):
                    self.celda.append(str(fila))
                    self.celda.append(str(columna))
                    if self.celda in self.xy:
                        posicion = self.xy.index(self.celda)
                        codigo = self.id[posicion]
                        if self.codigos.index(codigo) == 0:
                            self.contenido = self.contenido + '<TD BGCOLOR="green"></TD>'
                            self.celda = []
                        elif self.codigos.index(codigo) == 1:
                            self.contenido = self.contenido + '<TD BGCOLOR="blue"></TD>'
                            self.celda = []
                        elif self.codigos.index(codigo) == 2:
                            self.contenido = self.contenido + '<TD BGCOLOR="gold"></TD>'
                            self.celda = []
                        elif self.codigos.index(codigo) == 3:
                            self.contenido = self.contenido + '<TD BGCOLOR="red"></TD>'
                            self.celda = []
                        elif self.codigos.index(codigo) == 4:
                            self.contenido = self.contenido + '<TD BGCOLOR="bisque"></TD>'
                            self.celda = []
                        elif self.codigos.index(codigo) == 5:
                            self.contenido = self.contenido + '<TD BGCOLOR="black"></TD>'
                            self.celda = []
                        else:
                            self.contenido = self.contenido + '<TD BGCOLOR="cyan"></TD>'
                            self.celda = []
                    else:
                        self.contenido = self.contenido + '<TD BGCOLOR="white"></TD>'
                        self.celda = []
                self.contenido = self.contenido + '\n'
                self.contenido = self.contenido + '</TR>'
                self.contenido = self.contenido + '\n'

            with open(f'archivos_creados/Muestra.dot', mode='w') as grafo:
                grafo.write('digraph ' + self.codigo + ' {\n')
                grafo.write('abc [shape=none, margin=0, label=<\n')
                grafo.write('<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2" CELLPADDING="7">\n')
                grafo.write(self.contenido)
                grafo.write('</TABLE>>];\n')
                grafo.write('\n')
                grafo.write('detalles [shape=none, margin=0, label=<\n')
                grafo.write('<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2" CELLPADDING="7">\n')
                for nombre in range(len(self.nombres)):
                    dato = self.nombres[nombre]
                    if self.nombres.index(dato) == 0:
                        grafo.write('<TR><TD BGCOLOR="green">' + dato + '</TD></TR>\n')
                    elif self.nombres.index(dato) == 1:
                        grafo.write('<TR><TD BGCOLOR="blue">' + dato + '</TD></TR>\n')
                    elif self.nombres.index(dato) == 2:
                        grafo.write('<TR><TD BGCOLOR="gold">' + dato + '</TD></TR>\n')
                    elif self.nombres.index(dato) == 3:
                        grafo.write('<TR><TD BGCOLOR="red">' + dato + '</TD></TR>\n')
                    elif self.nombres.index(dato) == 4:
                        grafo.write('<TR><TD BGCOLOR="bisque">' + dato + '</TD></TR>\n')
                    elif self.nombres.index(dato) == 5:
                        grafo.write('<TR><TD BGCOLOR="black">' + dato + '</TD></TR>\n')
                    else:
                        grafo.write('<TR><TD BGCOLOR="cyan">' + dato + '</TD></TR>\n')
                grafo.write('</TABLE>>];\n')
                grafo.write('}')
            os.system('dot -Tpdf archivos_creados/Muestra.dot -o archivos_creados/Muestra.pdf')

    def nueva_grafica(self, muestra, codigos, nombres):
        self.muestra = muestra
        self.codigo = self.muestra[0]
        self.descripcion = self.muestra[1]
        self.filas = self.muestra[2]
        self.columnas = self.muestra[3]
        self.lista_celdas = self.muestra[4]
        self.codigos = codigos
        self.nombres = nombres
        self.contenido = ''

        if int(self.filas) > 10000 or int(self.columnas) > 10000:
            print('                                                           ')
            print(Fore.RED + '--> No se puede graficar, dimenciones no validas')
        elif len(self.codigos) > 1000:
            print('                                                          ')
            print(Fore.RED + '--> No se puede graficar, organismos no validos')
        else:
            for celda in range(len(self.lista_celdas)):
                self.celda = self.lista_celdas[celda]
                fila = self.celda[0]
                columna = self.celda[1]
                cod = self.celda[2]

                self.celda = []
                self.celda.append(fila)
                self.celda.append(columna)
                self.xy.append(self.celda)
                self.id.append(cod)
                self.celda = []

            for fila in range(int(self.filas)):
                self.contenido = self.contenido + '<TR>'
                for columna in range(int(self.columnas)):
                    self.celda.append(str(fila))
                    self.celda.append(str(columna))
                    if self.celda in self.xy:
                        posicion = self.xy.index(self.celda)
                        codigo = self.id[posicion]
                        if self.codigos.index(codigo) == 0:
                            self.contenido = self.contenido + '<TD BGCOLOR="green"></TD>'
                            self.celda = []
                        elif self.codigos.index(codigo) == 1:
                            self.contenido = self.contenido + '<TD BGCOLOR="blue"></TD>'
                            self.celda = []
                        elif self.codigos.index(codigo) == 2:
                            self.contenido = self.contenido + '<TD BGCOLOR="gold"></TD>'
                            self.celda = []
                        elif self.codigos.index(codigo) == 3:
                            self.contenido = self.contenido + '<TD BGCOLOR="red"></TD>'
                            self.celda = []
                        elif self.codigos.index(codigo) == 4:
                            self.contenido = self.contenido + '<TD BGCOLOR="bisque"></TD>'
                            self.celda = []
                        elif self.codigos.index(codigo) == 5:
                            self.contenido = self.contenido + '<TD BGCOLOR="black"></TD>'
                            self.celda = []
                        else:
                            self.contenido = self.contenido + '<TD BGCOLOR="cyan"></TD>'
                            self.celda = []
                    else:
                        self.contenido = self.contenido + '<TD BGCOLOR="white"></TD>'
                        self.celda = []
                self.contenido = self.contenido + '\n'
                self.contenido = self.contenido + '</TR>'
                self.contenido = self.contenido + '\n'

            with open(f'archivos_creados/Nueva_Muestra.dot', mode='w') as grafo:
                grafo.write('digraph ' + self.codigo + ' {\n')
                grafo.write('abc [shape=none, margin=0, label=<\n')
                grafo.write('<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2" CELLPADDING="7">\n')
                grafo.write(self.contenido)
                grafo.write('</TABLE>>];\n')
                grafo.write('\n')
                grafo.write('detalles [shape=none, margin=0, label=<\n')
                grafo.write('<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2" CELLPADDING="7">\n')
                for nombre in range(len(self.nombres)):
                    dato = self.nombres[nombre]
                    if self.nombres.index(dato) == 0:
                        grafo.write('<TR><TD BGCOLOR="green">' + dato + '</TD></TR>\n')
                    elif self.nombres.index(dato) == 1:
                        grafo.write('<TR><TD BGCOLOR="blue">' + dato + '</TD></TR>\n')
                    elif self.nombres.index(dato) == 2:
                        grafo.write('<TR><TD BGCOLOR="gold">' + dato + '</TD></TR>\n')
                    elif self.nombres.index(dato) == 3:
                        grafo.write('<TR><TD BGCOLOR="red">' + dato + '</TD></TR>\n')
                    elif self.nombres.index(dato) == 4:
                        grafo.write('<TR><TD BGCOLOR="bisque">' + dato + '</TD></TR>\n')
                    elif self.nombres.index(dato) == 5:
                        grafo.write('<TR><TD BGCOLOR="black">' + dato + '</TD></TR>\n')
                    else:
                        grafo.write('<TR><TD BGCOLOR="cyan">' + dato + '</TD></TR>\n')
                grafo.write('</TABLE>>];\n')
                grafo.write('}')
            os.system('dot -Tpdf archivos_creados/Nueva_Muestra.dot -o archivos_creados/Nueva_Muestra.pdf')
