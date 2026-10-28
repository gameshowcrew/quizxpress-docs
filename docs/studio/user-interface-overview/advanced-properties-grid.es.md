# Cuadrícula de propiedades avanzadas

El panel de propiedades es el lugar donde puede establecer rápidamente todas las propiedades detalladas de los elementos seleccionados. Cada elemento (como una pregunta, una respuesta, una diapositiva, un vídeo o una imagen) tiene sus propias propiedades. No es imprescindible utilizarlo, ya que los ajustes más importantes se pueden alcanzar desde la cinta de opciones, pero para los usuarios avanzados puede ser una forma más rápida de hacer las cosas. (algunas propiedades más avanzadas u oscuras solo se pueden alcanzar desde el panel de propiedades). En los capítulos siguientes encontrará una explicación de las propiedades más importantes. Puede mostrar el panel de propiedades yendo al menú VIEW y marcando ‘Properties’ (en la sección ‘Views’).

QuizXpress muestra esas propiedades en el **panel de propiedades**, que se obtiene de forma predeterminada, y sigue ofreciendo la **cuadrícula de propiedades clásica** que utilizaban las versiones anteriores. Ambos muestran exactamente las mismas propiedades y puede cambiar de uno a otro cuando quiera, por lo que los capítulos siguientes se aplican a cualquiera de los dos.

## El panel de propiedades

![](../../assets/images/properties-panel-overview.webp){ width="322" loading=lazy }

En lugar de una larga lista alfabética, el panel agrupa las propiedades del elemento seleccionado en páginas y secciones, y asigna a cada propiedad un control adecuado: un interruptor para un ajuste de sí/no, un control deslizante para una transparencia, una muestra de color para un color, etc. Todo lo que cambie se aplica a la diapositiva de inmediato.

**Qué está seleccionado**

La parte superior del panel indica lo que está editando: un icono, el tipo del elemento y una segunda línea con su contenido (el texto de una respuesta, el nombre de archivo de una imagen). Cuando selecciona varios elementos a la vez (por ejemplo, las cuatro respuestas de una pregunta), el título dice ‘4 objects selected’ y el panel muestra las propiedades que tienen en común. Las propiedades cuyos valores difieren entre los elementos seleccionados se muestran vacías o como ‘Mixed’; en cuanto establezca una, todos los elementos seleccionados reciben el nuevo valor.

**Páginas**

Debajo del cuadro de búsqueda hay una fila de páginas: *Gameplay*, *Scoring*, *Design*, *Text*, *Media* y *Advanced*. Solo se muestran las páginas que realmente tienen propiedades para la selección actual, y la página más relevante para el elemento seleccionado aparece primero: la página *Text* para un elemento de texto, *Gameplay* para una diapositiva de quiz. La página *Advanced* (la pestaña `{}`) reúne las propiedades técnicas: metadatos, ajustes de dispositivos móviles y scripting. Haga clic en una pestaña para cambiar de página; el panel recuerda su elección para cada tipo de elemento.

**Secciones y más opciones**

Cada página se divide en secciones como ‘Timing’, ‘Answering’ o ‘Border’. Haga clic en el título de una sección para plegarla y utilice *Expand all sections* / *Collapse all sections* en el menú de opciones para hacerlo con todas a la vez. Las secciones que contienen además propiedades poco utilizadas muestran un enlace **More options** en la parte inferior; haga clic en él para mostrarlas y en **Fewer options** para ocultarlas de nuevo. El panel recuerda qué secciones ha contraído y cuáles muestran sus opciones adicionales.

**Buscar una propiedad**

![](../../assets/images/properties-panel-search.webp){ width="322" loading=lazy }

Si no sabe dónde se encuentra una propiedad, escriba una palabra en el cuadro de búsqueda de la parte superior (o pulse *Ctrl+F*). El panel muestra entonces de una vez todas las propiedades coincidentes de todas las páginas, con la parte coincidente del nombre resaltada. La búsqueda también examina las descripciones, de modo que una palabra que solo aparece en la explicación de una propiedad también la encuentra. Haga clic en la ✕ del cuadro de búsqueda para volver a la vista normal.

### Cambiar valores

![](../../assets/images/properties-panel-text-editors.webp){ width="322" loading=lazy }

La mayoría de las propiedades se explican por sí solas: escribir en un cuadro, accionar un interruptor, elegir en una lista desplegable. Algunas merecen una mención especial.

Los **números** se pueden escribir, ajustar con las pequeñas flechas situadas a la derecha del cuadro o, a menudo más rápido, cambiar *arrastrando el nombre de la propiedad* a izquierda y derecha. Mantenga pulsada la tecla *Shift* mientras arrastra para pasos mayores y *Alt* para pasos más finos. Las propiedades que tienen un mínimo y un máximo razonables, como una transparencia, disponen de un control deslizante con un cuadro numérico al lado; ambos se mantienen sincronizados.

Las **fuentes** se establecen con una lista desplegable que muestra una vista previa de todas las fuentes instaladas, un cuadro de tamaño y botones de negrita, cursiva y subrayado.

Las **propiedades agrupadas**, como un degradado o un tamaño, muestran un resumen en una sola línea. Haga clic en el nombre de la propiedad para desplegar debajo los ajustes individuales (para un degradado: From, To y Type).

### Colores

![](../../assets/images/properties-panel-color-picker.webp){ width="333" loading=lazy }

Una propiedad de color muestra una muestra con su valor hexadecimal. Haga clic en ella y obtendrá:

- **No color**, para las propiedades que pueden dejarse vacías (por ejemplo, un fondo transparente).
- Una **paleta** de tonos en la parte superior y una fila de **Standard colors** debajo.
- **Recent colors**: los colores que utilizó anteriormente, de modo que repetir un color en varios elementos requiere un solo clic. Se recuerdan mientras QuizXpress Studio esté en ejecución.
- **Custom color**, que despliega un cuadrado de saturación/brillo, una barra de tono, una barra de opacidad y un cuadro donde puede escribir o pegar un valor hexadecimal como `#1E4A6B`.

La pequeña pipeta situada a la derecha del título ‘Custom color’ toma un color **de cualquier lugar de la pantalla**, también fuera de QuizXpress. Haga clic en ella y la pantalla se congela; una lupa sigue el ratón y muestra los píxeles individuales con el color que hay bajo el cursor. Haga clic para tomar ese color, utilice las teclas de flecha para moverse un píxel cada vez (mantenga pulsada *Shift* para moverse diez) o pulse *Esc* para cancelar. Como la pantalla no tiene transparencia, se conserva la opacidad del color que tenía.

