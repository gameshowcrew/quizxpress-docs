# Uso de dispositivos físicos

Una instalación completa de QuizXpress con hardware podría tener el siguiente aspecto:

![](../assets/images/image349.webp){ width="514" loading=lazy }

En esta instalación se utilizan todos los elementos de hardware compatibles con QuizXpress: mandos/pulsadores, pulseras Galaxy y marcadores. Como puede ver, se utiliza un receptor distinto para cada tipo de dispositivo.

Antes de describir el software con todo detalle, veamos primero los tipos de pulsadores admitidos y cómo utilizarlos.

## Uso de los mandos, pulsadores y postes pulsadores de QuizXpress

Los dos tipos de mando de QuizXpress, el normal y el Plus, tienen seis botones y un botón de fastest finger. Cuando se presenta una pregunta, al pulsar uno de los botones se enciende la luz roja indicadora de transmisión situada en la parte superior derecha del mando, lo que significa que está enviando su elección al receptor inalámbrico conectado al ordenador que ejecuta QuizXpress Live. Mientras la luz roja del mando sigue encendiéndose, el mando está intentando enviar la elección al receptor. Cuando parpadea la luz verde de la parte superior izquierda, la señal se ha procesado correctamente. Si la transmisión no tuvo éxito, el LED rojo parpadea varias veces.

Los mandos de QuizXpress se emparejan con un único receptor, y cada receptor tiene un número de serie único (por lo que, si desea pedir un receptor de repuesto, asegúrese de indicar el número de serie). QuizXpress incluye una práctica herramienta para *emparejar* un mando con el receptor conectado y asignarle un número. La herramienta *QuizXpress Device Programmer* se encuentra en la entrada de QuizXpress del menú Inicio de Windows, o en el menú *Tools* de QuizXpress Studio.

| ![](../assets/images/image350.webp){ width="287" loading=lazy } | ![](../assets/images/image351.webp){ width="288" loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|

Para empezar a programar cualquier mando o pulsador de QuizXpress, conecte el receptor al ordenador y elija el tipo de receptor en la lista desplegable de receptores. Introduzca el rango de mandos que va a programar y pulse Connect. Debería aparecer una marca de verificación verde que indica que la conexión con el receptor se ha realizado correctamente.

La herramienta de programación permite programar el número (id) de un solo mando, o de forma semiautomática para un conjunto completo de mandos (aún tendrá que pulsar los botones de la ‘mano’ y ‘B’ en cada mando). Para programar un solo mando, establezca el número deseado en el campo ‘Keypad to set’, haga clic en ‘Set’ y, en un plazo de 4 segundos, pulse a la vez los botones de la ‘mano’ y ‘B’ del mando (vea la imagen de la derecha).

Los mandos tienen una asociación única con el receptor y primero deben emparejarse con él. Al establecer el id de un mando, este también se empareja de inmediato con el receptor conectado. Para emparejar el mando a distancia de QuizXpress, pulse el botón ‘Set’ de la herramienta de programación y pulse al mismo tiempo los botones Power y Up del mando a distancia.

Para programar los pulsadores de QuizXpress, haga clic en el botón ‘Set Buzzer’ de la herramienta de programación. La luz amarilla del receptor se enciende. Ahora pulse a la vez el botón B y el botón grande. Mantenga pulsado el botón grande hasta que parpadee. Cuando parpadee, espere a que se apague la luz amarilla y después pulse el pulsador. El número del pulsador aparecerá ahora en la herramienta de programación.

Para programar los pulsadores Galaxy RGB de QuizXpress, siga los mismos pasos que para los pulsadores anteriores, pero en lugar de pulsar B y el botón grande, pulse C y el botón grande hasta que el pulsador parpadee.

Los postes pulsadores Sparkle, así como la mesa pulsadora Luminous, también se pueden programar. Utilizan el mismo receptor que los pulsadores de QuizXpress.

Para programar los postes pulsadores Sparkle:

- Apague el pulsador.

- Pulse el botón ‘Set Buzzer’ en QuizXpress Device Programmer.

- Ahora pulse el botón del pulsador del Sparkle y vuelva a encender el Sparkle.

- Ahora parpadeará, lo que indica que está programado con el ID indicado en la aplicación de programación.

Para programar las mesas de quiz Luminous:

- ![](../assets/images/image352.webp){ width="106" loading=lazy }Apague el Luminous.

- Pulse el botón ‘Set Buzzer’ en QuizXpress Device Programmer.

- Ahora pulse el pequeño botón negro situado junto al botón de encendido/apagado del Luminous y vuelva a encender el Luminous.

- Ahora parpadeará, lo que indica que está programado con el ID indicado en la herramienta de programación.

## Uso de los mandos de Fleetwood Reply Systems

| ![](../assets/images/image353.webp){ width="193" loading=lazy } | Los mandos Fleetwood Reply Mini tienen cinco botones. Cuando se muestra una pregunta, al pulsar uno de los botones se enciende la luz indicadora de transmisión situada en la parte superior del mando, lo que significa que está enviando su elección al receptor inalámbrico conectado al ordenador que ejecuta Quiz Show. Cuando la luz del mando se pone roja, significa que el receptor inalámbrico no ha recibido la respuesta y el participante debe intentar enviar de nuevo su respuesta. Cuando la luz se pone verde, la señal se ha procesado correctamente. |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Uso de los pulsadores Sony

Los pulsadores Sony BuzzTM existen en dos versiones: con cable e inalámbricos. Tienen cuatro botones de colores, que representan las respuestas de opción múltiple A (azul), B (naranja), C (verde) y D (amarillo), y un botón rojo grande. El botón rojo puede iluminarse.

En Quiz Show, las respuestas de opción múltiple tienen el mismo color que los cuatro botones de colores de opción múltiple del pulsador.

| ![](../assets/images/image354.webp){ width="65" loading=lazy } | Cuando se muestra una pregunta en QuizXpress Live, los botones rojos de todos los pulsadores (excepto los de los jugadores ya eliminados de la partida) se iluminan, lo que significa que los pulsadores esperan una entrada. |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Cuando una pregunta es de opción múltiple (ya sea fastest finger o votación; consulte [Presentación del show con QuizXpress Live](index.md)), el jugador debe pulsar uno de los botones de opción múltiple para responder. Cuando una pregunta es ‘abierta’ (lo que implica que siempre es fastest finger), debe pulsarse el botón rojo para responder.

Cuando una pregunta es ‘fastest finger’ y un jugador es el más rápido en pulsar, la luz roja empieza a parpadear. Si la pregunta era una ‘pregunta abierta’, el jugador dice su respuesta al presentador del quiz, que la juzga. Si la pregunta era de opción múltiple, el jugador ya ha dado su respuesta al pulsar uno de los cuatro botones de opción múltiple; en este caso, Quiz Show juzga automáticamente la respuesta y suma o resta puntos.

Si la respuesta era incorrecta, la cuenta atrás continúa. El jugador que respondió incorrectamente ya no puede participar en la respuesta a la pregunta actual, por lo que su pulsador no se iluminará hasta que se muestre la siguiente pregunta.
