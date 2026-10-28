# ­La pantalla del quiz: voting (todos responden)

Después del vídeo de cuenta atrás (que puede desactivarse y/o sustituirse por su propio vídeo en Quiz Setup), aparece la pantalla del quiz. Como puede ver en la captura siguiente, hay algunas zonas que requieren una atención especial, todas ellas parte de lo que llamamos el ‘Information Panel’:

1.  El temporizador de cuenta atrás. Este temporizador cuenta hacia atrás desde el tiempo indicado al crear el quiz en QuizXpress Live hasta cero. Debajo del temporizador puede ver una indicación de la posición de la pregunta en el quiz, con el formato \<número de pregunta/número total de preguntas>.

2.  Los equipos (participantes) que han pulsado su mando. Este indicador tiene tres fases: primero muestra una cuadrícula de cuadrados que indica de qué mando se ha recibido una respuesta, ofreciendo una imagen general. Cuando quedan pocos mandos, muestra los números de mando individuales. Cuando quedan aún menos, muestra los nombres de los jugadores tal como se establecieron en Quiz Setup, lo que ayuda al presentador del quiz a identificar a los últimos jugadores que aún deben responder.

3.  El número total de jugadores que ya han dado una respuesta.

4.  El número de puntos que se obtienen al responder correctamente a la pregunta. Tenga en cuenta que los puntos pueden disminuir con el tiempo según los ajustes de la diapositiva establecidos en Studio.

![](../../assets/images/image407.webp){ loading=lazy }

Cuando todos los equipos han hecho su elección, el sistema juzga todas las respuestas y suma o resta puntos a las puntuaciones. Además, en la parte superior de la pantalla del quiz se muestra un gráfico:

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Número de equipos que respondieron correctamente</p></li>
<li><p>Número de equipos que respondieron incorrectamente</p></li>
<li><p>Número de equipos que no respondieron en absoluto</p></li>
</ul></th>
<th><img src="../../../assets/images/image408.webp" alt="" width="368" loading="lazy"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Cuando utiliza pulsadores Sony, QuizXpress Live procesa una diapositiva de quiz de tipo voting de forma ligeramente distinta. En lugar de un contador en la parte superior de la pantalla que cuenta el número de equipos que han respondido hasta el momento, aparece un panel con el nombre y el avatar de cada equipo a medida que responde. Después de que todos hayan pulsado su pulsador (o de que la cuenta atrás haya llegado a cero), QuizXpress Live muestra todas las respuestas elegidas, las juzga y muestra las puntuaciones totales de todos los equipos. A continuación se muestra una representación visual de esta secuencia.

