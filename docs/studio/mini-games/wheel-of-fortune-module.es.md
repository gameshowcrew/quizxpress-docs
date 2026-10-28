# Módulo Wheel of Fortune

Wheel of Fortune permite hacer girar una rueda para sortear un premio o puntos para un equipo, o simplemente sortear un equipo concreto.

![La Wheel of Fortune con premios y puntos](../../assets/images/wheel-of-fortune-game.webp){ loading=lazy }

A continuación se muestran las pantallas de configuración con sus ajustes predeterminados:

| ![La pestaña ‘Game’](../../assets/images/wheel-of-fortune-settings-game.webp){ width="240" loading=lazy } | ![La pestaña ‘Appearance’](../../assets/images/wheel-of-fortune-settings-appearance.webp){ width="240" loading=lazy } | ![La pestaña ‘Other’](../../assets/images/wheel-of-fortune-settings-other.webp){ width="240" loading=lazy } |
|---|---|---|

- Participants: elija quién juega con la rueda.

    - ‘Select participating players before game’: se seleccionan los jugadores en la pantalla del director, justo antes de que empiece la rueda.
    - ‘Play the game with the top’: juegan con la rueda los jugadores mejor clasificados, según el número indicado.
    - ‘The player with this ranking can stop the wheel for a prize’: un único jugador con una determinada posición en la clasificación puede detener la rueda con su mando para conseguir un premio. Desmarque ‘Show player’ para ocultar el panel que muestra quién es este jugador.
    - ‘Play with the winner of the last question’: juega con la rueda el equipo que respondió correctamente primero a la pregunta anterior. Si nadie respondió correctamente a esa pregunta, se omite la rueda.
    - ‘None (wheel only)’: solo se muestra la rueda, sin equipos. Úselo para sortear un premio para alguien de la sala. Los puntos de la rueda se muestran, pero no se conceden a ningún equipo.

- Draw a prize: los premios (que también pueden ser puntos positivos o negativos) se muestran en la rueda. Al pulsar el botón ‘Setup prizes’ se pueden configurar los premios; consulte [Configuración de los premios](#configuracion-de-los-premios).

- Draw a team/player: los participantes seleccionados se distribuyen por la rueda. En ‘Show in wheel’ elija si la rueda muestra los nombres de los equipos o los números de los mandos. El número de segmentos de la rueda se puede elegir seleccionando un valor en ‘Number of segments’. Si la casilla situada antes de ‘Show prize’ está marcada, los premios que se pueden ganar (o perder) se muestran junto a la rueda. Mientras la rueda gira, los premios se resaltan uno tras otro. Cuando la rueda se detiene en un jugador o equipo, el premio resaltado se gana (o se pierde, en el caso de los puntos negativos). Los premios (o puntos) se pueden definir pulsando el botón ‘Setup prizes’. Este modo no funciona en combinación con la opción ‘stop the wheel’ de la sección ‘participants’, ya que en el juego ‘stop the wheel’ se necesitan premios en la rueda, ni con ‘None (wheel only)’.

- Draw bonus points: los puntos positivos, negativos y Kapow! se distribuyen por la rueda en el número de segmentos indicado. En el caso de los puntos positivos y negativos, cada segmento aumenta o disminuye de valor, respectivamente (por ejemplo: unos puntos positivos de 1 con 5 segmentos dan los valores 1, 2, 3, 4 y 5; unos puntos negativos de -2 con 4 segmentos dan los valores -2, -4, -6, -8). Los puntos Kapow! son puntos negativos fijos repartidos entre el número de segmentos especificado. ¡Los segmentos Kapow! son aquellos en los que los jugadores no quieren caer! El número total de segmentos de la sección ‘Draw bonus points’ no puede superar 40.

- Pestaña Appearance: establezca el texto del título del juego, la fuente del título (que también se usa para el panel junto a la rueda y para el resultado) y la fuente del texto de la rueda. Elija una imagen de fondo, así como la imagen que se muestra en el centro de la rueda. Sin imagen central, la rueda muestra una estrella dorada en el centro. En ‘Sound’ puede elegir la música (un archivo MP3) que suena mientras la rueda está en pantalla.

- Pestaña Other: establezca la velocidad de giro de la rueda, así como el tiempo de giro.

## Configuración de los premios

![La ventana ‘Setup prizes’](../../assets/images/wheel-of-fortune-setup-prizes.webp){ loading=lazy }

Cada fila es un premio:

- Prize type: ‘Prize’ para algo que se puede ganar, o ‘Points’ para ganar puntos (o perderlos, con un número negativo).
- Points: el número de puntos de un premio ‘Points’. La rueda muestra este número.
- Prize name: el texto que aparece en la rueda y en el mensaje para el ganador.
- Repeat: el número de segmentos que ocupa el premio en la rueda. Un premio que aparece más de una vez se reparte por la rueda.
- Image: una imagen opcional, que se muestra en la rueda en lugar del nombre.

La ventana comienza con ocho filas. Pulse ‘Add prize’ para obtener más filas, hasta un máximo de 40 premios. Las filas vacías posteriores a las ocho primeras se eliminan al pulsar ‘OK’. La rueda tiene espacio para 40 segmentos en total, o 24 cuando los premios tienen una imagen.

La misma ventana configura los premios que se muestran junto a la rueda cuando se sortea un equipo o jugador. La columna ‘Repeat’ no se utiliza en ese caso.

!!! note
    Las versiones anteriores de QuizXpress solo admiten ocho premios. Reproduzca un quiz con más premios en un ordenador con la última versión.

## Cómo se juega

Para hacer girar la rueda, pulse el botón ‘Spin’ del panel del lado izquierdo.

![](../../assets/images/image143.webp){ width="142" loading=lazy }

Mientras la rueda gira, las luces del borde se persiguen. Cuando la rueda se detiene, el segmento situado bajo el puntero parpadea y mantiene un contorno dorado, y el resultado se muestra en la parte inferior de la pantalla.

![El resultado tras un giro](../../assets/images/wheel-of-fortune-result.webp){ loading=lazy }

Cuando el ajuste ‘Stop the wheel’ está activado, el jugador que puede detener la rueda con su mando se indica en el panel ‘Teams’ del juego. El pulsador situado debajo del nombre se agita cuando el jugador pulsa su mando. La rueda también se puede detener pulsando el botón ‘Stop the Wheel!’ (aunque normalmente no es necesario, ya que debería ser el jugador quien detenga la rueda).

![El jugador que puede detener la rueda](../../assets/images/wheel-of-fortune-stop-the-wheel.webp){ loading=lazy }

![](../../assets/images/image144.webp){ width="143" loading=lazy }
