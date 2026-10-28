# Trivia Feud

Establezca el tipo de diapositiva en 'Trivia Feud' para crear un juego basado en encuestas. Después de establecer el tipo de diapositiva en Trivia Feud, aparece el editor de encuestas, donde puede introducir la pregunta de la encuesta y las respuestas de la encuesta con sus porcentajes correspondientes:

![](../../assets/images/image76.webp){ width="578" loading=lazy }

Además de introducir los detalles y las respuestas de la encuesta, puede establecer el juego en tres modos diferentes: Manual, Interactive o Multiplayer. Encontrará más información al respecto a continuación.

Puede utilizar la funcionalidad de inteligencia artificial de QuizXpress para ayudarle a generar encuestas. Después de introducir una pregunta de encuesta, pulse el botón 'Complete with AI' para rellenar automáticamente las respuestas de la encuesta y los porcentajes correspondientes. Consulte [Minijuegos](../mini-games/index.md) para obtener más información.

Después de introducir los detalles y pulsar OK, la vista previa en QuizXpress Studio tiene el aspecto siguiente. El fondo de la pantalla se puede cambiar (para incluir, por ejemplo, el nombre de su empresa o su imagen de marca).

![](../../assets/images/image77.webp){ width="615" loading=lazy }

Al hacer clic en la encuesta, se muestra la pestaña TRIVIA FEUD en la cinta. Aquí se puede cambiar el modo de juego y se puede abrir el Survey Editor haciendo clic en 'Edit Survey'.

![](../../assets/images/image78.webp){ width="592" loading=lazy }

Hay varias opciones disponibles en la barra de herramientas y en la ventana de propiedades avanzadas, que se explicarán más adelante en el contexto de los distintos modos disponibles.

Después de iniciar el programa del quiz, QuizXpress Live muestra el tablero de Trivia Feud con la pregunta de la encuesta y las respuestas de la encuesta ocultas. El siguiente tablero es un ejemplo de un juego Feud en modo Manual.

![](../../assets/images/image79.webp){ width="591" loading=lazy }

Trivia Feud tiene tres modos de juego: **Manual**, **Interactive** (dedo más rápido) y **Multiplayer**.

## Modo Manual

En el modo manual, el juego se controla por completo desde una pantalla de QuizXpress Director, el panel de control del presentador del quiz, que se ejecuta en la pantalla del portátil mientras el programa de concursos se muestra en una pantalla grande.

![](../../assets/images/image80.webp){ loading=lazy }

Las respuestas de la encuesta dadas por los jugadores pueden revelarse manualmente pulsando los botones correspondientes en Director. Los puntos acumulados se muestran en la parte superior, y las puntuaciones se muestran para ambos equipos.

También puede utilizarlo para jugar exactamente el formato del programa de televisión conocido, siguiendo estos pasos:

- Comience con un Faceoff entre los dos equipos pulsando el botón 'Start Faceoff':

- Los jugadores utilizan su pulsador (que puede ser un mando, un pulsador o un teléfono móvil) para pulsar. El jugador que pulsa más rápido aparece en pantalla.

- El jugador que pulsó primero da una respuesta a la encuesta.

- El presentador del quiz revela la respuesta (si está en el tablero) pulsando el botón correspondiente en QuizXpress Director. Los puntos de la respuesta se suman a los puntos del marcador superior, que muestra los puntos que puede ganar el jugador ganador.

- Pulse el botón 'Switch team'.

- El otro jugador también da ahora una respuesta a la encuesta, que el presentador del quiz revela en el tablero si está presente.

- Según el equipo que haya dado la respuesta de mayor rango, convierta a ese equipo en el 'playing team' (es decir, mantenga el equipo seleccionado actualmente o pulse de nuevo 'switch team').

- Los miembros del equipo que juega (o el individuo, en caso de que sea un juego cara a cara entre dos personas) intentan mencionar tantas respuestas como sea posible.

  - Si una respuesta está presente, haga clic en la respuesta correspondiente para revelarla en el tablero y acumular los puntos en el total de puntos que se pueden ganar, que se muestra en la parte superior del tablero.

> ![](../../assets/images/image81.webp){ width="317" loading=lazy }

- Si una respuesta no está presente, haga clic en el botón 'Incorrect' para mostrar en pantalla una cruz que indica que la respuesta era incorrecta. El ajuste 'max wrong answers' del tablero, que se indicó en QuizXpress Studio para la diapositiva, determina después de cuántas cruces pasa el turno al equipo contrario:

> ![](../../assets/images/image82.webp){ width="316" loading=lazy }

- Como en el programa oficial de televisión, el equipo contrario tiene ahora la oportunidad de adivinar una de las respuestas restantes. La respuesta dada puede ser:

  - visible en el tablero: haga clic en la respuesta correspondiente en Director para revelarla. A continuación, haga clic en el botón 'Playing team wins' para asignar los puntos al equipo:

> ![](../../assets/images/image83.webp){ width="358" loading=lazy }

- no presente en el tablero: haga clic en el botón 'Incorrect' para mostrar la cruz roja. Ahora haga clic en 'switch team' para volver al equipo que jugaba originalmente y, a continuación, haga clic en el botón 'Playing team wins' para asignar los puntos al equipo.

