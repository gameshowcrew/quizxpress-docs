# Question

Este tipo indica una pregunta de quiz normal. Son posibles las siguientes variantes:

- *Everyone Answers (también denominado votación):* permite que todos los jugadores respondan a una pregunta.

- *Lock-out (también denominado dedo más rápido)*: el jugador que pulse primero un pulsador puede responder a la pregunta.

- *Pregunta de opción múltiple*: pregunta con varias respuestas entre las que los jugadores pueden elegir. El sistema juzga automáticamente las respuestas dadas (es decir, si 'Judge question' está establecido en 'Automatically'). Puede crear una pregunta de opción múltiple yendo a la pestaña DESIGN y cambiando el diseño a uno con varias respuestas.

- *Pregunta abierta (sin opciones múltiples)*: pregunta que un jugador o equipo responde verbalmente y que después juzga el presentador del quiz (con su mando de presentador, el teclado o QuizXpress Director). Puede crear una pregunta abierta yendo al menú DESIGN y cambiando el diseño a uno sin respuestas. En la sección 'input mode', seleccione 'default' como modo de entrada.

- Tipos de entrada ampliados, que incluyen preguntas con respuestas numéricas, de texto completo o de primera letra. Estas preguntas pueden responderse con la aplicación QuizXpress Smart Buzzer o mediante el sitio web buzzerpad. Puede crear una pregunta abierta con una respuesta de número, letra o texto seleccionando 'number', 'letter' o 'text' como modo de entrada.

En la sección de puntos, puede indicar el número de puntos que se ganan por una respuesta correcta, el número de puntos que se pierden por una respuesta incorrecta y el número de puntos que se pierden cuando no se da ninguna respuesta. También puede hacer que los puntos disminuyan a medida que el reloj cuenta atrás durante una pregunta. Para ello, introduzca el número de puntos 'At start' y 'At end'. Puede hacer lo mismo con los puntos de penalización (*Wrong answer* y *No answer*).

![](../../assets/images/image30.webp){ width="222" loading=lazy }

Con estas opciones puede recompensar con más puntos a los jugadores que responden con rapidez. Al mismo tiempo, las respuestas incorrectas pueden penalizarse más al principio de una pregunta para evitar que la gente adivine o apueste al azar nada más empezar la cuenta atrás.

En una pregunta de opción múltiple puede establecer puntos de bonificación por velocidad para los tres jugadores más rápidos en responder correctamente a la pregunta. El resultado es una pregunta de tipo 'todos pueden responder' con un elemento de 'dedo más rápido'. Para acceder al ajuste de los puntos de bonificación, haga clic en el botón 'Speed Bonus' de la sección Points, tras lo cual se abre el siguiente formulario:

![](../../assets/images/image31.webp){ width="201" loading=lazy }

Asigne un valor superior a cero a cada entrada (si solo desea premiar al jugador más rápido, rellene únicamente los puntos del primero en responder). Durante el quiz, aparecerá en pantalla un indicador animado de puntos de bonificación una vez terminada la pregunta para destacar a los jugadores que han ganado los puntos de bonificación.

También se reproducirá el jingle del ganador del primer puesto de los puntos de bonificación (para obtener más información sobre los jingles, consulte [Configuración de los sonidos: la página de la pestaña Sounds](../../setup/configuring-sounds-the-sounds-tab-page.md))

![](../../assets/images/image32.webp){ width="275" loading=lazy }

## Preguntas de opción múltiple

Al crear una pregunta de opción múltiple, puede indicar en QuizXpress Studio cuál de las respuestas es la correcta. Si lo hace, QuizXpress puede juzgar si las respuestas dadas por los equipos son correctas al jugar un quiz. Puede indicar cuál es la respuesta correcta seleccionando primero una de las respuestas con el ratón y marcando después la casilla situada antes de 'Correct Answer' en el panel Properties. También puede utilizar el menú contextual: seleccione primero la respuesta, haga clic con el botón derecho y elija 'Set correct answer'. Además, puede establecer las respuestas correctas de las preguntas de opción múltiple en la representación 'Table Mode' de las preguntas (haga clic en la pestaña VIEW y después en 'Table Mode'). En la última columna de la cuadrícula puede indicar la respuesta correcta de las preguntas de opción múltiple (de respuesta única).

