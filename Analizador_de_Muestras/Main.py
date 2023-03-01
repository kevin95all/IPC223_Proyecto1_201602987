from tkinter import *
from tkinter import filedialog
from colorama import Fore
from XML import XML
#  import os
#  import webbrowser


class Main:

    def __init__(self):
        self.ruta = ''  # -----> Guarda la dirección del archivo XML
        self.op = ''  # -----> Guarda la opción seleccionada del menú
        self.salir = False  # -----> Variable para finalizar el programa
        self.archivo = XML()

    def menu_principal(self):  # -----> Metodo para mostrar el menu principal
        while not self.salir:
            print('                                                       ')
            print(Fore.GREEN + '┌------------ MENU PRINCIPAL ------------┐')
            print(Fore.GREEN + '|                                        |')
            print(Fore.GREEN + '|        1)   Cargar archivo             |')
            print(Fore.GREEN + '|        2)   Seleccionar paciente       |')
            print(Fore.GREEN + '|        3)   Mostrar celula             |')
            print(Fore.GREEN + '|        4)   Analizar paciente          |')
            print(Fore.GREEN + '|        5)   Generar reporte            |')
            print(Fore.GREEN + '|        6)   Salir                      |')
            print(Fore.GREEN + '|                                        |')
            print(Fore.GREEN + '└----------------------------------------┘')
            print('                                                       ')

            self.op = input(Fore.CYAN + '--> Ingrese una opción: ')

            if self.op == '1':
                self.cargar_archivo()
            elif self.op == '2':
                pass
            elif self.op == '3':
                pass
            elif self.op == '4':
                pass
            elif self.op == '5':
                pass
            elif self.op == '6':
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
            print('                                          ')
            print(Fore.GREEN + '--> Archivo cargado con exito')
        ventana.mainloop()

    def finalizar(self):  # -----> Metodo para finalizar el programa
        print('                                  ')
        print(Fore.RED + '--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.salir = True


app = Main()
app.menu_principal()
