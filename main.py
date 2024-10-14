from receta import Receta
from libro import Libro



Recetario = Libro("Recetario")

for i in  range(100000):
    pass


primera_receta = Receta("Tortilla de patatas", 3, ["huevo", "patata", "cebolla"], "Pelar las patatas. Cortar las patatas y las cebollas. Freír todo en abundante aceite. Batir los huevos. Escurrir las patatas y las cebollas y mezclarlo con el huevo. A continuación, verter la mezcla a la sartén y cocinar por ambos lados", "entrante", 45)
segunda_receta = Receta("Croquetas de jamón", 4, ["mantequilla", "leche", "harina", "jamón serrano", "aceite de girasol", "pan rallado"], "Fundir la mantequilla. Hacer un roux junto la harina y posteriormente agregar la leche lentamente y remover hasta ligar la masa. A continuación añadir el jamón cortado en dados. Verter la masas en recipiente y dejar reposar minimo 6 horas. Transcurrido este tiempo, formar las piezas con forma de croqueta y rebozar con huevo y pan rallado. Finalmente freír en abundante aceite", "entrante", 480)
tercera_receta = Receta("Canapé", 2, ["mini tostadas", "aguacate", "queso untable", "salmón ahumado"], "Untar las mini tostadas con el queso untado. Después Ponemos un trocito de salmón ahumado y encima un poquito de aguacate, cortado al gusto.", "entrante", 30)
cuarta_receta = Receta("Bikini", 2, ["pan de molde", "mantequilla", "queso", "jamón dulce"], "Untar dos rebanadas de pan de molde con mantequilla. A continuación, ponemos una loncha de queso y dos de jamón dulce. Cerramos el sandwich y lo ponemos en la sandwichera o en la sartén hasta que se tueste.", "principal", 20)
quinta_receta = Receta("Bikini trufado", 2, ["pan de molde", "mantequilla", "queso", "jamón serrano", "trufa"], "Untar dos rebanadas de pan de molde con mantequilla. A continuación, ponemos una loncha de queso y dos de jamón serrano. Añadimos también crema de trufa. Cerramos el sandwich y lo ponemos en la sandwichera o en la sartén hasta que se tueste.", "principal", 20)
sexta_receta = Receta("Bikini mallorquín", 2, ["pan de molde", "mantequilla", "queso", "sobrasada"], "Untar dos rebanadas de pan de molde con mantequilla. A continuación, ponemos una loncha de queso y dos de jamón dulce. Cerramos el sandwich y lo ponemos en la sandwichera o en la sartén hasta que se tueste.", "principal", 20)
septima_receta = Receta("Pastel de queso", 3, ["galletas", "mantequilla", "crema de queso", "huevos", "harina", "azúcar"], "Primero hacemos la base de la tarta. Para ello fundimos la mantequilla y la mezclamos con las galletas previamente trituradas. Después mezclamos el resto de ingredientes y lo batimos con las barillas hasta que esten todos integrados. Verter esta mezcla en la base de galletas. Hornar 30 minutos en el horno y dejar enfríar antes de servir.", "postres", 60)
octava_receta = Receta("Musico", 1, ["moscatell", "almendras", "nueces", "avellanas", "pasas"], "Servir el moscatell en una copa pequeña o un vasito de chupito. En un plato pequeño pondremos el resto de ingredientes. Servir conjuntamente.", "postres", 5)
novena_receta = Receta("Vino", 1, ["vino tinto"], "Verter parte del contenido de la botella en una copa", "bebida", 2)

Recetario.guarda_receta(novena_receta)

Recetario.guarda_receta(primera_receta)
Recetario.guarda_receta(segunda_receta)
Recetario.guarda_receta(tercera_receta)
Recetario.guarda_receta(cuarta_receta)
Recetario.guarda_receta(quinta_receta)
Recetario.guarda_receta(sexta_receta)
Recetario.guarda_receta(septima_receta)
Recetario.guarda_receta(octava_receta)

# Recetario.listar()


# print(Recetario.buscar_receta("Bikino"))

# print(Recetario)

print(Recetario.listar_tipo("entrante"))


