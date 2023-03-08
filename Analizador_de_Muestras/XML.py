from xml.dom import minidom
from colorama import Fore
from TDA import SCList
from Graphics import Graphics
from Operations import Operations


class XML:

    def __init__(self):
        self.ruta_xml = ''  # -----> Guarda la dirección del archivo XML
        self.lista_nombres_organismos = SCList()  # -----> Es una lista con todos los organismos
        self.lista_nombres_muestras = SCList()  # -----> Es una lista con todas las muestras
        self.lista_organismos = SCList()  # -----> Es una lista con todos los organismos (posición, organismo)
        self.lista_muestras = SCList()  # -----> Es una lista con todas las muestras (posición, muestra)
        self.muestra = []  # -----> Contiene toda la información de 1 muestra
        self.copia = []  # -----> Contiene la copia de la muestra seleccionada
        self.codigos = []  # -----> Es una lista con todos los codigos
        self.nombres = []  # -----> Es una lista con todos los nombres
        self.lista_celdas = []  # -----> Es una lista con todas las celdas
        self.celda = []  # -----> Contendra la información (x, y, codigo) de 1 celda
        self.nueva_celda = []  # -----> Contiene el valor de las celdas ingresadas
        self.imagen = Graphics()  # -----> Es un objeto encargado de graficar
        self.analisis = Operations()  # -----> Es un objeto encargado de analisar la muestra

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
            self.codigos.append(codigo.firstChild.data)
            self.lista_nombres_organismos.agregar_fin(f'{contador_1}) {nombre.firstChild.data}')
            self.nombres.append(nombre.firstChild.data)
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
        print('                                                 ')
        print(Fore.GREEN + '--> Lista de organismos disponibles:')
        print('                                                 ')
        self.lista_nombres_organismos.mostrar_contenido()
        print('                                                    ')
        posicion = input(Fore.CYAN + '--> Seleccione un organismo: ')
        resultado = self.lista_organismos.buscar(posicion)
        if resultado is not None:
            return resultado

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
            self.imagen.graficar(resultado, self.codigos, self.nombres)
            self.copia = resultado

    def insertar_organismo(self):
        if self.copia is not None:
            nombre = 'Nuevo_' + self.copia[0]
            descripcion = self.copia[1]
            filas = self.copia[2]
            columnas = self.copia[3]
            self.lista_celdas = self.copia[4]
            salir = False

            while not salir:
                print('                                                     ')
                print(Fore.GREEN + '┌--------------------------------------┐')
                print(Fore.GREEN + '|                                      |')
                print(Fore.GREEN + '|        1)   Colocar organismo        |')
                print(Fore.GREEN + '|        2)   Finalizar                |')
                print(Fore.GREEN + '|                                      |')
                print(Fore.GREEN + '└--------------------------------------┘')
                print('                                                     ')

                op = input(Fore.CYAN + '--> Ingrese una opción: ')

                if op == '1':
                    xy = []

                    for celda in range(len(self.lista_celdas)):
                        self.celda = self.lista_celdas[celda]
                        f = self.celda[0]
                        c = self.celda[1]

                        self.celda = []
                        self.celda.append(f)
                        self.celda.append(c)
                        xy.append(self.celda)
                        self.celda = []

                    print('                                                                  ')
                    fila = input(Fore.CYAN + '--> Ingrese la posición "y" de la nueva celda: ')
                    print('                                                                     ')
                    columna = input(Fore.CYAN + '--> Ingrese la posición "x" de la nueva celda: ')

                    self.nueva_celda.append(fila)
                    self.nueva_celda.append(columna)

                    if self.nueva_celda in xy:
                        self.nueva_celda = []
                        print('                                                       ')
                        print(Fore.RED + '--> La celda ingresada ya posee un organismo')
                    else:
                        codigo = self.mostrar_organismo()
                        self.nueva_celda.append(codigo)
                        self.lista_celdas.append(self.nueva_celda)
                        self.nueva_celda = []
                elif op == '2':
                    self.muestra.append(nombre)
                    self.muestra.append(descripcion)
                    self.muestra.append(filas)
                    self.muestra.append(columnas)
                    self.muestra.append(self.lista_celdas)
                    self.analisis.analizar(self.muestra, self.codigos, self.nombres)
                    self.lista_celdas = []
                    self.muestra = []

                    print('                                   ')
                    print(Fore.CYAN + '--> Muestra actualizada')
                    salir = True
                else:
                    print('                               ')
                    print(Fore.RED + '--> Opción no valida')
        else:
            print('                                                           ')
            print(Fore.RED + '--> La muestra no fue seleccionada correctamente')

    def generar_xml(self):
        self.muestra = self.analisis.contenido()
        nombre = self.muestra[0]
        descripcion = self.muestra[1]
        filas = self.muestra[2]
        columnas = self.muestra[3]
        self.lista_celdas = self.muestra[4]

        with open(f'archivos_creados/Salida.xml', mode='w') as xml:
            xml.write('<?xml version="1.0"?>\n')
            xml.write('<datosMarte>\n')
            xml.write('    <listaOrganismos>\n')

            for codigo in range(len(self.codigos)):
                xml.write('        <organismo>\n')
                xml.write('            <codigo>' + str(self.codigos[codigo]) + '</codigo>\n')
                xml.write('            <nombre>' + str(self.nombres[codigo]) + '</nombre>\n')
                xml.write('        </organismo>\n')

            xml.write('    </listaOrganismos>\n')
            xml.write('    <listadoMuestras>\n')
            xml.write('        <muestra>\n')
            xml.write('            <codigo>' + str(nombre) + '</codigo>\n')
            xml.write('            <descripcion>' + str(descripcion) + '</descripcion>\n')
            xml.write('            <filas>' + str(filas) + '</filas>\n')
            xml.write('            <columnas>' + str(columnas) + '</columnas>\n')
            xml.write('            <listadoCeldasVivas>\n')

            for celda in range(len(self.lista_celdas)):
                self.celda = self.lista_celdas[celda]
                xml.write('                <celdaViva>\n')
                xml.write('                    <fila>' + str(self.celda[0]) + '</fila>\n')
                xml.write('                    <columna>' + str(self.celda[1]) + '</columna>\n')
                xml.write('                    <codigoOrganismo>' + str(self.celda[2]) + '</codigoOrganismo>\n')
                xml.write('                </celdaViva>\n')
                self.celda = []

            xml.write('            </listadoCeldasVivas>\n')
            xml.write('        </muestra>\n')
            xml.write('    </listadoMuestras>\n')
            xml.write('</datosMarte>\n')
        self.lista_celdas = []
