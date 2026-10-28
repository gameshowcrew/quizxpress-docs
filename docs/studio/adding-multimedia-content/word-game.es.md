# Word Game

Un elemento Word Game es un elemento gráfico para crear preguntas basadas en palabras y frases. Al insertar un Word Game, aparece la siguiente ventana:

![](../../assets/images/image221.webp){ width="320" loading=lazy }.

Aquí introduce el texto que se mostrará y selecciona el tipo de juego y las opciones asociadas.

Hay cuatro juegos distintos:

| *Word Reveal* (aquí en formato de cuadrícula fija de 52 letras). Las letras aparecen con el tiempo, a partir de una cuadrícula vacía | ![](../../assets/images/image222.webp){ width="279" loading=lazy } |
|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| *Word Scramble* (anagrama). La palabra o frase se va ordenando con el tiempo                                                   | ![](../../assets/images/image223.webp){ width="388" loading=lazy } |
| *Letter Grid. Las palabras están ocultas en una cuadrícula de letras aleatoria. Cuando termina la pregunta, las palabras se resaltan.* | ![](../../assets/images/image224.webp){ width="122" loading=lazy }  |
| *Word Wheel. La palabra se presenta como una rueda (opcionalmente giratoria). Se quita una letra al azar y se coloca en el centro.* | ![](../../assets/images/image225.webp){ width="126" loading=lazy } |

Tanto Word Reveal como Word Scramble pueden presentarse visualmente como una cuadrícula normal de varias líneas (cuadrícula de letras dinámica) o en un tablero fijo de 52 casillas (como el del programa de televisión La Ruleta de la Fortuna©). Tenga en cuenta que, en estos dos elementos, le corresponde a usted dividir la frase en varias líneas pulsando Intro para pasar a la línea siguiente.

Con Word Reveal puede elegir controlar manualmente la revelación desde QuizXpress Director. Al ejecutar un quiz, en cuanto se muestra la diapositiva aparece la pestaña 'Reveal Word Game' en QuizXpress Director. Allí puede revelar manualmente una letra que mencione un jugador pulsando el botón correspondiente, o bien revelar una vocal, una consonante, una palabra o la frase completa (all).

Si la letra forma parte de la frase, se revela en el reproductor de quiz. Tras pulsar una letra, Director también indica si está en la frase (letra verde) o no (letra roja).

![](../../assets/images/image226.webp){ loading=lazy }

Si un jugador intenta adivinar la palabra, puede juzgarlo pulsando el botón de correcto o incorrecto, tras lo cual aparece en la pantalla del reproductor de quiz, para el público, una gran marca verde o una cruz roja.

El reproductor de quiz muestra la cuadrícula de letras con las letras reveladas. También puede mostrar un resumen de las letras que aún no se han elegido (activando la opción 'Show alphabet strip' en las propiedades avanzadas de QuizXpress Studio).

![](../../assets/images/image227.webp){ loading=lazy }

El modo manual también permite comprar vocales y ganar o perder puntos al adivinar consonantes. Los ajustes de puntuación de vocales y consonantes se pueden configurar en QuizXpress Studio después de seleccionar el elemento Word Game en la diapositiva.

![](../../assets/images/image228.webp){ width="359" loading=lazy }

El jugador que va a jugar puede seleccionarse durante el quiz en QuizXpress Director, en la pestaña Reveal Word game.

![](../../assets/images/image229.webp){ width="505" loading=lazy }

Los puntos ganados o perdidos se muestran en el reproductor de quiz.

| ![](../../assets/images/image230.webp){ loading=lazy } | ![](../../assets/images/image231.webp){ loading=lazy } | ![](../../assets/images/image232.webp){ loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Compra de una vocal**                                                         | **Consonante correcta**                                                         | **Consonante incorrecta**                                                       |

En los juegos automáticos Word Reveal y Word Scramble puede configurar el ritmo de revelación u ordenación. De forma predeterminada, cada paso dura el mismo tiempo, lo que significa que, en el juego de revelación, las letras aparecen a intervalos fijos. Esto puede estar bien para una sola palabra, pero para una frase más larga quizá prefiera otro esquema, por ejemplo mostrar más letras al principio y luego ir más despacio. Puede elegir la opción que prefiera en la sección 'Reveal timing'.

Una vez insertado el elemento Word Game en la diapositiva, puede configurarlo con más detalle: haga clic en el elemento Word Game y modifique sus ajustes en la cinta Word Game, en la parte superior de Studio, o en la cuadrícula de propiedades avanzadas que aparece a la derecha de QuizXpress Studio.

![](../../assets/images/image233.webp){ loading=lazy }

Puede utilizar este elemento para distintos tipos de preguntas. Por ejemplo, una pregunta de tipo fastest finger en la que el jugador que pulsa primero adivina la frase correcta a partir de las letras reveladas hasta ese momento, o nombra una letra para revelarla y luego intenta adivinar la frase. O bien una pregunta de respuesta en texto libre con QuizXpress mobile, en la que todos los jugadores pueden escribir la respuesta correcta. Si se combina con puntos decrecientes, los jugadores más rápidos obtienen más puntos. También puede dar un turno a cada jugador y hacer que gane puntos con el modo de revelación manual combinado con puntos. El color, la fuente, el tamaño de las letras, los márgenes, etc. se pueden editar en la cinta o en la cuadrícula de propiedades avanzadas.

El elemento Word Game respeta la propiedad 'Show correct answer' de la diapositiva. Si está establecida en 'Do not show', el Word Game no revelará la respuesta correcta cuando termine la pregunta. Si está establecida en 'Global' (valor predeterminado), el Word Game sigue el ajuste 'Show correct answer on quiz slides' de Quiz Setup.