## Varias respuestas correctas

QuizXpress admite tener varias respuestas correctas. Están disponibles las siguientes opciones:

### Una sola correcta

Este es el modo predeterminado, en el que hay una única respuesta correcta para una pregunta de opción múltiple.

### Varias correctas (una respuesta)

En este modo la pregunta puede tener varias respuestas correctas, pero los jugadores solo pueden elegir una de ellas. Para cada respuesta puede establecer una corrección diferente, si procede. Puede utilizarlo para crear preguntas en las que los jugadores ganan más puntos si están 'más cerca' de la respuesta correcta, como se ilustra en la pregunta siguiente (2000 es la respuesta exacta):

![](../../assets/images/image33.webp){ width="449" loading=lazy }

La 'correctness' de una respuesta se establece haciendo clic con el botón derecho en la respuesta y seleccionando 'Set Correctness' en el menú contextual. El siguiente cuadro de diálogo le ayuda a establecer el valor de corrección:

![](../../assets/images/image34.webp){ width="311" loading=lazy }

También puede utilizarlo para crear preguntas al estilo 'Family Feud' como la siguiente. Si asigna a las respuestas la corrección equivalente a los porcentajes de las respuestas de Family Feud, elegir una respuesta más popular otorgará más puntos al jugador. Si establece los puntos de la pregunta en 100, el número de puntos que un jugador puede ganar por dar una determinada respuesta es el porcentaje correspondiente.

![](../../assets/images/image35.webp){ loading=lazy }

### Varias correctas (varias respuestas)

En este modo, la pregunta también puede tener varias respuestas correctas, cada una con una 'correctness' diferente, pero ahora los jugadores pueden seleccionar más de una respuesta. Así, por ejemplo, cuando las respuestas A y C están ambas establecidas como correctas (cada una con un 50 % de corrección), los jugadores pueden obtener el 100 % de los puntos respondiendo a la pregunta con *ambas*, A y C. Si respondieran con A y B, obtendrían solo el 50 % de los puntos.

Si los jugadores deben responder con todas las respuestas correctas para ganar puntos, seleccione la pregunta y, en el panel de propiedades, establezca el 'response mode' en 'multiple responses, exact match'.

### Ordenada

En este modo, el jugador debe colocar las respuestas en el orden correcto. Puede crear preguntas como la que se muestra a continuación (la respuesta correcta sería C->A->D->B).

Si desea que los jugadores den el orden exacto para ganar puntos, seleccione la pregunta y, en el panel de propiedades, establezca el 'ordered answer mode' en 'exact match' (que es el valor predeterminado). Si dar un orden parcialmente correcto también debe permitir ganar puntos, establezca el 'ordered answer mode' en 'partial match'. En este caso, el porcentaje de respuestas dadas en la posición correcta dará lugar al mismo porcentaje de los puntos que se pueden ganar en la pregunta. Por ejemplo, si el orden correcto es ABCD y un jugador responde ACBD, obtendrá el 50 % de los puntos que se pueden ganar en la pregunta.

![](../../assets/images/image36.webp){ loading=lazy }

Para cambiar el orden, haga clic con el botón derecho en una de las respuestas ordenadas y haga clic en 'Set Order':![](../../assets/images/image37.webp){ width="284" loading=lazy }

## Preguntas numéricas, de texto completo y de primera letra

QuizXpress admite tres tipos de entrada que pueden utilizarse con la aplicación Smart Buzzer o el sitio web buzzerpad: numérica, de texto completo y de primera letra. Puede utilizar estos tipos de entrada en combinación con una pregunta abierta. Las opciones son las siguientes:

![](../../assets/images/image38.webp){ width="286" loading=lazy }

Elegir *Default* en una pregunta abierta da como resultado una pregunta normal de dedo más rápido que se puede jugar con pulsadores o mandos. Al utilizar la aplicación Smart Buzzer o el sitio web buzzerpad, se mostrará un pulsador en pantalla. La persona que pulse primero bloquea los pulsadores de todos los demás jugadores y responde verbalmente al presentador del quiz.

### Entrada numérica

|     |
|-----|

