from tkinter import *
from tkinter import filedialog
from colorama import Fore
from XML import XML
import os
import webbrowser


class Main:

    def __init__(self):
        self.ruta = ''  # -----> Guarda la dirección del archivo XML
        self.op = ''  # -----> Guarda la opción seleccionada del menú
        self.salir = False  # -----> Variable para finalizar el programa
        self.muestra_seleccionada = False  # -----> variable para seleccionar muestra
        self.muestra_analizada = False  # -----> variable para analizar la muestra
        self.archivo = XML()

    def menu_principal(self):  # -----> Metodo para mostrar el menu principal
        while not self.salir:  # -----> Mientras self.salir sea = False...
            print('                                                       ')
            print(Fore.GREEN + '┌------------ MENU PRINCIPAL ------------┐')
            print(Fore.GREEN + '|                                        |')
            print(Fore.GREEN + '|        1)   Cargar archivo             |')
            print(Fore.GREEN + '|        2)   Seleccionar muestra        |')
            print(Fore.GREEN + '|        3)   Graficar muestra           |')
            print(Fore.GREEN + '|        4)   Colocar organismo          |')
            print(Fore.GREEN + '|        5)   Analizar muestra           |')
            print(Fore.GREEN + '|        6)   Generar XML                |')
            print(Fore.GREEN + '|        7)   Finalizar programa         |')
            print(Fore.GREEN + '|                                        |')
            print(Fore.GREEN + '└----------------------------------------┘')
            print('                                                       ')

            self.op = input(Fore.CYAN + '--> Ingrese una opción: ')

            if self.op == '1':
                self.cargar_archivo()
            elif self.op == '2':
                self.seleccionar_muestra()
            elif self.op == '3':
                self.graficar_muestra()
            elif self.op == '4':
                self.colocar_organismo()
            elif self.op == '5':
                self.analizar_muestra()
            elif self.op == '6':
                self.generar_xml()
            elif self.op == '7':
                self.finalizar()
            else:
                print('                               ')
                print(Fore.RED + '--> Opción no valida')

    def cargar_archivo(self):  # -----> Metodo para cargar archivos XML
        ventana = Tk()
        respaldo = self.ruta
        self.ruta = ''

        self.ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos xml', '*.xml'),
                ('Todos los archivos', '*.*')
            ]
        )
        if self.ruta == '':
            self.ruta = respaldo
            print('                                         ')
            print(Fore.RED + '--> No se cargo ningun archivo')
        else:
            self.archivo.leer_xml(self.ruta)
            print('                                         ')
            print(Fore.CYAN + '--> Archivo cargado con exito')
        ventana.mainloop()

    def seleccionar_muestra(self):  # -----> Metodo para seleccionar la muestra
        if self.ruta == '':
            print('                                              ')
            print(Fore.RED + '--> No se ha cargado ningun archivo')
        else:
            self.archivo.mostrar_muestra()
            self.muestra_seleccionada = True

    def graficar_muestra(self):  # -----> Metodo para graficar la muestra
        if self.ruta == '':
            print('                                              ')
            print(Fore.RED + '--> No se ha cargado ningun archivo')
        else:
            if not self.muestra_seleccionada:
                print('                                               ')
                print(Fore.RED + '--> No se ha cargado ninguna muestra')
            else:
                print('                                          ')
                print(Fore.CYAN + '--> Muestra original graficada')

                direccion = 'file:///' + os.getcwd() + '/' + 'archivos_creados/Muestra.pdf'

                webbrowser.open_new(direccion)

    def colocar_organismo(self):  # -----> Metodo para colocar nuevos organismos
        if self.ruta == '':
            print('                                              ')
            print(Fore.RED + '--> No se ha cargado ningun archivo')
        else:
            if not self.muestra_seleccionada:
                print('                                               ')
                print(Fore.RED + '--> No se ha cargado ninguna muestra')
            else:
                self.archivo.insertar_organismo()

    def analizar_muestra(self):  # -----> Metodo para analizar la muestra
        if self.ruta == '':
            print('                                              ')
            print(Fore.RED + '--> No se ha cargado ningun archivo')
        else:
            if not self.muestra_seleccionada:
                print('                                               ')
                print(Fore.RED + '--> No se ha cargado ninguna muestra')
            else:
                print('                                 ')
                print(Fore.CYAN + '--> Muestra analizada')

                direccion = 'file:///' + os.getcwd() + '/' + 'archivos_creados/Nueva_Muestra.pdf'

                webbrowser.open_new(direccion)
                self.muestra_analizada = True

    def generar_xml(self):  # -----> Metodo para generar un archivo XML
        if self.ruta == '':
            print('                                              ')
            print(Fore.RED + '--> No se ha cargado ningun archivo')
        else:
            if not self.muestra_seleccionada:
                print('                                               ')
                print(Fore.RED + '--> No se ha cargado ninguna muestra')
            else:
                if not self.muestra_analizada:
                    print('                                                 ')
                    print(Fore.RED + '--> No se ha analizado ninguna muestra')
                else:
                    self.archivo.generar_xml()
                    print('                                              ')
                    print(Fore.CYAN + '--> Archivo xml generado con exito')

    def finalizar(self):  # -----> Metodo para finalizar el programa
        print('                                  ')
        print(Fore.RED + '--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.muestra_seleccionada = False
        self.muestra_analizada = False
        self.salir = True


app = Main()
app.menu_principal()
