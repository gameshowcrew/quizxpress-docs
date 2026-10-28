# Ronda de Bingo

Este tipo de diapositiva inicia una partida normal de Number Bingo, Emoji Bingo, Music Bingo o Trivia Bingo. Actualmente, este tipo de juego solo se puede jugar cuando el público utiliza la app Smart Buzzer para dispositivos móviles.

![](../../assets/images/image99.webp){ width="518" loading=lazy }

Al seleccionar el elemento de bolas de Bingo en la diapositiva, aparece la pestaña contextual Bingo en la cinta de opciones y puede configurar los distintos aspectos de su nueva partida de bingo como se describe en la sección [Propiedades de Bingo](../user-interface-overview/advanced-properties-grid.md#propiedades-de-bingo).

QuizXpress admite los siguientes juegos de Bingo:

| ![](../../assets/images/image100.webp){ width="257" loading=lazy } | ![](../../assets/images/image101.webp){ width="259" loading=lazy } |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../../assets/images/image102.webp){ width="257" loading=lazy }                                                                                       | ![](../../assets/images/image103.webp){ width="259" loading=lazy }                                                                                       |

## Crear una partida de Bingo

Puede crear una nueva ronda de bingo con el Quiz Wizard o insertando manualmente una diapositiva de bingo desde el selector Quiz Slides de la pestaña INSERT de la cinta de opciones.

![](../../assets/images/image104.webp){ width="604" loading=lazy }

Para una partida tradicional de Number Bingo o Emoji Bingo, solo necesita crear esa única diapositiva. Basta con hacer clic en las bolas de Bingo y seleccionar después ‘Regular Bingo’ o ‘Emoji Bingo’.

![](../../assets/images/image105.webp){ width="190" loading=lazy }

Para una ronda de Trivia Bingo, sin embargo, también tendrá que crear las preguntas cuya respuesta (que puede ser un texto o una imagen) aparecerá en las celdas del cartón de bingo. Las preguntas deben insertarse después de la diapositiva de Bingo, y debe terminar la ronda con una diapositiva de *fin de ronda*. Como cada cartón tiene 24 celdas que rellenar, necesita al menos 24 preguntas. Crear más preguntas dará como resultado cartones más aleatorios. Por ejemplo, si solo tiene 24 preguntas, todos los cartones tendrán ‘Coverall’ en la última pregunta y todo el mundo tendrá Bingo. Si crea más preguntas, como en el bingo normal, no todas las respuestas estarán en los cartones.

Los tipos de preguntas admitidos en una ronda de Trivia Bingo son las preguntas de número, texto, letra y las preguntas abiertas con una sola imagen (lo que dará como resultado una celda de bingo con imagen).

Para crear celdas de texto en su cartón de bingo, utilice la plantilla de diapositiva ‘open question’:

![](../../assets/images/image106.webp){ loading=lazy }

Y establezca el Input mode en Number, Letter o Text:

![](../../assets/images/image107.webp){ loading=lazy }

Esto dará como resultado una celda de bingo con la respuesta correcta establecida para la pregunta. Usar ‘Number’ o ‘Text’ no supone mucha diferencia, pero al usar el tipo ‘Letter’, solo aparecerá la primera letra en el cartón de bingo.

Para crear una celda de cartón de bingo con *imagen*, elija el siguiente diseño:

![](../../assets/images/image108.webp){ loading=lazy }

Seleccione el elemento de imagen y marque la opción ‘Hidden’ en la sección ‘Adjust’ de la cinta de opciones.

![](../../assets/images/image109.webp){ width="298" loading=lazy }

Esto ocultará la imagen al presentar el quiz al público y aparecerá en el cartón de bingo como una celda de imagen (puede elegir mostrar también la imagen en la pantalla grande durante un quiz, ¡pero esto hará que la respuesta sea muy fácil de encontrar en el cartón de bingo!).

![](../../assets/images/image110.webp){ loading=lazy }