| ![](../../assets/images/image409.webp){ width="160" loading=lazy } | ![](../../assets/images/image410.webp){ width="166" loading=lazy } |                                                                                 | ![](../../assets/images/image411.webp){ width="155" loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| ![](../../assets/images/image412.webp){ loading=lazy } |                                                                                 | ![](../../assets/images/image413.webp){ loading=lazy } | ![](../../assets/images/image414.webp){ loading=lazy } |

Voting es uno de los modos posibles de una diapositiva de quiz. Otras variantes se describen a continuación.

## Fastest Finger/ Lock-out

En la sección anterior hemos tratado la pantalla de una pregunta de tipo ‘voting’, en la que todos pueden responder. Con una pregunta de tipo fastest-finger, solo la primera persona que pulsa su pulsador puede responder. Si responde incorrectamente, se le restan puntos de su puntuación y la cuenta atrás continúa. Entonces, los demás jugadores tienen la oportunidad de pulsar su pulsador (el jugador que respondió incorrectamente ya no puede responder a la pregunta actual).

En la página siguiente verá una imagen de una pantalla típica de fastest finger. La diferencia más importante con respecto a una pantalla de voting es que en esta pantalla hay una barra grande en la parte inferior con el nombre del equipo (o de la persona) que pulsó primero su pulsador. Esta barra también muestra la respuesta dada, el avatar del equipo, así como los puntos ganados/perdidos. En este caso, el equipo 17 dio la respuesta correcta, con lo que obtiene 10 puntos. La gran marca de verificación verde indica que la pregunta se respondió correctamente. En este ejemplo, la respuesta correcta se estableció como Answer-‘D’ en QuizXpress Studio y la opción ‘autojudge’ (judge question automatically en la cinta de menú) de la diapositiva Quiz se estableció en true. En este caso, QuizXpress juzga automáticamente la respuesta cuando se pulsa un botón de opción múltiple en un pulsador. Cuando un pulsador no tiene botón de opción múltiple (por ejemplo, los postes Sparkle), la opción ‘auto judge’ no se aplica automáticamente. En ese caso, el equipo\jugador debe responder verbalmente y, a continuación, el presentador del quiz debe juzgar la respuesta utilizando su mando a distancia, el teclado del ordenador o QuizXpress Director. Puede leer más sobre los comandos del presentador del quiz en [Control del quiz](../controlling-the-quiz.md).

El hecho de que ‘Team 17’ pulsara primero puede verificarse consultando el ‘Information Panel’ en la parte superior de la pantalla. Este panel muestra, en cuadros separados, la hora a la que cada equipo pulsó. Cada cuadro contiene el nombre de un equipo que pulsó su pulsador, junto con la marca de tiempo en la que lo hizo, ordenados de izquierda a derecha, empezando por el equipo más rápido.

| ![](../../assets/images/image415.webp){ loading=lazy } | ![](../../assets/images/image416.webp){ loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|

Tenga en cuenta que el Information Panel de la parte superior muestra el número de puntos que se pueden obtener (que pueden disminuir con el tiempo, como se explicó anteriormente). Además, no hay ningún indicador del número de equipos que han respondido, ya que esto no es aplicable a una pregunta de tipo fastest-finger.

!!! note

    Cuando utilice los pulsadores QuizXpress (que tienen tanto botones de opción múltiple ABCD como un botón de pulsador grande) para preguntas de opción múltiple, tenga en cuenta estas dos opciones:*

- *Cuando ‘auto judge’ es ‘true’ en la ventana de propiedades (equivalente en la cinta de menú: ‘Judge question’ está establecido en ‘Automatically’), los participantes deben utilizar los botones ABCD del pulsador. QuizXpress juzga automáticamente la respuesta dada.*

- *Cuando ‘auto judge’ es ‘false’ en la ventana de propiedades (equivalente en la cinta de menú: ‘Judge question’ está establecido en ‘Manual’), los participantes deben utilizar el botón grande del pulsador para intervenir. El jugador que pulsó más rápido da entonces la respuesta verbalmente y el presentador del quiz la juzga.*

## Billboard

Una diapositiva de quiz Billboard es una diapositiva de quiz con la que no es posible ninguna interacción del jugador: es simplemente una pantalla estática. Puede diseñar una diapositiva Billboard igual que una pregunta normal, utilizando texto, colores, imágenes, sonidos y vídeos.

Entre las aplicaciones útiles de una diapositiva Billboard se incluyen:

- Indicación de ronda

- Mostrar la pregunta (como vista previa) antes de una diapositiva de quiz de tipo voting.

- Mostrar información de marketing en forma de imágenes, sonidos o vídeos

## End of Round

En QuizXpress puede indicar que una diapositiva de quiz marca el ‘final de una ronda’. Para ello, establezca el tipo de la diapositiva de quiz en ‘End of Round’ en QuizXpress Studio.

Cuando se muestra una diapositiva End of Round durante un quiz, no se produce ninguna interacción con los participantes. Por ejemplo, podría utilizarla para mostrar el texto ‘End of Round 3’. Como antes, puede diseñar la diapositiva como desee, con vídeo, sonido e imágenes.

Al establecer una diapositiva como ‘End of Round’, hay otra opción, llamada ‘end of round action’, que se puede configurar. Puede establecerse en una de las siguientes opciones:

- Disable one player: descarta automáticamente al jugador con menos puntos. Si varios jugadores están empatados en la parte inferior de la lista de puntuaciones intermedias, el presentador del quiz selecciona qué jugador será descartado, utilizando las teclas de flecha del teclado o el mando a distancia del presentador del quiz. El jugador/equipo seleccionado se resalta con una luz roja parpadeante. Al pulsar la barra espaciadora del teclado, o el botón inferior del mando a distancia del presentador, se descarta al jugador seleccionado. Decidir qué jugador descartar cuando varios equipos tienen la misma puntuación queda fuera del alcance de QuizXpress Live; por ejemplo, un presentador del quiz podría plantear una pregunta de estimación y descartar al jugador cuya respuesta se aleje más de la correcta.

> ![](../../assets/images/image417.webp){ loading=lazy }

- Manually dismiss players: el presentador del quiz puede seleccionar cualquier número de jugadores para descartar. Lo hace uno por uno, de nuevo utilizando el teclado o el mando a distancia del presentador para seleccionarlos. Más arriba se muestra un ejemplo de una diapositiva de quiz ‘End of Round, quizmaster selects losers’. El botón de ‘play’ en la parte inferior de la pantalla indica que el presentador del quiz ha terminado de descartar jugadores; al pulsarlo (selecciónelo con el teclado y pulse la barra espaciadora) el quiz continúa. El botón con la flecha giratoria deshace el proceso de descarte si el presentador del quiz descarta a alguien por error, tras lo cual puede volver a empezar a descartar jugadores.

- Automatically dismiss players: con esta opción, el sistema deshabilita automáticamente un determinado número de jugadores (según lo configurado para la diapositiva en Studio), sin ninguna indicación visual para el público.

Show scoreboard/Show round scores: el sistema muestra la clasificación de todo el quiz o de la ronda actual.

Reset scores: restablece todas las puntuaciones al final de la ronda.

Una ronda se define como el conjunto de diapositivas comprendidas entre:

- La primera diapositiva del quiz y la primera diapositiva End of Round (ronda 1)

- Dos diapositivas *End of Round*

- La diapositiva que sigue a la última diapositiva *End of Round* y la última diapositiva del quiz

A continuación puede ver un ejemplo de un quiz con tres rondas.

![](../../assets/images/image418.webp){ width="595" loading=lazy }

Una diapositiva ‘End of Round’ también puede utilizarse para rondas de ‘Last Man Standing’. Cuando se utilizan preguntas ‘Last Man Standing’, los jugadores que responden incorrectamente son eliminados del quiz y ya no pueden seguir jugando. Cuando se muestra una diapositiva ‘End of Round’, todos los jugadores que están fuera de juego a causa de preguntas ‘Last Man Standing’ pueden volver a incorporarse.

!!! note

    Los jugadores\equipos también pueden activarse\desactivarse desde QuizXpress Director. En QuizXpress Director también puede añadir nuevos jugadores durante un quiz o modificar los puntos de un equipo. Consulte [QuizXpress Director](../quizxpress-director/index.md) para obtener más información sobre QuizXpress Director.*

## Test Question

Una diapositiva de quiz ‘Test Question’ se comporta igual que una diapositiva de quiz normal, salvo que no se suman ni se restan puntos cuando se ha respondido a la pregunta. Puede utilizarse para demostrar cómo funciona el sistema y suele usarse como primera pregunta de un quiz para que los jugadores se familiaricen con el sistema.

## Demographic

El tipo de diapositiva de quiz ‘Demographic’ permite dividir a todos los jugadores en diferentes grupos que compiten entre sí (algunos ejemplos de este tipo de quizzes son ‘batalla de sexos’, ‘marketing contra finanzas’, etc.).

Para utilizar esta funcionalidad, establezca el tipo de una diapositiva de quiz en ‘Demographic’ en QuizXpress Studio. Aparece entonces un campo de entrada en la cuadrícula de propiedades llamado ‘Demographic group’, donde puede introducir el nombre de un grupo demográfico (p. ej., ‘Males’). Para el diseño de la diapositiva de quiz, debe seleccionar un diseño que contenga una pregunta y ninguna respuesta. Introduzca un texto de pregunta que indique a los jugadores que un determinado grupo de personas debe pulsar su pulsador para convertirse en miembro de un grupo específico (p. ej., ‘Please press your buzzer if you are male’).

!!! note

    Como alternativa, puede dividir al público en grupos antes de que comience un quiz en QuizXpress Setup. Aquí puede definir qué mandos pertenecen a qué grupo. Para obtener más información, consulte [Agrupación de mandos](../../setup/setting-up-teams-the-teams-tab-page.md#agrupacion-de-mandos)*

## Last Man Standing

Una diapositiva de quiz de tipo ‘Last Man Standing’ elimina de la ronda del quiz a los jugadores que responden incorrectamente a una pregunta. Si tras la eliminación queda un solo jugador, ese jugador gana la ronda y el quiz avanza hasta la primera diapositiva End of Round que encuentre, o hasta el final del quiz. Sin embargo, si todos los jugadores restantes responden incorrectamente a una pregunta, ninguno de ellos es eliminado.

## Preguntas de respuesta del público

Este es un tipo de pregunta que puede utilizarse para recopilar datos/estadísticas arbitrarios de su público. Las respuestas dadas a una pregunta de respuesta del público se registran, pero no tienen ningún efecto en las puntuaciones. Después de una pregunta de respuesta del público, puede mostrar un gráfico con la tecla ‘C’ para ver la distribución de las respuestas dadas.

![](../../assets/images/image419.webp){ width="604" loading=lazy }

## Pregunta Wager

Las preguntas Wager pueden utilizarse para que el público apueste sobre el resultado de la siguiente pregunta. Permiten crear preguntas ‘estilo Jeopardy’ en las que las personas arriesgan puntos según cuánto creen saber sobre un tema.

Cuando establece una diapositiva de quiz en el tipo ‘Wager’, tiene el siguiente aspecto en QuizXpress Studio:

![](../../assets/images/image420.webp){ loading=lazy }

El texto de la pregunta se cambia de forma predeterminada a “Please place your bet for the next question…”, pero puede cambiarlo más adelante por lo que desee. Las respuestas a este tipo de pregunta se utilizan para establecer el porcentaje de la puntuación que el jugador puede ganar o perder en la siguiente pregunta. Por ejemplo, si el jugador responde ‘C’ a esta pregunta, significa que apuesta el 66 % de su puntuación en la siguiente pregunta. Si responde correctamente a la siguiente pregunta, su puntuación aumenta un 66 %. Por supuesto, si utiliza un diseño de diapositiva con cinco respuestas, los porcentajes se distribuyen entre cinco opciones (0 %, 25 %, 50 %, 75 % y 100 %). También puede establecer el porcentaje manualmente haciendo clic en cualquiera de las respuestas y cambiando la propiedad ‘Wager %’.

Las apuestas (Wager) también pueden utilizarse con un número de puntos en lugar de un porcentaje.
