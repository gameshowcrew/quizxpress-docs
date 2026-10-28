# Trivia Ladder round

Una ronda Trivia Ladder permite crear una ronda al estilo de ‘Who Wants to Be a Millionaire®’ (‘¿Quién quiere ser millonario?’) en la que uno o varios jugadores intentan subir por una escalera respondiendo correctamente a las preguntas.

![](../../assets/images/image72.webp){ width="570" loading=lazy }

Al igual que las diapositivas de quiz normales, un Trivia Ladder puede personalizarse por completo con estilos (consulte [Trivia Ladder properties](../user-interface-overview/advanced-properties-grid.md#propiedades-de-trivia-ladder) para obtener más detalles sobre todas las opciones).

## ¿Cómo crear un Trivia Ladder?

Para crear un Trivia Ladder, comience insertando una diapositiva Trivia Ladder en el quiz (vaya al menú INSERT, haga clic en la lista desplegable de la sección Quiz Slides y elija el diseño Trivia Ladder). El Trivia Ladder se generará automáticamente a partir de las preguntas que lo siguen.

!!! note

    a diferencia de todos los demás tipos de diapositiva, la diapositiva Trivia Ladder no se muestra por sí misma durante el quiz. Su único propósito es crear la escalera, que se mostrará en cada diapositiva de la ronda Trivia Ladder durante el quiz.

Para rellenar la escalera, cree *después* de la diapositiva Trivia Ladder tantas preguntas como peldaños desee en la escalera. A continuación puede ver un peldaño de la escalera.

![](../../assets/images/image73.webp){ width="425" loading=lazy }

Peldaño de la escalera

Los números de las preguntas se muestran en el lado izquierdo de la escalera. Los puntos que aparecen a la derecha del número de pregunta se definen según los puntos que tengan las preguntas correspondientes de la ronda Trivia Ladder. También es posible añadir premios a la escalera en lugar de puntos. En el lado derecho de cada peldaño se muestran los mandos que se encuentran en ese peldaño.

El separador situado más a la izquierda (un rombo) indica si la pregunta del peldaño ya se ha jugado.

Solo al final, cuando se ha terminado la última pregunta de la escalera, cada jugador (mando) recibe los puntos del peldaño en el que se encuentra.

Los peldaños de red de seguridad de la escalera suelen tener un color diferente (blanco en la imagen siguiente, por ejemplo) para indicar a qué peldaños retroceden los jugadores cuando responden incorrectamente (en caso de que la *acción de respuesta incorrecta* de la escalera esté establecida en ‘Fall to safety net’).

Al igual que el Trivia Board, un Trivia Ladder puede combinarse con otros formatos de juego de QuizXpress. Para crear un Trivia Ladder (ronda), QuizXpress necesita saber dónde termina una ronda Trivia Ladder. Una ronda Trivia Ladder termina en uno de los siguientes tipos de diapositiva:

- una diapositiva ‘End of round’ (consulte también 3.4.3)

- otra diapositiva Trivia Ladder

- una diapositiva Trivia Board

- el final del quiz (última ronda o un juego solo de Trivia Ladder)

Las preguntas sin puntos (por ejemplo, Audience response, Demographic, Wager) se ignoran al crear el Trivia Ladder.

Como alternativa, ¡el Quiz Wizard puede ayudarle a crear una ronda Trivia Ladder completa con unos pocos clics! Inicie el asistente (pestaña HOME y a continuación ‘Quiz Wizard’) y seleccione ‘create a new round’ y después ‘a Trivia Ladder round’. A continuación, introduzca los puntos e indique dónde están las redes de seguridad.

![](../../assets/images/image74.webp){ width="544" loading=lazy }

Elija el tiempo de pregunta, los puntos y el estilo que se usarán en las páginas siguientes, y pulse ‘Finish’ para que se creen la escalera, las preguntas y la diapositiva final de fin de ronda. Por supuesto, todavía tendrá que introducir las preguntas en sí, pero los puntos, las redes de seguridad y la estructura de la escalera ya estarán configurados.

## Posición en el Trivia Ladder

Cuando un jugador responde correctamente a una pregunta en una ronda Trivia Ladder, avanza un peldaño en la escalera. Cuando una pregunta se responde incorrectamente, puede ocurrir lo siguiente según la ‘Wrong answer action’:

- Same step – el jugador permanece en el mismo peldaño de la escalera.

- One step down – el jugador baja un peldaño en la escalera.

- Fall to safety net – el jugador retrocede a la primera red de seguridad que encuentra.

- Back to bottom – el jugador cae de la escalera y debe volver a empezar.

## Vista previa de un Trivia Ladder

El Trivia Ladder de QuizXpress Studio tal como se muestra en la diapositiva Trivia Ladder solo se utiliza con fines de diseño. Al establecer las opciones de estilo del Trivia Ladder puede determinar el aspecto de la escalera (consulte [Trivia Ladder properties](../user-interface-overview/advanced-properties-grid.md#propiedades-de-trivia-ladder) para obtener más detalles sobre las opciones).

![](../../assets/images/image75.webp){ width="596" loading=lazy }

Cuando desee ver una vista previa de la escalera tal como se mostrará durante el concurso, pulse F5 (o haga clic con el botón derecho en la escalera y pulse ‘Preview’) y la escalera se generará automáticamente a partir de las preguntas presentes en la ronda Trivia Ladder.
