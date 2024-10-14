from receta import Receta
from datetime import datetime

class Libro:
    def __init__(self, n:str):
        '''
        Los elementos que tendrá el libro
        '''
        self.nombre = n
        self.fecha_creacion = datetime.now().strftime("%d/%m/%y  %H:%M:%S.%f")
        self.fecha_actualización =  self.fecha_creacion
        self.recetas = {"entrante":[], "postres":[], "principal": []} 

    def __str__(self):
        '''
        Esta será la información que se mostrará del libro
        '''
        return f"{self.nombre}, {self.fecha_creacion}, {self.fecha_actualización}"
    
    def guarda_receta(self, receta:Receta):
        '''
        lo usaremos para introducir/guardar una receta en el libro, ordenada por TIPO
        '''
        if receta.tipo not in self.recetas:
            print(f"El tipo {receta.tipo} NO existe en este libro")
        else:
            self.recetas[receta.tipo].append(receta)
            self.fecha_actualización = datetime.now().strftime("%d/%m/%y  %H:%M:%S.%f")

    
    def listar(self):
        '''
        Método para listar todas las recetas del libro. No distingue por ningún valor
        '''
        for listareceta in self.recetas.values():
            for receta in listareceta:
                print(receta)
    
    def listar_tipo(self, tipo):
        '''
        Método para listar las recetas del libro por tipo de receta
        '''
        for tiporecetas, listareceta in self.recetas.items():
            if tiporecetas ==  tipo:
                for receta in listareceta:
                    print (receta)
            return
        print(f"No existe la categoria: {tipo}")
                
        

    def buscar_receta(self, nombre):
        '''
        usar para buscar una receta por su nombre
        '''
        for listareceta in self.recetas.values():
            for receta in listareceta:
                if receta.nombre ==  nombre:
                    return receta
        print(f"No se ha encontrado la receta con nombre: {nombre}")