El Quiz Wizard también ayuda a crear rápidamente una ronda de Trivia Bingo o Music Bingo. Basta con iniciar el Quiz Wizard (pestaña HOME, botón Quiz Wizard) y pulsar ‘create a new round’ seguido de ‘a Bingo round’. Ahora puede elegir entre los cuatro tipos de Bingo e indicar sus preferencias.

Cuando haya terminado de crear sus preguntas, puede previsualizar un cartón (aleatorio) haciendo clic con el botón derecho en la diapositiva de bingo y seleccionando Preview (o pulsando F5).

A continuación puede ver un ejemplo de vista previa de un cartón de Trivia Bingo:

![](../../assets/images/image111.webp){ loading=lazy }

Al ejecutar su quiz, en cuanto se presenta la diapositiva de Bingo, el sistema crea un conjunto de cartones aleatorios y los distribuye automáticamente entre sus jugadores.

Para Trivia Bingo hay una opción (en la pestaña BINGO de la cinta de opciones) para aleatorizar las diapositivas de la ronda de Bingo de modo que aparezcan en un orden distinto cada vez que juegue el quiz:

![](../../assets/images/image112.webp){ width="158" loading=lazy }

Es posible personalizar la imagen que se muestra en el centro de los cartones de Bingo en la app móvil y usar su propia imagen. Para ello, seleccione el elemento Bingo de la diapositiva de Bingo, abra el panel de propiedades avanzadas (pestaña VIEW, marque ‘Properties’), haga clic en la propiedad ‘Center image’ y haga clic en el botón de los tres puntos para seleccionar un archivo de imagen:

![](../../assets/images/image113.webp){ loading=lazy }

¡Utilice su propia imagen central para promocionar su marca entre los jugadores!

### Patrones de Bingo admitidos

![](../../assets/images/image114.webp){ width="146" loading=lazy }

Puede definir hasta cinco patrones sucesivos que conducirán a Bingo. Puede seleccionar tres patrones haciendo clic en los botones ‘Pattern’ de la sección First pattern, Second pattern y Third pattern de la pestaña BINGO de la cinta de opciones. Si desea definir un cuarto y un quinto patrón, puede hacerlo en el panel Properties.

Se puede elegir entre 13 patrones predefinidos. También existe la posibilidad de definir patrones personalizados.

Al abrir los patrones, se muestra una animación para los patrones cuando procede (por ejemplo, el patrón de línea horizontal es válido para cada línea horizontal).

Al jugar una partida de Bingo, tanto en el reproductor del quiz como en el teléfono móvil se mostrará una animación con el patrón actual que da Bingo.

Con la versión 7.1 llega la posibilidad de crear sus propios patrones de bingo. Para ello, elija el patrón personalizado en la cinta de opciones (la última entrada del selector de patrones), tras lo cual verá el editor de patrones:

