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
        cadena = "Nombre       = " + self.nombre +'\n'
        cadena += "Tipo         = " + self.tipo + '\n'
        cadena += "Dificultad   = " + str(self.dificultad) +'\n'
        cadena += "Tiempo       = " + str(self.tiempo) + " minutos" + '\n'
        cadena += "Elaboración  = " + self.elaboracion + '\n'
        cadena += f"Ingredientes =  "
        for ingre in self.ingredientes[:-1]:
            cadena += ingre +", "
        cadena += self.ingredientes[-1] +".\n"
                
        return cadena
 