### Degradados

![](../../assets/images/properties-panel-gradient-presets.webp){ width="313" loading=lazy }

Una propiedad de degradado muestra una vista previa del degradado. Junto a ella hay un botón de paleta que abre un conjunto de **degradados predefinidos** listos para usar: con un solo clic, el fondo de una diapositiva o un cuadro de texto adquiere un aspecto acabado. Para conservar un degradado creado por usted, haga clic con el botón derecho en la propiedad de degradado y elija *Add to my gradients*; aparecerá entonces en **My gradients** en el selector (hasta cinco). Haga clic con el botón derecho en uno de sus propios degradados en el selector para eliminarlo de nuevo. Sus degradados se conservan entre sesiones.

### Restablecer, copiar y pegar

Haga clic con el botón derecho en cualquier propiedad para obtener:

- **Reset to default**: devuelve la propiedad al valor que tiene en una diapositiva nueva.
- **Copy value** y **Paste value**: útiles para pasar un color, una fuente o un degradado de un elemento a otro. *Ctrl+C* y *Ctrl+V* hacen lo mismo con la propiedad en la que está trabajando, de modo que puede copiar un color aquí y pegarlo directamente en otro programa como `#1E4A6B`, o al revés.

### Descripciones

![](../../assets/images/properties-panel-descriptions.webp){ width="333" loading=lazy }

Al pasar el ratón sobre el nombre de una propiedad se muestra una información sobre herramientas que explica lo que hace. Si prefiere tener esa explicación permanentemente a la vista, active *Show descriptions* en el menú de opciones: aparecerá entonces una barra en la parte inferior del panel con el nombre y la explicación de la propiedad sobre la que está el ratón.

### Opciones

![](../../assets/images/properties-panel-options-menu.webp){ width="333" loading=lazy }

El botón **…** de la esquina superior derecha del panel contiene los ajustes del propio panel: expandir y contraer todas las secciones, mostrar descripciones, el tema oscuro y el cambio a la cuadrícula de propiedades clásica.

### Tema oscuro

![](../../assets/images/properties-panel-dark-theme.webp){ width="333" loading=lazy }

*Dark theme* en el menú de opciones da al panel un esquema de colores oscuro, que cansa menos la vista cuando diseña diapositivas claras o trabaja en una habitación con poca luz. La elección se recuerda la próxima vez que inicie QuizXpress Studio y solo afecta al panel de propiedades.

## La cuadrícula de propiedades clásica

![](../../assets/images/image18.webp){ width="644" loading=lazy }

La cuadrícula que utilizaban las versiones anteriores de QuizXpress sigue estando disponible. Muestra todas las propiedades del elemento seleccionado en grupos alfabéticos y es la forma más rápida de verlo todo a la vez. Elija *Classic property grid* en el menú **…** del panel de propiedades para cambiar a ella, y el botón *Switch to the new properties panel* a la derecha de la propia barra de herramientas de la cuadrícula para volver. QuizXpress recuerda cuál de los dos prefiere.

## Propiedades de las diapositivas de quiz

Estas propiedades se muestran al hacer clic en el fondo de una pregunta. Las propiedades se dividen en diferentes grupos:

- *Appearance*, que define cómo se representa la pregunta.

- *Behavior*, que define el comportamiento de la pregunta durante el concurso.

- *General*, propiedades generales.

- *Metadata, metadatos de esta diapositiva (Id y Class)*

