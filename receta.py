class Receta:

    def __init__(self, n:str, d:int, i:list, e:str, t:str, ti:int):
        '''
        Los elementos que tendrá la receta
        '''
        self.nombre = n
        self.dificultad = d
        self.ingredientes = i
        self.elaboracion = e
        self.tipo = t
        self.tiempo = ti 

    def __str__(self):
        ''' 
        Hacemos una cadena para unir los elementos y que se printean con saltos de linia
        '''
        cadena = "Nombre de la receta: " + self.nombre +'\n'
        cadena += "Nivel de dificultad: " + str(self.dificultad) +'\n'
        #cadena += f"Lista de ingredientes:  {self.ingredientes}" + '\n'
        cadena += f"Lista de ingredientes:  "
        for ingre in self.ingredientes[:-1]:
            cadena += ingre +", "
        cadena += self.ingredientes[-1] +".\n"
        cadena += "Descripción de la preparación: " + self.elaboracion + '\n'
        cadena += "Tipo de receta: " + self.tipo + '\n'
        cadena += "El tiempo de preparación es de: " + str(self.tiempo) + " minutos"
        cadena += "\n-----------------------------------------------------------------"
        
        return cadena


