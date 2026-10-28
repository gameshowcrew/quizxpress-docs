# Ronda Trivia Board

Una ronda Trivia Board le permite crear un tablero de preguntas al estilo Jeopardy® con temas y preguntas de distinta dificultad/puntuación.

![](../../assets/images/image68.webp){ width="513" loading=lazy }

Al igual que las diapositivas de quiz normales, un trivia board puede personalizarse por completo en su estilo (consulte la sección [Trivia Board properties](../user-interface-overview/advanced-properties-grid.md#propiedades-de-trivia-board) para obtener más detalles sobre las opciones).

Durante el programa del quiz, las preguntas del tablero pueden elegirse (con el teclado, con el ratón o con el mando del presentador) o seleccionarse al azar, en cuyo caso un selector aleatorio salta por la pantalla y elige una de las casillas.

## ¿Cómo se crea un Trivia Board?

Para crear un trivia board, comience insertando una diapositiva de trivia board en el quiz (vaya al menú INSERT, haga clic en la lista desplegable de la sección Quiz Slides y elija el diseño Trivia Board). El trivia board se generará automáticamente a partir de las preguntas que lo siguen.

Para clasificar las preguntas por temas y puntos (o solo por temas), asegúrese de establecer las siguientes propiedades en las preguntas que siguen al trivia board:

- El tema

- Los puntos

Puede introducir ambos en la pestaña QUESTION mientras la pregunta está seleccionada:

![](../../assets/images/image69.webp){ width="604" loading=lazy }

Como alternativa, también puede introducir las propiedades en el panel de propiedades (si no está visible, muéstrelo primero seleccionando la pestaña VIEW y marcando la casilla situada antes de 'Properties').

Un Trivia Board puede combinarse con otros formatos de juego de QuizXpress. Para crear un Trivia Board (ronda), QuizXpress necesita saber dónde termina una ronda Trivia Board. Una ronda Trivia Board termina en uno de los siguientes tipos de diapositiva:

- una diapositiva 'End of round' (consulte también 3.4.3)

- otra diapositiva Trivia Board

- una diapositiva Trivia Ladder

- el final del quiz (última ronda o un juego solo de Trivia Board)

Durante el programa del quiz, todas las diapositivas de una ronda Trivia Board se procesan y se agrupan por tema. Dentro de un tema, las preguntas se agrupan por número de puntos. De este modo, detrás de cada casilla de puntos del tablero puede haber varias preguntas. Cuando se agotan las preguntas de una casilla determinada del tablero, la casilla se muestra en gris y ya no se puede elegir.

Las preguntas que no tienen puntos (por ejemplo, Audience response, Demographic, Wager) se ignoran al crear el Trivia Board.

Como alternativa, ¡el Quiz Wizard puede ayudarle a crear una ronda Trivia Board completa con unos pocos clics! Inicie el asistente (pestaña HOME y después 'Quiz Wizard') y seleccione 'create a new round' y después 'a Trivia Board round'. A continuación, rellene los temas, los puntos y otras preferencias.

![](../../assets/images/image70.webp){ width="499" loading=lazy }

Elija el tiempo de pregunta, los puntos y el estilo que se utilizarán en las páginas siguientes y pulse 'Finish' para que se creen el tablero, las preguntas y la diapositiva de fin de ronda de cierre. Por supuesto, aún tendrá que rellenar las preguntas propiamente dichas, pero el tema y los puntos correctos ya estarán establecidos.

## Vista previa de un Trivia Board

La diapositiva Trivia Board de QuizXpress Studio muestra el tablero tal como se verá durante el programa: los temas y los valores de puntos reales de la ronda, dispuestos con sus ajustes de diseño (posición, espaciado, imágenes y texto). Mediante las opciones de estilo del Trivia Board, así como el fondo, puede determinar el aspecto del tablero.

![Una diapositiva Trivia Board diseñada en Studio](../../assets/images/trivia-board-studio-slide.webp){ loading=lazy }

Si desea probar el tablero tal como se jugará durante el programa de concursos, pulse F5 y el tablero se generará automáticamente a partir de las preguntas presentes en la ronda Trivia Board.

## Diseñar su propio tablero

Además del clásico tablero azul, puede dar a un Trivia Board un diseño completamente propio: un fondo temático, encabezados de tema ilustrados y casillas propias. Algunos ejemplos:

![Un tablero de música con casillas de neón y encabezados de tema ilustrados](../../assets/images/trivia-board-custom-music.webp){ loading=lazy }

![Un tablero de deportes con un título en el fondo y encabezados con fotos](../../assets/images/trivia-board-custom-sports.webp){ loading=lazy }

![Un tablero de viajes sobre un mapa ilustrado con etiquetas de tema de colores](../../assets/images/trivia-board-custom-world.webp){ loading=lazy }

Un diseño como estos se compone de unas pocas imágenes:

- **Un fondo** para la diapositiva (1920 × 1080 para un quiz 16:9), con todo lo que no cambia durante el juego: el escenario, un título, un marco alrededor del tablero.
- **Una imagen por tema** para las casillas de tema, por ejemplo una ilustración con el nombre del tema, como en los ejemplos anteriores.
- **Una imagen de casilla** para las casillas de puntos, por ejemplo un botón o una pincelada. Guárdela como PNG con esquinas transparentes, para que el fondo se vea alrededor de la casilla.

Todos los ajustes de diseño se encuentran en la página 'Design' del panel de propiedades cuando el tablero está seleccionado. Todas las imágenes se almacenan dentro del archivo del quiz, por lo que no es necesario copiarlas junto con el quiz.

![Las propiedades de diseño del tablero de música](../../assets/images/trivia-board-properties-custom.webp){ width="380" loading=lazy }

El tablero de música anterior, por ejemplo, tiene una posición personalizada, una altura de la fila de temas del 390 % para los encabezados altos, una imagen de tema sobre toda la casilla para cada tema con el nombre del tema desactivado (las imágenes ya lo contienen), un fondo de casilla de tema transparente y una imagen de casilla para las casillas de puntos.

### Posición del tablero

'Board position' decide dónde aparece el tablero:

- **Automatic** llena la pantalla, como el tablero clásico. Las casillas utilizan entonces un color de relleno en lugar de imágenes.
- **Custom** coloca el tablero donde esté en la diapositiva. Arrastre y cambie el tamaño del tablero en Studio para ajustarlo al marco de su fondo. Los ajustes de imagen que figuran más abajo solo están disponibles con una posición personalizada.

En 'Layout' también puede establecer:

- **Topic row height**: la altura de las casillas de tema en comparación con las casillas de puntos (por ejemplo, 250 % para encabezados ilustrados grandes).
- **Column spacing** y **Row spacing**: el espacio entre las casillas.

### Imágenes de casilla

- **Tile image** (en 'Topic tiles' y en 'Question tiles') sustituye el color de relleno de las casillas por una imagen.
- **Image scaling** decide cómo se ajusta la imagen a una casilla: 'Stretch' (llena la casilla exactamente), 'Fit' (mantiene la forma de la imagen), 'Fill' (mantiene la forma y recorta lo que no cabe) o 'Keep corners' (estira el centro de la imagen y mantiene sus esquinas tal cual, útil para casillas con marco).
- **Vary tiles** refleja la imagen de la casilla de puntos de forma distinta en cada casilla, de modo que una casilla con, por ejemplo, salpicaduras de pintura no tenga exactamente el mismo aspecto en todas partes.

### Imágenes de tema

Haga clic en el botón situado junto a 'Topic images' para dar a cada tema de la ronda su propia imagen. El cuadro de diálogo enumera los temas de las preguntas que siguen al tablero:

![El cuadro de diálogo Topic images](../../assets/images/trivia-board-topic-images-dialog.webp){ width="600" loading=lazy }


- Haga clic en 'Choose…' para elegir una imagen para un tema, o arrastre un archivo de imagen sobre su fila.
- 'Assign from files…' asigna varias imágenes de una sola vez: cada imagen se asigna al tema que tenga el mismo nombre que el archivo. Las mayúsculas y minúsculas, los acentos, los espacios, los guiones y los guiones bajos no importan, por lo que `dutch-pop.png` se asigna al tema 'Dutch Pop'.
- Las imágenes de temas que ya no están en la ronda aparecen al final de la lista, para que pueda eliminarlas.

'Image position' coloca la imagen del tema sobre toda la casilla, o a la izquierda, a la derecha o encima del nombre del tema. Cuando sus imágenes ya contienen el nombre del tema (como los ejemplos anteriores), desactive 'Show topic name'.

!!! tip
    Las imágenes de tema pertenecen a un tema por su nombre. Cuando cambie el nombre de un tema en las preguntas, vuelva a elegir su imagen.

### Texto de las casillas

![Las secciones Tile text y Tile states del panel de propiedades](../../assets/images/trivia-board-properties-tile-text.webp){ width="380" loading=lazy }

- **Same text size for all tiles**: cuando está activado, todos los nombres de tema tienen el mismo tamaño de texto y todos los valores de puntos tienen el mismo tamaño de texto: el tamaño más grande con el que todos los textos caben en su casilla, pero nunca mayor que el tamaño de fuente que haya establecido. Los nombres de tema largos se reparten en dos líneas. Cuando está desactivado, cada texto se hace tan grande como permite su propia casilla, de modo que los textos cortos resultan más grandes que los largos.
- **Text effect** añade una sombra o un contorno alrededor del texto de las casillas, en el 'Effect color'.

### Casillas seleccionadas y jugadas

- **Selection highlight** decide cómo muestra la selección aleatoria la casilla elegida: 'Fill' cubre la casilla con el color de resaltado (el aspecto clásico), 'Tint' la colorea parcialmente, 'Outline' y 'Glow' dibujan un borde de color y mantienen visible la imagen de su casilla.
- **Highlight color** establece el color de la selección aleatoria.
- **Played tiles** decide el aspecto de una casilla una vez que se han jugado sus preguntas: 'Dimmed', 'Hidden' o 'No text' (la casilla permanece, sin su valor de puntos).

### Vídeo de fondo

Una diapositiva Trivia Board también puede tener un [vídeo de fondo](../backgrounds.md#video-de-fondo). Se reproduce detrás del tablero con los propios ajustes del vídeo (bucle, silencio, volumen) y se pausa mientras se muestra una pregunta.

!!! note
    Las versiones anteriores de QuizXpress aún pueden abrir un quiz con un tablero diseñado, pero lo muestran como un tablero clásico.