- *Points,* sección de asignación de puntos.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Propiedad</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Answer time</td>
<td>La duración de la cuenta atrás en segundos. Especifique un valor de 0 para una pregunta sin tiempo. Entonces puede finalizar la pregunta pulsando la barra espaciadora. La cuenta atrás se puede pausar pulsando ‘P’ en QuizXpress Live.</td>
</tr>
<tr class="even">
<td>Auto judge</td>
<td>Este ajuste es válido para una pregunta de dedo más rápido (Voting = no) y de opción múltiple. En este caso, el ajuste ‘Auto judge’ indica si QuizXpress Live juzgará automáticamente una pregunta cuando se pulse un botón de opción múltiple en un pulsador/mando (para los pulsadores que no son de opción múltiple, auto judge se establece siempre automáticamente en ‘No’).</td>
</tr>
<tr class="odd">
<td>Auto advance when media ends</td>
<td>Avanza automáticamente a la siguiente diapositiva cuando termina un vídeo o un sonido en una cartelera. Esto ayuda a crear quizzes que se ejecutan solos. Esta propiedad está disponible cuando hay un elemento multimedia en la diapositiva y cuando el Type de la diapositiva es billboard.</td>
</tr>
<tr class="even">
<td>Background image</td>
<td>La imagen de fondo de la diapositiva de quiz.</td>
</tr>
<tr class="odd">
<td>Background stretch mode</td>
<td>Indica cómo se estira la imagen de fondo en la diapositiva. Puede ser ‘Fill’, para llenar simplemente toda la diapositiva con la imagen (no se mantiene la relación de aspecto), o ‘Zoom’, para mantener la relación de aspecto correcta y posiblemente perder algunas partes de la imagen</td>
</tr>
<tr class="odd">
<td>Background video</td>
<td><p>Un vídeo que se reproduce detrás de la diapositiva durante el quiz. Una imagen o un vídeo en un marcador de posición se reproduce encima de él. Una vez establecido, debajo aparecen estos ajustes: <em>Video storage type</em> (incrustado o vinculado), <em>Linked file</em> (para un vídeo vinculado), <em>Loop</em> (activado de forma predeterminada), <em>Silent</em> (activado de forma predeterminada) y, en ‘More options’, <em>Sync with quiz</em> (pausar el vídeo cuando un equipo pulsa, la cuenta atrás se pausa o la pregunta termina).</p>
<p>En una categoría, el vídeo de fondo se aplica a cada diapositiva con el formato de esa categoría. Véase <a href="../../backgrounds/#video-de-fondo">Vídeo de fondo</a>.</p></td>
</tr>
<tr class="even">
<td>Bonus points</td>
<td>Los puntos de bonificación para el 1.º, 2.º y 3.º jugador más rápido en responder correctamente.</td>
</tr>
<tr class="odd">
<td>Class</td>
<td>Un texto definible por el usuario para clasificar el tipo de diapositiva. Estos datos se exportarán en el archivo de puntuaciones de Analyzer y se enviarán a MessageBroker para que puedan utilizarse para desencadenar un comportamiento concreto</td>
</tr>
<tr class="even">
<td>Category</td>
<td>La categoría de esta diapositiva de quiz. Al seleccionar una categoría, define el formato gráfico. Nota: ¡puede definir sus propias categorías! Para una explicación de las categorías, consulte la sección 3.3</td>
</tr>
<tr class="odd">
<td>Continue after correct answer</td>
<td>Cuando se da una respuesta correcta a una pregunta de dedo más rápido (de tipo ‘default’, la respuesta se da verbalmente y se juzga como correcta), la cuenta atrás continúa y los demás jugadores pueden pulsar (se utiliza a menudo para juegos durante un evento que se desarrolla fuera de un quiz).</td>
</tr>
<tr class="even">
<td>Correct answer</td>
<td>La respuesta correcta de esta diapositiva. Solo se aplica cuando el modo de entrada (véase más abajo) es ‘numeric’, ‘letter’ o ‘text’.</td>
</tr>
<tr class="odd">
<td>Custom HTML Screen</td>
<td>Una página HTML personalizada que se mostrará en los dispositivos móviles cuando se cargue esta diapositiva <em>(uso avanzado)</em></td>
</tr>
<tr class="even">
<td>Delay before answer</td>
<td>Tiempo en segundos que transcurrirá antes de que se muestren las respuestas. Esto da al presentador del quiz la posibilidad de leer la pregunta en voz alta antes de que se muestren las respuestas.</td>
</tr>
<tr class="odd">
<td>Delay between answers<sup>*</sup></td>
<td>Si se han establecido tanto ‘Delay before answer’ como ‘hide and show one by one’, aparece esta propiedad. Define el intervalo de tiempo que transcurrirá entre cada respuesta que aparezca.</td>
</tr>
<tr class="even">
<td>Demographic group<sup>*</sup></td>
<td>Esta propiedad se puede establecer cuando el <strong>Type</strong> de la diapositiva es ‘Demographic’. Define un grupo demográfico. Cuando se ejecute el quiz, las personas que pulsen su pulsador cuando se muestre una diapositiva de quiz demográfica pertenecerán al grupo indicado por esta propiedad. Consulte también la sección 5.4.5.5 para obtener más información sobre los grupos demográficos.</td>
</tr>
<tr class="odd">
<td>End of round action<sup>*</sup></td>
<td>Esta propiedad se puede establecer cuando el <strong>Type</strong> de la diapositiva es ‘End of round’. Sus valores posibles son ‘Disable one loser’, en cuyo caso se elimina al participante con menos puntos, y ‘Quizmaster selects losers’, en cuyo caso el presentador del quiz puede seleccionar a los participantes que se eliminarán, uno por uno.</td>
</tr>
<tr class="even">
<td>Evaluation mode</td>
<td>Indica si la evaluación de una respuesta numérica es ‘exact match’ (la respuesta dada debe coincidir exactamente con la respuesta correcta de la pregunta) o ‘nearest wins’ (el jugador que se acerque más a la respuesta gana los puntos indicados).</td>
</tr>
<tr class="odd">
<td>Gradient</td>
<td>El relleno degradado del fondo de la diapositiva. Esta propiedad solo se aplica si no hay ninguna imagen de fondo. Se pueden seleccionar un color ‘from’ y un color ‘to’ del degradado, así como un tipo de degradado.</td>
</tr>
<tr class="even">
<td>Id</td>
<td>Un ID único para identificar esta diapositiva (por ejemplo, para el enrutamiento estático de diapositivas con la propiedad <em>Next slide</em>)</td>
</tr>
<tr class="odd">
<td>Input type</td>
<td>Para una pregunta abierta puede elegir entre ‘default’ (pregunta de dedo más rápido) o una respuesta de tipo ‘number’, ‘letter’ o ‘text’. Estos tres últimos modos solo se aplican cuando se utilizan teléfonos móviles (ya que los mandos y los pulsadores no ofrecen entrada numérica ni de texto).</td>
</tr>
<tr class="even">
<td>Language</td>
<td>El idioma de visualización actual (de edición) de la diapositiva para quizzes bilingües.</td>
</tr>
<tr class="odd">
<td>Lock-out on wrong answer</td>
<td>Establece el modo de bloqueo para una pregunta de dedo más rápido. O bien el jugador queda bloqueado tras una respuesta incorrecta, o bien puede volver a intentarlo.</td>
</tr>
<tr class="even">
<td>Multiple correct answers</td>
<td>Indica si esta pregunta tiene más de una respuesta correcta y si las respuestas correctas múltiples siguen un orden específico</td>
</tr>
<tr class="odd">
<td>Mute countdown sound</td>
<td>Silencia el sonido de la cuenta atrás para esta pregunta</td>
</tr>
<tr class="even">
<td>Next slide</td>
<td>El ID de la diapositiva que se mostrará después de esta (enrutamiento estático de diapositivas)</td>
</tr>
<tr class="odd">
<td>Notes</td>
<td>Un texto (pistas) para el presentador del quiz que se incluirá en la exportación a PDF</td>
</tr>
<tr class="even">
<td>Ordered answer mode</td>
<td>Para las respuestas ordenadas, puede indicar si desea que las respuestas coincidan exactamente con el orden (Exact match) o si una respuesta parcialmente correcta también da puntos (un porcentaje de los puntos, según cuántas de las respuestas estén en el lugar correcto).</td>
</tr>
<tr class="odd">
<td>Penalty points end</td>
<td>Número de puntos que se restan cuando un participante responde incorrectamente al final de la cuenta atrás (interpola entre inicio y final)</td>
</tr>
<tr class="even">
<td>Penalty points start</td>
<td>Número de puntos que se restan cuando un participante responde incorrectamente al inicio de la cuenta atrás</td>
</tr>
<tr class="odd">
<td>Points at end</td>
<td>Número de puntos que se suman cuando un participante responde correctamente al final de la cuenta atrás. Debe ser menor o igual que ‘points at start time’. Los puntos se interpolan entre el inicio y el final del contador. Así, cuando los puntos al final son menores que los puntos al inicio, el número de puntos que se pueden ganar disminuye mientras la cuenta atrás está en marcha. Cuando los dos valores son iguales, los puntos que se pueden ganar se mantienen iguales durante toda la cuenta atrás.</td>
</tr>
<tr class="even">
<td>Points at start</td>
<td>Número de puntos que se suman cuando un participante responde correctamente al inicio de la cuenta atrás.</td>
</tr>
<tr class="odd">
<td>Points to lose on no answer</td>
<td>Los puntos que se restan cuando no se da ninguna respuesta (solo aplicable a las preguntas de votación)</td>
</tr>
<tr class="even">
<td>Steal Points</td>
<td>Cuando la opción de robar puntos está activa en una pregunta de dedo más rápido (pulsador), un jugador que da una respuesta incorrecta no pierde puntos. En su lugar, los puntos de penalización configurados para la diapositiva se otorgan a todos los demás jugadores y la pregunta termina de inmediato.</td>
</tr>
<tr class="odd">
<td>Response limit</td>
<td>El número máximo de equipos de los que el sistema aceptará respuestas. Por ejemplo, si juega con 100 equipos, puede establecer este valor en 25 para que solo los primeros 25 equipos puedan responder a la pregunta.</td>
</tr>
<tr class="even">
<td>Response mode</td>
<td>Indica si esta pregunta acepta solo una respuesta por jugador o varias (se utiliza en combinación con ‘Multiple correct answers’). Al establecer esta opción en ‘multiple responses, exact match’, la respuesta múltiple debe coincidir exactamente con las respuestas correctas para ganar puntos.</td>
</tr>
<tr class="odd">
<td>Revise answer</td>
<td>Aquí puede anular la opción global que permite a los jugadores revisar su respuesta (establecida globalmente en Quiz Setup para todas las diapositivas).</td>
</tr>
<tr class="even">
<td>Safety net<sup>*</sup></td>
<td>Se utiliza para las preguntas de la escalera de trivial. En una ronda de escalera de trivial, cuando un jugador responde incorrectamente, retrocede hasta la red de seguridad más cercana de la escalera de trivial.</td>
</tr>
<tr class="odd">
<td>Script</td>
<td>Comportamiento personalizado de la diapositiva programado en JavaScript <em>(uso avanzado)</em></td>
</tr>
<tr class="even">
<td>Show answers action<sup>*</sup></td>
<td>Cuando se ha establecido ‘Delay before answer’, aparece esta propiedad. Al establecerla en ‘hide and show at once’, las respuestas se muestran de una vez cuando ha transcurrido el tiempo de retraso. Al establecerla en ‘hide and show one by one’, las respuestas se muestran una por una cuando ha transcurrido el tiempo de retraso.</td>
</tr>
<tr class="odd">
<td>Show correct answer</td>
<td>Modo de mostrar la respuesta correcta en esta diapositiva. Puede seguir el ajuste global indicado en Quiz Setup, no mostrar nunca la respuesta correcta o mostrarla siempre.</td>
</tr>
<tr class="even">
<td>Shuffle mode</td>
<td>Determina lo que ocurre cuando se mezcla el quiz</td>
</tr>
<tr class="odd">
<td>Start timer</td>
<td>Indica si el temporizador de cuenta atrás debe iniciarse automáticamente cuando aparece la pregunta o mediante una acción manual.</td>
</tr>
<tr class="even">
<td>Steal points</td>
<td>Aplicable a las preguntas de dedo más rápido. Cuando está activado, todos los demás jugadores roban los puntos al jugador que pulsó cuando la respuesta dada es incorrecta.</td>
</tr>
<tr class="odd">
<td>Style</td>
<td>El estilo de representación de la pregunta. Encontrará más información sobre los estilos en el capítulo “Styles”.</td>
</tr>
<tr class="even">
<td>Text evaluation</td>
<td>Indica si la evaluación de una respuesta de texto es ‘exact match’ (la respuesta dada debe coincidir exactamente con la respuesta correcta) o ‘fuzzy match’ (un algoritmo permite un cierto porcentaje de diferencia entre la respuesta dada y la respuesta correcta, de modo que los jugadores pueden cometer pequeños errores ortográficos).</td>
</tr>
<tr class="odd">
<td>Tolerance</td>
<td>Variación permitida entre la respuesta correcta y las respuestas dadas. Se aplica a las preguntas con input type ‘text’ y ‘text evaluation’ establecido en ‘fuzzy match’.</td>
</tr>
<tr class="even">
<td>Topic<sup>*</sup></td>
<td>El tema de la pregunta. Se utiliza para generar automáticamente un Trivia Board anterior.</td>
</tr>
<tr class="odd">
<td>Transition</td>
<td>La animación de transición específica al pasar a la siguiente diapositiva (de forma predeterminada, el sistema selecciona una transición aleatoria)</td>
</tr>
<tr class="even">
<td>Type</td>
<td><p>Campo de solo visualización que muestra el tipo de la diapositiva:</p>
<ul>
<li><p><em>Question</em>: la diapositiva es una pregunta de quiz normal.</p></li>
<li><p><em>Billboard</em>: la diapositiva es solo de visualización.</p></li>
<li><p><em>End of round</em>: la diapositiva indica el final de una ronda del quiz. Se muestran las puntuaciones intermedias y el presentador del quiz tiene la opción de eliminar equipos. Consulte también la propiedad: ‘End of Round’.</p></li>
<li><p><em>Test question</em>: diapositiva utilizada para demostrar el sistema a los participantes. No se suman ni se restan puntos.</p></li>
<li><p><em>Demographic</em>: esta diapositiva sirve para dividir a todos los participantes en grupos que compiten entre sí. Consulte también la propiedad ‘Demographic group’.</p></li>
<li><p><em>Last Man Standing</em>: la diapositiva es una pregunta de quiz. Los participantes que respondan incorrectamente a la pregunta son eliminados del quiz.</p></li>
<li><p><em>Audience Response</em>: diapositiva para recoger simplemente una respuesta del público sin cambiar ninguna puntuación del quiz. Los datos de respuesta se pueden mostrar en un gráfico.</p></li>
<li><p><em>Wager</em>: permite al público apostar un porcentaje de sus puntuaciones en la pregunta siguiente.</p></li>
<li><p><em>Majority Rules</em>: una diapositiva en la que la respuesta correcta depende de la opción elegida por la mayoría del público</p></li>
<li><p><em>Minigame</em>: una diapositiva que inicia el minijuego seleccionado</p></li>
<li><p><em>Trivia Board</em>: una diapositiva que inicia una ronda en la que las preguntas se organizan por Topic/Points y se presentan como una cuadrícula</p></li>
<li><p><em>Trivia Ladder:</em> inicia una ronda de Trivia Ladder en la que los jugadores suben por la escalera con cada pregunta correcta</p></li>
<li><p><em>Speed Round:</em> inicia una ronda en la que un jugador debe responder a tantas preguntas como pueda en un tiempo fijo.</p></li>
<li><p><em>Trivia Bingo:</em> inicia una ronda de Bingo, ya sea construida a partir de diapositivas de quiz consecutivas o como un juego de Bingo de números tradicional.</p></li>
<li><p><em>Trivia Feud:</em> una diapositiva en la que los jugadores responden a una pregunta de tipo encuesta.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Voting</td>
<td>Indica si todos los participantes pueden responder o si solo puede responder el participante que pulsa primero.</td>
</tr>
</tbody>
</table>
<p><sup>* la visibilidad de la propiedad depende de otras propiedades</sup></p></td>
</tr>
</tbody>
</table>