![](../../assets/images/image39.webp){ width="126" loading=lazy }Para el tipo de entrada *Number*, la aplicación Smart Buzzer o el sitio web buzzerpad presenta a los jugadores una pantalla en la que pueden introducir un valor numérico.

En las preguntas numéricas, también puede especificar un intervalo como '80-90'. Esto significa que todas las respuestas entre 80 y 90 (ambos inclusive) se juzgan como correctas. O bien puede convertir la pregunta en una pregunta de aproximación (por ejemplo, '¿cuántas canicas hay en el tarro?') en la que solo el jugador con la respuesta más cercana a la correcta obtiene puntos. En este caso, marque la casilla situada antes de 'Nearest wins'. Cuando hay varios ganadores, los jugadores que dieron la respuesta más rápido ganan los puntos.

En las preguntas numéricas de tipo nearest-wins, un número arbitrario de jugadores puede ganar puntos. El número de ganadores se configura en la cuadrícula de propiedades cambiando el campo 'Nearest Wins'.

![](../../assets/images/image40.webp){ width="413" loading=lazy }

En este caso, los 3 primeros jugadores más cercanos a la respuesta correcta ganan puntos.

### Entrada de texto completo

El tipo *Full-Text* permite a los jugadores introducir texto libre (sin distinguir mayúsculas de minúsculas; las mayúsculas no importan).

En las preguntas de texto completo, puede indicar si desea una coincidencia exacta con las respuestas dadas, o bien puede utilizar la coincidencia aproximada y establecer una tolerancia que admita pequeños errores ortográficos. Si desea admitir varias respuestas, puede introducir varios textos en el campo 'correct answer' separados por un punto y coma (por ejemplo, 'Belgium;Belgique;Belgie'). Utilice la opción Test para comprobar que la tolerancia de las respuestas de texto con 'fuzzy match' funciona correctamente.

#### Preguntas de texto completo con varias respuestas

Las preguntas de texto también pueden tener varias respuestas. Por ejemplo, puede reproducir una canción y preguntar por el artista y el título. Cada respuesta correcta aportará el 50 % de los puntos. Supongamos que reproduce una canción de Madonna llamada Holiday y quiere que los jugadores respondan tanto el artista como el título:

1)  Cree una pregunta de texto estándar con la respuesta correcta: Madonna ![](../../assets/images/image41.webp){ width="602" loading=lazy }

2)  Vaya a las propiedades avanzadas de la diapositiva y busque 'Full-text answers'.

3)  Haga clic en los tres puntos \[…\] para abrir el editor Full-text answer y añada el título de la canción 'Holiday'. Si es necesario, también puede establecer la coincidencia aproximada para cada respuesta o introducir variantes de respuesta para cada respuesta correcta separadas por un punto y coma:

Cuando se presenta la pregunta, el jugador ve la siguiente pantalla:

![](../../assets/images/image42.webp){ width="335" loading=lazy }

De forma predeterminada, el jugador ve tantos campos de entrada como respuestas correctas se hayan definido, pero también puede limitar el número de entradas con el ajuste 'Full-text response limit':

![](../../assets/images/image43.webp){ width="377" loading=lazy }

Así, por ejemplo, podría preguntar 'Nombre 4 países que hacen frontera con Alemania', establecer el Full-text response limit en 4 e introducir los 9 países fronterizos como respuestas correctas.

### Entrada de letra

Para el tipo *Letter*, se presenta una cuadrícula A-Z para que los jugadores elijan una letra.

Las preguntas con tipo de respuesta letra muestran en el teléfono una cuadrícula con todas las letras del alfabeto. Los jugadores eligen la primera letra de lo que creen que es la respuesta. Al final de la pregunta, el pulsador muestra si la respuesta fue correcta o incorrecta, junto con la respuesta correcta completa.

En las preguntas de primera letra también puede mostrar la cuadrícula de letras en el pulsador móvil mezclada (una vez o cada 2 segundos) como reto adicional para los jugadores. El ajuste está disponible en el panel de propiedades avanzadas de la diapositiva:

![](../../assets/images/image44.webp){ width="231" loading=lazy }

Cuando esta opción se establece en *Shuffle* o *Moving*, la cuadrícula del pulsador tiene una disposición aleatoria:

![](../../assets/images/image45.webp){ width="187" loading=lazy }

## Preguntas de emparejamiento
