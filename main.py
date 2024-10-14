from receta import Receta
from libro import Libro



Recetas_abuela = Libro("Recetas mamá")

for i in  range(100000):
    pass


receta_1 = Receta("Ensalada", 1, ["lechuga", "tomate", "aceite", "sal"], "lavar cortar sazonar", "entrante", 10)
receta_2 = Receta("Arroz", 2, ["Aceite", "ajo", "sal", "arroz", "agua"], "sofreír ajo y arroz. Agrega agua ", "principal", 10)
receta_3 = Receta("Arroz con leche", 3, ["Arroz", "Leche"], "poner arroz a cocer en leche hasta que esta se reduzca ", "postre", 10)
receta_4 = Receta("Sopa", 1, ["zanahoria", "nabo", "agua" , "sal"], "lavar cortar sazonar", "entrante", 10)
receta_5 = Receta("pollo horno", 5, ["pollo", "Patata", "Cebolla"], "lavar cortar sazonar", "principal", 10)
receta_6 = Receta("Macedonia primavera", 2, ["Naranja", "fresa", "melocotón"], "lavar cortar sazonar", "postre", 10)
receta_7 = Receta("Ensalada2", 1, ["lechuga", "tomate", "aceite", "sal"], "lavar cortar sazonar", "entrante", -10)
receta_8 = Receta("Arroz2", 8, ["Aceite", "ajo", "sal", "arroz", "agua"], " sofreír ajo y arroz. Agrega agua ", "principal", 10)
receta_9 = Receta("Arroz con leche", -2, ["Arroz", "Leche"], "poner arroz a cocer en leche hasta que esta se reduzca ", "postre", 10)
receta_10 = Receta("Sopa sosa", 1, ["zanahoria", "nabo", "agua" , "sal"], "lavar cortar sazonar", "entrante", 10)
receta_11 = Receta("pavo horno", 5, ["pavo", "Patata", "Cebolla"], "lavar cortar sazonar", "principal", 10)
receta_12 = Receta("Macedonia otoño", 2, ["Naranja", "Manzana", "Pera"], "lavar cortar sazonar", "postre", 10)



Recetas_abuela.guarda_receta(receta_1)
Recetas_abuela.guarda_receta(receta_2)
Recetas_abuela.guarda_receta(receta_3)
Recetas_abuela.guarda_receta(receta_4)
Recetas_abuela.guarda_receta(receta_5)
Recetas_abuela.guarda_receta(receta_6)
Recetas_abuela.guarda_receta(receta_7)
Recetas_abuela.guarda_receta(receta_8)
Recetas_abuela.guarda_receta(receta_9)
Recetas_abuela.guarda_receta(receta_10)
Recetas_abuela.guarda_receta(receta_11)
Recetas_abuela.guarda_receta(receta_12)


Recetas_abuela.listar()
print(Recetas_abuela.busca_receta("Macedonia primavera"))
print(Recetas_abuela)
print(Recetas_abuela.lista_recetas_por_tipo("postre"))








