from Node import Node
from colorama import Fore


class SCList:  # -----> Lista circular simplemente enlazada

    def __init__(self):
        self.ini = None  # -----> Nodo inicial
        self.fin = None  # -----> Nodo final

    def lista_vacia(self):  # -----> Metodo para verificar si la lista esta vacia
        if self.ini is None:  # -----> Si self.ini = None entonces...
            return True  # -----> La lista esta vacia
        else:
            return False  # -----> La lista no esta vacia

    def agregar_ini(self, dato):  # -----> Metodo para agregar al inicio de la lista
        if self.lista_vacia():  # -----> Si lista_vacia() = True entonces...
            self.ini = self.fin = Node(dato)  # -----> ini y fin son objetos de la clase Node
            self.fin.siguiente = self.ini  # -----> El apuntador de fin --> ini
        else:
            nodo_auxiliar = Node(dato)  # -----> nodo_auxiliar es un objeto de la clase Node
            nodo_auxiliar.siguiente = self.ini  # -----> El apuntador de nodo_auxiliar --> ini
            self.ini = nodo_auxiliar  # -----> El nodo_auxiliar se coloca al principio de la lista
            self.fin.siguiente = self.ini  # -----> El apuntador de fin --> ini

    def agregar_fin(self, dato):  # -----> Metodo para agregar al final de la lista
        if self.lista_vacia():
            self.ini = self.fin = Node(dato)
            self.fin.siguiente = self.ini
        else:
            nodo_auxiliar = self.fin
            self.fin = nodo_auxiliar.siguiente = Node(dato)
            self.fin.siguiente = self.ini

    def quitar_ini(self):  # -----> Metodo para quitar al inicio de la lista
        if self.lista_vacia():
            print('                          ')
            print(Fore.RED + '--> Lista vacia')
        elif self.ini == self.fin:
            self.ini = self.fin = None
        else:
            self.ini = self.ini.siguiente
            self.fin.siguiente = self.ini

    def quitar_fin(self):  # -----> Metodo para quitar al final de la lista
        if self.lista_vacia():
            print('                          ')
            print(Fore.RED + '--> Lista vacia')
        elif self.ini == self.fin:
            self.ini = self.fin = None
        else:
            nodo_auxiliar = self.ini
            while nodo_auxiliar.siguiente != self.fin:
                nodo_auxiliar = nodo_auxiliar.siguiente
            nodo_auxiliar.siguiente = self.ini
            self.fin = nodo_auxiliar

    def buscar(self, dato):  # -----> Metodo para hacer una busqueda en la lista
        nodo_auxiliar = self.ini
        while nodo_auxiliar:
            if nodo_auxiliar.dato == dato:
                nodo_auxiliar = nodo_auxiliar.siguiente
                return nodo_auxiliar.dato
            elif nodo_auxiliar.siguiente == self.ini:
                print('                                       ')
                print(Fore.RED + '--> Información no existente')
                break
            else:
                nodo_auxiliar = nodo_auxiliar.siguiente

    def mostrar_contenido(self):  # -----> Metodo para mostrar el contenido de la lista
        nodo_auxiliar = self.ini
        while nodo_auxiliar:
            print(nodo_auxiliar.dato)
            nodo_auxiliar = nodo_auxiliar.siguiente
            if nodo_auxiliar == self.ini:
                break
