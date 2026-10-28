# Usar categorías

Las categorías le permiten hacer que grupos de preguntas tengan el mismo aspecto. Por ejemplo, dentro de un mismo quiz podría tener preguntas sobre ciencia, música, cine, etc. Para que todas las preguntas sobre ciencia tengan el mismo aspecto, puede crear una categoría llamada ‘Science’. Para esta categoría puede establecer propiedades como la imagen de fondo, la fuente y los colores. Al crear una nueva pregunta sobre ciencia, puede aplicar la categoría ‘Science’ y toda la pregunta recibirá el formato de la plantilla ‘Science’. Todas las categorías se almacenan dentro de su archivo de quiz actual. Si utiliza con frecuencia las mismas categorías, le aconsejamos crear un archivo de quiz vacío para usarlo como punto de partida de todos sus quizzes. Las categorías también desempeñan un papel importante al importar preguntas directamente desde Excel: como la información de formato avanzado no se puede almacenar en Excel, cada pregunta de Excel puede hacer referencia a una categoría existente de la que se aplicará el formato a la diapositiva recién creada. Para crear una nueva categoría, primero cambie a la vista ‘Category’:

![](../assets/images/image26.webp){ width="407" loading=lazy }

Después active la pestaña INSERT de la cinta de opciones, haga clic en cualquiera de las plantillas e introduzca un nombre para su categoría:

![](../assets/images/image27.webp){ width="220" loading=lazy }

Ahora puede establecer las propiedades de la categoría, como el fondo que se va a utilizar. Para aplicar una categoría, vuelva a la vista normal de diapositivas de quiz, seleccione una o más diapositivas en el panel de miniaturas de la izquierda, active la pestaña DESIGN y elija la categoría en la galería Categories:

![](../assets/images/image28.webp){ width="350" loading=lazy }

Ahora las diapositivas seleccionadas tendrán el formato de la diapositiva de categoría.

## Vídeo de fondo para una categoría

Una categoría también puede tener un [vídeo de fondo](backgrounds.md#video-de-fondo), por ejemplo una animación en bucle con los colores de la ronda ‘Science’. Seleccione la diapositiva de categoría en la vista Category y configúrelo del mismo modo que en una diapositiva normal: haga clic con el botón derecho en su fondo y elija ‘Background video…’, o establezca la propiedad ‘Background video’ en el panel de propiedades, junto con sus ajustes (loop, silent, sync with quiz).

Al aplicar la categoría, cada diapositiva seleccionada recibe el vídeo de fondo con los mismos ajustes. El vídeo se almacena una sola vez en el archivo del quiz, independientemente de cuántas diapositivas lo utilicen. Una imagen o un vídeo en los marcadores de posición de esas diapositivas permanece donde está y se reproduce encima del vídeo de fondo. Si se aplica de nuevo la categoría, u otra categoría con vídeo de fondo, se sustituye el vídeo de fondo de la diapositiva. Después todavía puede cambiar los ajustes del vídeo de fondo diapositiva por diapositiva.

Las preguntas importadas desde Excel que hacen referencia a la categoría también reciben su vídeo de fondo, a menos que la columna BACKGROUND-VIDEO de la pregunta indique un vídeo propio (consulte [Importación y exportación de preguntas](import-and-export-of-questions.md)).