## Propiedades de la pregunta

Estas propiedades se muestran al hacer clic en el cuadro de la pregunta de una diapositiva

| Propiedad               | Descripción                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------------------|
| Alignment               | La alineación del texto de la pregunta                                                                         |
| Drop shadow             | Indica si se aplica una sombra debajo del texto de la pregunta                                                 |
| Gradient                | El relleno degradado del fondo de la pregunta.                                                                 |
| Shadow color            | Indica el color de la sombra                                                                                   |
| Text                    | El texto de la pregunta                                                                                        |
| Text Color              | El color del texto de la pregunta                                                                              |
| Text font               | La fuente utilizada para el texto de la pregunta                                                               |
| Text reveal animation   | Cómo se revela el texto. Show (predeterminado: se muestra directamente), Show letter by letter o Show word by word |
| Text reveal delay (sec) | El retraso tras el cual se muestra el texto                                                                    |
| Text reveal speed       | Velocidad de la revelación del texto                                                                           |
| Transparency            | Transparencia del fondo de la pregunta                                                                         |

## Propiedades de las respuestas

Estas propiedades se muestran al hacer clic en un cuadro de respuesta de una diapositiva

| Propiedad               | Descripción |                                                                                                                                                       |
|-------------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Alignment               |             | La alineación del texto de la respuesta                                                                                                               |
| Correct answer          |             | Indica si la respuesta seleccionada es la respuesta correcta. Establézcalo en ‘true’ si la respuesta seleccionada es la respuesta correcta.          |
| Correctness             |             | Aplicable a las preguntas con varias respuestas correctas, este valor establece la corrección (como porcentaje de los puntos totales de la pregunta) de la respuesta. |
| Drop shadow             |             | Indica si se aplica una sombra debajo del texto de la pregunta                                                                                        |
| Gradient                |             | El relleno degradado del fondo de la pregunta. Que esta propiedad sea aplicable depende del estilo utilizado.                                         |
| Shadow color            |             | El color de la sombra                                                                                                                                 |
| Text                    |             | El texto de la respuesta                                                                                                                              |
| Text reveal animation   |             | Cómo se revela el texto. Show (predeterminado: se muestra directamente), Show letter by letter o Show word by word                                    |
| Text reveal delay (sec) |             | El retraso tras el cual se muestra el texto                                                                                                           |
| Text reveal speed       |             | Velocidad de la revelación del texto                                                                                                                  |
| Text color              |             | El color del texto de la respuesta                                                                                                                    |
| Text font               |             | La fuente del texto de la respuesta                                                                                                                   |
| Transparency            |             | Transparencia del fondo del panel de respuesta                                                                                                        |