| ![](../../assets/images/image115.webp){ width="203" loading=lazy } | ![](../../assets/images/image116.webp){ width="205" loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Variación de patrón 1                                                           | Variación de patrón 2                                                           |

Al hacer clic en las celdas, usted crea el patrón. Un patrón puede tener varias variaciones que dan lugar a un bingo válido (de forma análoga a un Bingo de línea horizontal, por ejemplo, donde cada línea horizontal da como resultado un Bingo). En el reproductor del quiz, así como en la app móvil, las variaciones se mostrarán a los jugadores en una animación.

### Espacios en blanco por fila

Para activar los espacios en blanco, abra la vista de propiedades en Studio (VIEW->Properties en la cinta de opciones), seleccione la diapositiva de Bingo y busque la propiedad llamada Blanks per row:

![](../../assets/images/image117.webp){ width="605" loading=lazy }

Este valor indica el número de celdas en blanco por fila de su cartón. Puede ser un valor entre 0 y 4. Al especificar un valor de 2, el cartón de Bingo en el dispositivo móvil tendrá este aspecto:

![](../../assets/images/image118.webp){ width="128" loading=lazy }

Las celdas vacías actúan como comodines al evaluar una reclamación de Bingo. Así, en el cartón de ejemplo de la izquierda, con solo marcar 30, 50 y 67, el jugador podría reclamar un Bingo de línea horizontal. Al jugar con espacios en blanco, conviene considerar qué patrones jugar. Por ejemplo, jugar a una línea vertical podría no ser buena idea, ya que podría haber columnas con una sola celda que marcar. Además, patrones más complejos, como una forma de diamante, podrían no ser alcanzables nunca con ciertos cartones.

### Opciones avanzadas

*Auto advance after claim* – cuando esta opción está activada, el juego continúa automáticamente tras una reclamación de Bingo. Cuando no está activada, el juego espera a que el presentador avance.

*Virtual caller* – cuando está activada, el ordenador dirá en voz alta los números jugados (con el sintetizador de voz predeterminado de Windows).

**Usar una voz personalizada para el cantor de Bingo**

Al activar la opción Virtual Caller, por defecto se utiliza el sintetizador de voz de Windows para decir los números. Sin embargo, puede crear sus propios archivos de voz, por ejemplo con la ayuda de una celebridad local. Para ello, cree una subcarpeta llamada ‘bingo’ en la carpeta de datos de aplicación de QuizXpress (en el Explorador de Windows, introduzca *%appdata%\quizxpress* en la barra de navegación). En esta carpeta, cree los archivos mp3 de cada número que se vaya a decir (p. ej., 1.mp3, 2.mp3, 3.mp3, etc.) y, opcionalmente, un archivo llamado ‘welcome.mp3’ que se reproducirá cuando comience la partida de Bingo. El sistema reproducirá estos archivos cuando se extraiga una bola nueva.

### Modo de falso Bingo

![](../../assets/images/image119.webp){ width="604" loading=lazy }

Puede indicar qué debe ocurrir cuando se hace una reclamación de Bingo falsa. Las opciones son:

- Continue playing – el jugador que hizo una reclamación falsa puede reclamar otro bingo para el mismo patrón.

- Exclude for patterns – el jugador que hizo una reclamación falsa ya no puede reclamar bingo para el mismo patrón. El jugador debe esperar hasta que otra persona tenga un bingo válido y el sistema pase al siguiente patrón.

- Exclude for round – el jugador que hizo una reclamación falsa ya no puede reclamar bingo durante el resto de la ronda (que puede ser una partida completa si solo hay una ronda de Bingo).

En el panel de propiedades hay disponibles dos ajustes adicionales para las reclamaciones de Bingo falsas:

False Bingo limit – establece un límite al número de reclamaciones de Bingo falsas de un jugador. Una vez alcanzado el límite, el jugador queda bloqueado en el juego.

False Bingo handling – determina cómo se gestionan las reclamaciones de Bingo falsas, On-Screen o Silent. En el modo silent, solo se muestran en el reproductor del quiz las reclamaciones de Bingo que darán como resultado un Bingo válido.

### Gestión de reclamaciones

Hay dos opciones para gestionar una reclamación de Bingo:

![](../../assets/images/image120.webp){ width="605" loading=lazy }

Fastest: solo se gestionará al primer jugador que reclame un Bingo; las demás personas que pulsen Bingo también quedarán bloqueadas. Cuando es un Bingo válido, se jugará el siguiente patrón. Todos los jugadores juegan ahora por el nuevo patrón.

Multiple: se gestionan todas las reclamaciones realizadas en los pocos segundos posteriores a que el primer jugador reclamara Bingo. Si hubo una reclamación de Bingo válida, el patrón cambia al siguiente patrón una vez gestionadas todas las reclamaciones.

### Restricciones al guardar un quiz

Existen algunas restricciones al crear una ronda de Bingo. Por ejemplo, es importante que no haya celdas duplicadas en el cartón. El sistema tiene un verificador de reglas integrado que comprueba el quiz antes de guardarlo:

![](../../assets/images/image121.webp){ width="475" loading=lazy }

Lo hace automáticamente para las preguntas de texto. Para las celdas de imagen tendrá que hacerlo usted mismo; asegúrese de no incluir dos preguntas con la misma imagen.

## Jugar una partida de Bingo

El reproductor del quiz se encarga de registrar los cartones de Bingo de todos los jugadores y de escuchar las reclamaciones de Bingo que llegan de los jugadores. A continuación encontrará ejemplos de los distintos juegos de Bingo.

### Tipos de juegos de Bingo

![](../../assets/images/image122.webp){ width="424" loading=lazy }**Number Bingo**

La pantalla mostrará las últimas 9 bolas jugadas junto con su color (que indica la sección del cartón de Bingo), así como la última bola extraída. Muestra cuántas bolas quedan por extraer y el patrón actual que conduce a un Bingo.

![](../../assets/images/image123.webp){ width="423" loading=lazy }**Emoji Bingo**

Emoji Bingo es básicamente igual que Number Bingo, solo que en lugar de 75 números se utilizan los 75 emojis más usados.

![](../../assets/images/image124.webp){ width="422" loading=lazy }**Trivia Bingo**

Al jugar Trivia Bingo, las preguntas se muestran en la pantalla grande junto con el patrón actual y el reloj de cuenta atrás. La respuesta, ya sea un texto o una imagen, debe encontrarse en el cartón (si hay más preguntas que números en el cartón, puede ocurrir que la respuesta \*no\* esté en un cartón).

**Music Bingo**

Music Bingo (o incluso Video Bingo) es básicamente igual que Trivia Bingo. Se muestran en pantalla preguntas con fragmentos de música, y las respuestas (textos o imágenes) están en el cartón de Bingo.

El quiz wizard incluye compatibilidad específica con Music Bingo. Le permite seleccionar una carpeta con archivos mp3, a partir de los cuales se construye automáticamente la ronda de Bingo.

![](../../assets/images/image125.webp){ width="585" loading=lazy }

### Reclamar Bingo

Cuando un jugador ha marcado suficientes celdas para completar un patrón, hace una reclamación pulsando el botón Bingo de la app móvil. Esto hace que el nombre del jugador aparezca en pantalla y comience una cuenta atrás de 3 segundos mientras el sistema valida la reclamación. No es necesaria ninguna comprobación manual.

![](../../assets/images/image126.webp){ loading=lazy }

Tras la validación, se muestra un pulgar hacia arriba o hacia abajo en la pantalla grande y también en el móvil.

![](../../assets/images/image127.webp){ loading=lazy } ![](../../assets/images/image128.webp){ width="103" loading=lazy }

Con un Bingo válido, el jugador gana puntos (si está configurado) y el sistema pasa al siguiente patrón.

Cuando no hay más patrones que jugar, la ronda termina y el quiz continúa en la diapositiva de fin de ronda (cuando solo hay una ronda y no hay diapositiva de fin de ronda, el quiz muestra la pantalla de puntuación final).

La gestión de varias reclamaciones tiene este aspecto:

![](../../assets/images/image129.webp){ loading=lazy }

Cuando un jugador se desconecta de su quiz o pierde la conexión con la sesión, el cartón de Bingo y las celdas marcadas no se pierden. Al volver a unirse a la partida, el cartón se presentará tal como estaba al desconectarse. Además, si el reproductor del quiz se bloquea, puede reiniciar el quiz, recuperarse desde la instantánea almacenada y continuar la ronda de Bingo.

### Vista de cartón en directo

En QuizXpress Director, en la pestaña ‘Teams’, hay una opción para ver el cartón de Bingo actual del jugador seleccionado. El cartón también muestra qué celdas ya se han jugado, marcadas en verde.

Para mostrar el cartón de un jugador, seleccione al jugador y pulse el botón ‘Show bingo card’. Así, en caso de disputa, siempre puede volver a comprobarlo.

![](../../assets/images/image130.webp){ loading=lazy }

### Cambiar los patrones de Bingo durante una sesión de Bingo

En QuizXpress Director, ahora es posible cambiar los patrones de una ronda de Bingo junto con algunos de los demás ajustes de Bingo durante un quiz (antes de que comience la ronda). Para ello, haga doble clic en la diapositiva de Bingo en la pestaña Questions para abrir los ajustes de una ronda de Bingo.

![](../../assets/images/image131.webp){ width="605" loading=lazy }
