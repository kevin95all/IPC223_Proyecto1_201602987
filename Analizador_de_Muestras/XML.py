from xml.dom import minidom
from colorama import Fore
from TDA import SCList
from Graphics import Graphics


class XML:

    def __init__(self):
        self.ruta_xml = ''  # -----> Guarda la dirección del archivo XML
        self.lista_nombres_organismos = SCList()  # -----> Es una lista con todos los organismos
        self.lista_nombres_muestras = SCList()  # -----> Es una lista con todas las muestras
        self.lista_organismos = SCList()  # -----> Es una lista con todos los organismos (posición, organismo)
        self.lista_muestras = SCList()  # -----> Es una lista con todas las muestras (posición, muestra)
        self.muestra = []  # -----> Contiene toda la información de 1 muestra
        self.lista_celdas = []  # -----> Es una lista con todas las celdas
        self.celda = []  # -----> Contendra la información (x, y, codigo) de 1 celda
        self.imagen = Graphics()  # -----> Es un objeto encargado de graficar

    def leer_xml(self, ruta):
        contador_1 = 1
        contador_2 = 1
        self.ruta_xml = ruta
        xml = minidom.parse(self.ruta_xml)
        organismos = xml.getElementsByTagName('organismo')
        muestras = xml.getElementsByTagName('muestra')

        for organismo in organismos:
            codigo = organismo.getElementsByTagName('codigo')[0]
            nombre = organismo.getElementsByTagName('nombre')[0]

            self.lista_organismos.agregar_fin(str(contador_1))
            self.lista_organismos.agregar_fin(codigo.firstChild.data)
            self.lista_nombres_organismos.agregar_fin(f'{contador_1}) {nombre.firstChild.data}')
            contador_1 = contador_1 + 1

        for muestra in muestras:
            nombre = muestra.getElementsByTagName('codigo')[0]
            descripcion = muestra.getElementsByTagName('descripcion')[0]
            filas = muestra.getElementsByTagName('filas')[0]
            columnas = muestra.getElementsByTagName('columnas')[0]
            lista_celdas = muestra.getElementsByTagName('celdaViva')

            self.lista_nombres_muestras.agregar_fin(f'{contador_2}) {nombre.firstChild.data}')
            self.muestra.append(nombre.firstChild.data)
            self.muestra.append(descripcion.firstChild.data)
            self.muestra.append(filas.firstChild.data)
            self.muestra.append(columnas.firstChild.data)

            for celda in lista_celdas:
                fila = celda.getElementsByTagName('fila')[0]
                columna = celda.getElementsByTagName('columna')[0]
                codigo = celda.getElementsByTagName('codigoOrganismo')[0]

                self.celda.append(fila.firstChild.data)
                self.celda.append(columna.firstChild.data)
                self.celda.append(codigo.firstChild.data)
                self.lista_celdas.append(self.celda)
                self.celda = []

            self.muestra.append(self.lista_celdas)
            self.lista_celdas = []
            self.lista_muestras.agregar_fin(str(contador_2))
            self.lista_muestras.agregar_fin(self.muestra)
            self.muestra = []
            contador_2 = contador_2 + 1

    def mostrar_organismo(self):
        pass

    def mostrar_muestra(self):
        print('                                               ')
        print(Fore.GREEN + '--> Lista de muestras disponibles:')
        print('                                               ')
        self.lista_nombres_muestras.mostrar_contenido()
        print('                                                   ')
        posicion = input(Fore.CYAN + '--> Seleccione una muestra: ')
        resultado = self.lista_muestras.buscar(posicion)
        if resultado is not None:
            print('       ')
            print(resultado)
            self.imagen.graficar(resultado)