- Por último, puede revelar manualmente las respuestas restantes para los jugadores y para el público que está viendo el juego.

El esquema anterior muestra cómo jugar el juego de la misma manera que el formato original del programa de televisión. Como el ajuste manual le da control total, también puede pensar en formas alternativas de jugar.

Si dispone de otro medio para determinar qué equipo comenzará el juego, también puede seleccionar manualmente un equipo pulsando el mensaje 'team playing':

![](../../assets/images/image84.webp){ width="596" loading=lazy }

Esto mostrará una ventana de selección donde puede seleccionar el equipo que comienza.

![](../../assets/images/image85.webp){ width="170" loading=lazy }

Si juegan más de 2 jugadores/equipos, puede seleccionar qué equipos jugarán entre sí haciendo clic en los botones 'select left team' y 'select right team'.

![](../../assets/images/image86.webp){ width="271" loading=lazy }

![](../../assets/images/image87.webp){ width="317" loading=lazy }

El panel de control de QuizXpress Director también contiene un 'points multiplier'. Si elige un valor de 2 o 3, los jugadores reciben 2 o 3 veces más puntos, respectivamente. Podría aplicarlo, por ejemplo, en una ronda final, en la que un equipo tiene que superar un determinado número de puntos para ganar.

## Modo Interactive (Fastest Finger)

En este modo, todos los jugadores participan y pueden pulsar para dar su respuesta.

El jugador que pulsa más rápido se muestra en la pantalla grande con el número actual de puntos y tiene la oportunidad de responder a la encuesta.

![](../../assets/images/image88.webp){ width="255" loading=lazy }

Los jugadores disponen de un tiempo limitado para dar una respuesta. Esto se indica mediante un temporizador de cuenta atrás en la parte superior. El tiempo se puede configurar en la propiedad Answer Time (disponible en la cuadrícula de propiedades). Si un jugador no responde dentro del plazo, aparecen tres cruces y al jugador se le descuentan puntos de penalización.

![](../../assets/images/image89.webp){ loading=lazy }

Si la respuesta dada está en el tablero, el presentador del quiz revela la respuesta haciendo clic en el botón correspondiente en QuizXpress Director. Los puntos se muestran en la parte superior y después se suman al total del jugador.

![](../../assets/images/image90.webp){ width="223" loading=lazy } ![](../../assets/images/image91.webp){ width="227" loading=lazy }

Si la respuesta dada no está presente, haga clic en la cruz en Director, que se muestra entonces en la pantalla grande. En este caso se restarán los puntos indicados para 'wrong answer' en la pestaña QUESTION.

![](../../assets/images/image92.webp){ width="568" loading=lazy }

Al crear la diapositiva Trivia Feud en modo Fastest Finger, puede indicar cuántas respuestas puede dar un jugador tras pulsar (max correct answers), cuántas respuestas incorrectas se pueden dar antes de que termine el turno del jugador (max incorrect answers) y si un jugador queda excluido del tablero actual o puede volver a pulsar (Exclude o Continue).

![](../../assets/images/image93.webp){ width="605" loading=lazy }

También puede cambiar los ajustes anteriores en el panel de propiedades avanzadas, que puede mostrar haciendo clic en la pestaña VIEW y marcando la casilla situada antes de 'Properties'. En este panel verá todos los ajustes que se aplican al Trivia Feud una vez que haga clic en él.

La opción auto reveal indica si las respuestas restantes que no se mencionaron se mostrarán automáticamente cuando todos los jugadores estén fuera del juego, o si el presentador las revelará manualmente una por una haciendo clic en las respuestas en QuizXpress Director.

## Modo Multiplayer

Cuando el tablero está en modo multiplayer, todo el público puede participar.

![](../../assets/images/image94.webp){ width="321" loading=lazy }

En la parte superior del tablero de Trivia Feud se muestra un temporizador de cuenta atrás. En QuizXpress Studio, en la pestaña QUESTION, el 'Answer time' se puede configurar de la misma manera que para una pregunta normal.

Los jugadores envían sus respuestas desde su teléfono móvil mientras la cuenta atrás está en marcha, introduciendo y enviando varios textos.

![](../../assets/images/image95.webp){ width="385" loading=lazy }

En la ventana de propiedades de Studio (si no está visible, muéstrela haciendo clic en la pestaña VIEW y marcando la casilla situada antes de Properties), verá las siguientes opciones que se aplican al modo multiplayer:

**Response limit** – especifica el número máximo de respuestas que puede enviar un jugador.

**Tolerance** – especifica la tolerancia que utiliza QuizXpress para juzgar las respuestas dadas. Si se establece una tolerancia mayor, se admiten más errores ortográficos.

**Auto reveal** – indica si, al final de la cuenta atrás, las respuestas se mostrarán automáticamente o si el presentador las revelará manualmente una por una haciendo clic en las respuestas en QuizXpress Director.

En este modo, puede especificar varias respuestas correctas, separadas por un punto y coma:

![](../../assets/images/image96.webp){ width="430" loading=lazy }

La entrada de los jugadores se compara con cada entrada con la tolerancia establecida.