## Propiedades de las imágenes

Estas propiedades se muestran al hacer clic en un cuadro de imagen de una diapositiva

| Propiedad           | Descripción |
|---------------------|-------------|
| Border              | Indica si se dibuja un borde alrededor de la imagen |
| Border color        | El color del borde, cuando está activado |
| Border thickness    | Grosor en píxeles del borde (cuando está activado) |
| Corner radius       | Radio de las esquinas de la línea del borde para crear un borde redondeado |
| Correct answer      | Indica si la imagen contiene la respuesta correcta. Solo se puede establecer para imágenes cuando la diapositiva contiene únicamente imágenes y es una diapositiva de opción múltiple. |
| Drop shadow         | Indica si se aplica una sombra debajo de la imagen |
| Effect              | Establece un efecto en la imagen. Consulte [Recorte](../adding-multimedia-content/pictures.md#recortar) para obtener una explicación más detallada sobre los efectos. |
| Hidden              | Oculta la imagen durante el quiz |
| Hidden on mobile    | Indica si una imagen mostrada en una diapositiva de quiz debe ocultarse en el teléfono móvil. Un escenario para utilizarlo es cuando desea mostrar una imagen diferente en el teléfono móvil que en la pantalla grande para el público. Por ejemplo, puede que desee que la imagen del móvil tenga una relación de aspecto diferente. En ese caso, no desea que la imagen mostrada en la pantalla grande aparezca también en el teléfono móvil. |
| Image               | Una miniatura de la imagen. Haga clic en el botón de exploración (…) de esta propiedad para buscar una imagen. |
| Inflate             | Determina si la imagen debe llenar toda el área ampliándola |
| Label               | Una descripción textual de la imagen (se utiliza cuando no se puede mostrar la imagen) |
| Mobile device image | Una versión alternativa de la imagen que se utilizará en dispositivos móviles |
| Stretch             | Estira la imagen en ambas direcciones para llenar el área (puede deformar la imagen) |

## Propiedades del sonido

Estas propiedades se muestran al hacer clic en un elemento de sonido de una diapositiva

| Propiedad               | Descripción |
|-------------------------|-------------|
| Duration                | La duración del sonido. Inicialmente se muestra la duración completa. |
| Intro pause             | El tiempo de espera antes de que comience el sonido. Esto da al presentador del quiz la posibilidad de leer primero la pregunta. |
| Keep playing            | De forma predeterminada, la música que pone en una diapositiva se detiene cuando termina el temporizador de cuenta atrás. Con esta opción, puede dejar que la música suene hasta que pase a la siguiente diapositiva. |
| Pitch                   | El tono al inicio de la cuenta atrás |
| Remove vocals           | Efecto para eliminar las voces (puede dar resultados desiguales) |
| Repeat                  | Indica si el sonido debe repetirse. |
| Replay                  | Reproduce de nuevo el sonido después de que se haya revelado la respuesta correcta en la pregunta. |
| Replay delay            | Se muestra cuando replay está activado. Muestra el número de segundos tras los cuales comienza la repetición |
| Replay start            | Establece el momento en que comenzará a reproducirse el fragmento de sonido |
| Replay end              | Establece el momento en que dejará de reproducirse el fragmento de sonido |
| Reverse audio           | Reproduce el fragmento de sonido al revés |
| Sound Storage Type      | Indica si los datos del sonido se almacenan incrustados en el archivo del quiz o en el disco local (vinculado) |
| Speed percentage        | La velocidad del sonido cuando empieza a reproducirse. |
| Start at                | La posición del archivo de sonido desde la que se iniciará el sonido. |
| Stop at                 | El momento en que se detiene el sonido |
| Target Pitch            | El tono al final de la cuenta atrás (el tono se interpolará del inicio al final) |
| Target speed percentage | La velocidad del sonido cuando termina de reproducirse. Nota: jugando con el ‘speed percentage’ y el ‘target speed percentage’ es posible reproducir sonidos ‘de lento a normal’ o ‘de rápido a normal’. Si se establecen ambos porcentajes en 100 %, el fragmento de sonido simplemente se reproduce de principio a fin a velocidad normal. |
| Volume                  | El volumen al que se reproduce la música |
| Volume fade             | Fundido de entrada/salida al iniciar/detener la música |

## Propiedades de los minijuegos

| Propiedad      | Descripción |
|----------------|-------------|
| Minigame title | De forma predeterminada, el pulsador móvil muestra en pantalla el nombre del minijuego. Puede anularlo y proporcionar su propio texto. Así, en lugar de ver “Horse race”, puede mostrar algo más emocionante. |

## Propiedades del vídeo

Estas propiedades se muestran al hacer clic en un vídeo de una diapositiva

| Propiedad                      | Descripción |
|--------------------------------|-------------|
| Aspect Ratio                   | (solo lectura) relación de aspecto |
| Codec                          | (solo lectura) decodificador de vídeo que se está utilizando |
| Duration                       | (solo lectura) duración del vídeo |
| Effect                         | Efecto opcional en el vídeo |
| End                            | Momento en que termina el vídeo |
| Intro Pause                    | Retraso entre la visualización de la diapositiva y el inicio del vídeo |
| Linked File                    | Nombre del archivo de vídeo externo, si está vinculado |
| Loop                           | Repite el vídeo después de que se haya detenido |
| Replay                         | Reproduce de nuevo el vídeo después de que se haya revelado la respuesta correcta en la pregunta. |
| Replay delay                   | El número de segundos tras los cuales comienza la repetición |
| Replay start                   | Establece el momento de reproducción en que comenzará el vídeo |
| Replay end                     | Establece el momento de reproducción en que terminará el vídeo |
| Silent                         | Suprime el sonido del vídeo |
| Start                          | Momento en que empieza el vídeo |
| Video Height                   | (solo lectura) altura del vídeo |
| Video storage type             | Indica si el fragmento de vídeo está incrustado o vinculado. Incrustar un fragmento de vídeo en un quiz significa que el fragmento de vídeo se incorpora al archivo del quiz. Vincular un fragmento de vídeo significa que se establece una referencia desde el archivo del quiz a un vídeo del sistema de archivos. En general, se recomienda vincular los vídeos. *Nota: al vincular vídeos, asegúrese de no eliminar los archivos de vídeo de su sistema de archivos. Al trasladar el quiz a otro ordenador, los vídeos deben copiarse en la misma carpeta que el archivo del quiz.* |
| (read-only) width of the video | (solo lectura) anchura del vídeo |

## Propiedades de las formas

Estas propiedades se muestran al hacer clic en una forma de imagen o una forma de texto de una diapositiva.

| Propiedad               | Descripción |
|-------------------------|-------------|
| Alignment               | La alineación del texto de la forma de texto |
| Background transparency | Aplicable a las formas de texto. Establece la transparencia del color utilizado para el fondo (la propiedad Gradient). |
| Border color            | El color del borde de una forma de texto |
| Border width            | El ancho del borde de una forma de texto |
| Corner radius           | El radio del borde de una forma de texto. Permite crear esquinas redondeadas. |
| Drop shadow             | Indica si se utiliza una sombra para una forma de texto |
| Gradient                | El relleno degradado del fondo de una forma de texto. Se pueden seleccionar un color ‘from’ y un color ‘to’ del degradado, así como un tipo de degradado. |
| Picture                 | Aplicable a las formas de imagen. Una miniatura de la imagen. Haga clic en el botón de exploración (…) para buscar una imagen. |
| Rotation Angle          | El ángulo de rotación de la imagen o del texto |
| Shadow color            | Color de la sombra de una forma de texto |
| Stretch                 | Aplicable a las formas de imagen. Estira la imagen para cubrir toda el área del cuadro de selección que la rodea |
| Text                    | El texto de la forma de texto |
| Text color              | El color del texto de una forma de texto |
| Text font               | La fuente utilizada para la forma de texto |
| Transparency            | Establece la transparencia de la imagen o del texto |
| Visibility              | Indica si una forma (ya sea una imagen o un texto) está siempre visible, se hace visible cuando se revela una respuesta, se oculta cuando se revela una respuesta o es temporizada (aparece en un momento determinado durante la cuenta atrás). |

## Propiedades del habla

Estas propiedades se muestran al hacer clic en un elemento de habla de una diapositiva.

| Propiedad | Descripción                                                              |
|-----------|--------------------------------------------------------------------------|
| PreRoll   | Indica el número de segundos de espera antes de que comience el habla    |
| Rate      | La velocidad a la que se lee el texto del elemento de habla              |
| Text      | El texto que se va a leer                                                |
| Voice     | La voz que se va a utilizar (elija una de las voces instaladas en Windows) |
| Volume    | El volumen del texto hablado                                             |

## Propiedades del gráfico

Estas propiedades se muestran al hacer clic en un gráfico de una diapositiva

| Propiedad           | Descripción |
|---------------------|-------------|
| Alignment           | Alineación del título del gráfico |
| Area background     | Establece el color de fondo del área de datos del gráfico |
| Axis color          | El color utilizado para el eje |
| Axis label autosize | Establece automáticamente el tamaño de las etiquetas del eje. Si no está activado, puede elegir explícitamente una fuente y un tamaño para las etiquetas |
| Axis label color    | El color utilizado para las etiquetas del eje |
| Chart background    | Establece el color de fondo del área exterior a los datos del gráfico |
| Chart type          | El tipo de gráfico. Elija entre Bar, Column, Doughnut o Pie. |
| Corner radius       | Radio de las esquinas del elemento del gráfico |
| Dropshadow offset   | Muestra una sombra para el área de datos del gráfico |
| Grid color          | El color utilizado para la cuadrícula en el área de datos del gráfico |
| Label color         | Color de las etiquetas mostradas para cada elemento del gráfico |
| Label display mode  | Para las etiquetas, muestra valores absolutos, porcentajes o ambos |
| Label font          | Fuente de las etiquetas |
| Label style         | Indica dónde colocar las etiquetas |
| Mode                | Indica el tipo de datos que se muestra en el gráfico: response (porcentaje de cada respuesta dada) o right/wrong (porcentaje de jugadores que acertaron/fallaron) |
| Show 3D             | Muestra una representación en 3D del gráfico |
| Show legend         | Muestra una leyenda para los datos del gráfico (porcentaje de respuestas de cada respuesta) |
| Title               | Título del gráfico |
| Title color         | Color del título del gráfico |
| Title font          | Fuente del título del gráfico |
| Visibility          | Indica si el gráfico está siempre visible (con actualizaciones en directo durante la cuenta atrás) o solo después de que se cierre la pregunta |

## Propiedades del juego de palabras

Estas propiedades se muestran al hacer clic en un juego de palabras de una diapositiva

| Propiedad              | Descripción |
|------------------------|-------------|
| Alignment              | Alineación del texto |
| Background fill        | El relleno degradado del fondo del juego de palabras. Se pueden seleccionar un color ‘from’ y un color ‘to’ del degradado, así como un tipo de degradado. |
| Center index           | Para un juego de rueda de palabras, indica la letra que aparece en el centro |
| Drop shadow            | Indica si se utiliza una sombra para las letras del juego de palabras |
| End reveal at          | Porcentaje del tiempo de cuenta atrás en que termina la revelación |
| Font                   | La fuente utilizada para el texto |
| Interval               | Para los juegos de palabras de desordenar y de revelar, controla el tiempo entre los pasos del juego: lineal, ralentizándose o ralentizándose mucho. |
| Layout                 | Para los juegos de palabras de revelar o desordenar: cuadrícula de letras dinámica o cuadrícula de letras fija con 52 celdas. |
| Letter background fill | El relleno degradado del fondo de los cuadros de letras del juego de palabras. Se pueden seleccionar un color ‘from’ y un color ‘to’ del degradado, así como un tipo de degradado. |
| Letter corner radius   | Radio de las esquinas del juego de palabras |
| Letter spacing         | Espacio entre las letras del juego de palabras |
| Manual control         | Indica si las letras se revelan automáticamente o si las revela manualmente el presentador del quiz desde QuizXpress Director |
| Padding                | Relleno alrededor de las letras de la cuadrícula |
| Reverse                | Para un juego de rueda de palabras, invierte la dirección de las letras |
| Shadow color           | Color de la sombra de las letras |
| Spin                   | Hace girar las letras de la rueda de palabras para un desafío adicional |
| Start angle            | Para un juego de rueda de palabras, el ángulo inicial donde aparece la primera letra de la palabra |
| Start reveal at        | Porcentaje del tiempo de cuenta atrás en que comienza la revelación |
| Text                   | El texto del juego de palabras |
| Text color             | El color del texto |
| Text transparency      | La transparencia del texto |

## Propiedades de Trivia Board

Estas propiedades se muestran cuando se selecciona un trivia board. Las propiedades marcadas con *Custom* solo se muestran cuando 'Board position' es Custom; consulte [Diseño de su propio tablero](../slide-and-game-formats/trivia-board-round.md#disenar-su-propio-tablero).

| Propiedad                         | Descripción |
|-----------------------------------|-------------|
| Auto select                       | Selecciona automáticamente un recuadro aleatorio, con una animación, cuando se selecciona el tablero |
| Animation duration (sec)          | Duración en segundos de la animación de selección aleatoria |
| Animation interval (sec)          | Intervalo entre los cambios de selección durante la animación de selección aleatoria |
| Background color (Topic Tiles)    | Establece el color de fondo de los recuadros de tema |
| Background color (Question Tiles) | Establece el color de fondo de los recuadros de pregunta |
| Board position                    | Automatic llena la pantalla (el tablero clásico). Custom coloca el tablero donde está en la diapositiva, de modo que puede moverlo y cambiar su tamaño para adaptarlo a su fondo |
| Circular tiles (Topic tiles)      | Hace circulares los recuadros (de forma predeterminada son rectangulares) |
| Column spacing                    | El espacio entre las columnas de recuadros |
| Effect color                      | El color de la sombra o del contorno del texto |
| Font (Topic Tiles)                | Establece la fuente de los recuadros de tema |
| Font (Question Tiles)             | Establece la fuente de los recuadros de pregunta |
| Highlight color                   | El color de la selección aleatoria |
| Image position (Topic Tiles)      | *Custom.* Dónde va la imagen del tema: sobre todo el recuadro, o a la izquierda, a la derecha o encima del nombre del tema |
| Image scaling                     | *Custom.* Cómo se ajusta la imagen de un recuadro al recuadro: Stretch, Fit, Fill o Keep corners |
| Max. questions to play            | El número máximo de preguntas que se jugarán o 0 para todas las preguntas |
| Played tiles                      | Aspecto de un recuadro una vez que se han jugado todas sus preguntas: Dimmed, Hidden o No text |
| Randomize questions               | Si hay varias preguntas vinculadas a un recuadro, se seleccionará una al azar. Sin embargo, si la opción ‘Randomize questions’ no está activada, las preguntas detrás del recuadro se presentarán en el orden en que aparecen en el quiz. |
| Row spacing                       | El espacio entre las filas de recuadros |
| Same text size for all tiles      | Un tamaño de texto para todos los nombres de tema y uno para todos los valores de puntos, nunca mayor que el tamaño de la fuente; los nombres de tema largos se ajustan en dos líneas. Cuando está desactivado, cada texto llena su propio recuadro |
| Selection highlight               | Cómo muestra un recuadro la selección aleatoria: Fill, Tint, Outline o Glow |
| Show topic name (Topic Tiles)     | *Custom.* Muestra el nombre del tema en el recuadro; desactívelo cuando las imágenes de los temas ya contengan el nombre |
| Text color (Question Tiles)       | Establece el color del texto de los recuadros de pregunta |
| Text color (Topic Tiles)          | Establece el color del texto de los recuadros de tema |
| Text effect                       | Una sombra o un contorno alrededor del texto de los recuadros |
| Tile image                        | *Custom.* Una imagen para los recuadros de tema o los recuadros de pregunta, en lugar del color de fondo |
| Topic images (Topic Tiles)        | *Custom.* Una imagen distinta para cada tema del tablero |
| Topic row height                  | La altura de la fila de temas en comparación con una fila de recuadros de pregunta |
| Topics only                       | Muestra solo los temas en el tablero |
| Vary tiles (Question Tiles)       | *Custom.* Refleja la imagen del recuadro de forma distinta en cada recuadro |

## Propiedades de Trivia Ladder

Estas propiedades se muestran cuando se selecciona una diapositiva de Trivia Ladder.

| Propiedad               | Descripción |
|-------------------------|-------------|
| Background color        | Establece el color de fondo de la escalera de trivial |
| Background image        | Establece la imagen de fondo de la escalera |
| Background stretch mode | Modo de estiramiento de la imagen de fondo |
| Border color            | Establece el color del borde de la escalera de trivial |
| Display mode            | Dónde mostrar la escalera en la pantalla: deslizarse desde la derecha de la pantalla, deslizarse hasta el centro de la pantalla, mostrarse a pantalla completa o mostrarse siempre (en el lado derecho de la pantalla). |
| Keypads color           | Establece el color de los mandos |
| Safety net color        | Establece el color de los peldaños de la red de seguridad |
| Separator color         | Establece el color de los separadores |
| Show border             | Muestra el borde de la escalera de trivial |
| Step color              | Establece el color de los peldaños |
| Wrong answer action     | Indica qué hacer cuando un jugador responde incorrectamente: bajar un peldaño, permanecer en el mismo peldaño, reiniciar en la escalera o retroceder hasta la red de seguridad más cercana. |

## Propiedades de Bingo

Al configurar su juego de Bingo, están disponibles las siguientes propiedades:

| Propiedad                   | Descripción |
|-----------------------------|-------------|
| Auto advance after claim    | Cuando se gestiona una reclamación en pantalla y esa opción está activada, el juego continuará automáticamente tras la reclamación. Si no, el juego espera a que el presentador pulse Next. |
| Blanks per row              | El número de celdas en blanco por fila del cartón de bingo. Se puede utilizar para acelerar el juego |
| Center Image                | La imagen central (de bonificación) que aparecerá en el cartón de Bingo móvil |
| Claims mode                 | Indica si solo se gestiona al primer jugador que reclama bingo o a todos los jugadores |
| Countdown time (sec)        | El tiempo de cuenta atrás al gestionar una reclamación de bingo en pantalla. |
| Enable Virtual Caller       | Activa el sintetizador de voz de Windows para cantar las bolas/colores en un juego de Bingo normal |
| False Bingo handling        | Cómo se gestionan los bingos falsos (delante del público o en silencio) |
| False Bingo limit           | Cuántas veces puede un jugador reclamar un bingo antes de ser excluido |
| False Bingo mode            | Qué ocurre cuando un jugador reclama un Bingo falso |
| First Pattern…Fifth Pattern | Los patrones por los que se juega (se pueden jugar hasta 5 patrones en una ronda) |
| Game Type                   | Trivia Bingo, Number (traditional) Bingo o Emoji Bingo. |
| Pattern penalty points      | Los puntos que se pierden por un bingo falso (por patrón) |
| Pattern Points              | Los puntos que se ganan por un bingo válido (por patrón) |
| Randomize questions         | Al jugar a Trivia Bingo, esta opción indica que las preguntas se juegan en orden aleatorio |
| Say Colors                  | Dice los colores de las columnas junto con los números (por ejemplo, ‘Blue 4’) |

## Propiedades de Trivia Feud

Al configurar una diapositiva de Trivia Feud, están disponibles las siguientes propiedades:

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>Propiedad</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Auto scale text</td>
<td>Escala el texto de las respuestas para que quepan en los cuadros (da como resultado distintos tamaños de fuente para las respuestas)</td>
</tr>
<tr class="even">
<td>Drop shadow</td>
<td>Añade una sombra a los textos de las respuestas</td>
</tr>
<tr class="odd">
<td>Leading zeros</td>
<td>Muestra ceros a la izquierda en las puntuaciones de la encuesta</td>
</tr>
<tr class="even">
<td>Question font</td>
<td>Fuente de la pregunta de la encuesta</td>
</tr>
<tr class="odd">
<td>Question text color</td>
<td>Color de la pregunta de la encuesta</td>
</tr>
<tr class="even">
<td>Show light grid</td>
<td>Muestra la cuadrícula luminosa en el fondo</td>
</tr>
<tr class="odd">
<td>Survey</td>
<td>Edita las respuestas de la encuesta</td>
</tr>
<tr class="even">
<td>Survey question</td>
<td>Edita las preguntas de la encuesta</td>
</tr>
<tr class="odd">
<td>Survey text alignment</td>
<td>Alineación del texto de la encuesta</td>
</tr>
<tr class="even">
<td>Survey text color</td>
<td>Color de las respuestas de la encuesta</td>
</tr>
<tr class="odd">
<td>Game mode</td>
<td>Manual, Fastest Finger, Multiplayer</td>
</tr>
<tr class="even">
<td>Hide survey question</td>
<td>Oculta la pregunta de la encuesta (el presentador del quiz prefiere leerla en voz alta)</td>
</tr>
<tr class="odd">
<td>Max correct answers</td>
<td>El número máximo de respuestas correctas que puede dar un jugador (solo dedo más rápido).</td>
</tr>
<tr class="even">
<td>Max incorrect answers</td>
<td><p>El número máximo de respuestas incorrectas que puede dar un jugador antes de que se reanude la cuenta atrás (modo de dedo más rápido)</p>
<p>El número máximo de respuestas incorrectas antes de que el turno pase al otro equipo (modo manual)</p></td>
</tr>
<tr class="odd">
<td>Penalty points</td>
<td>El número de puntos de penalización cuando una respuesta dada es incorrecta (modo de dedo más rápido)</td>
</tr>
<tr class="even">
<td>Points multiplier</td>
<td>Aplica un multiplicador de 2 o 3 a las respuestas de la encuesta para que un jugador pueda ganar 2 o 3 veces más puntos</td>
</tr>
<tr class="odd">
<td>Reveal order</td>
<td>El orden en que se revelan los paneles restantes (‘first to last’ o ‘last to first’)</td>
</tr>
<tr class="even">
<td>Reveal delay (ms)</td>
<td>El retraso en milisegundos entre la revelación de cada respuesta de la encuesta. Permite al presentador leer las respuestas una por una mientras se muestran.</td>
</tr>
<tr class="odd">
<td>Wrong answer mode</td>
<td>Cuando un jugador ha dado un número de respuestas incorrectas definido en ‘max incorrect answers’, indique con este modo si el jugador queda excluido de esta pregunta o puede volver a pulsar (continuar) (modo de dedo más rápido)</td>
</tr>
</tbody>
</table>
