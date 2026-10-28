# Área de diseño

El área de diseño contiene una representación visual de lo que llamamos una ‘diapositiva de quiz’. Muestra la ‘diapositiva de quiz’ exactamente como se verá durante el concurso. Una ‘diapositiva de quiz’ se compone de varios elementos: una pregunta, respuestas de opción múltiple, imágenes, formas y texto, un vídeo o un elemento de sonido, etc. Los elementos se pueden seleccionar individualmente o en grupo, y después modificarlos. También se puede seleccionar la diapositiva de quiz completa para editar sus propiedades. Para seleccionar una diapositiva de quiz, haga clic en el fondo de la diapositiva. Consulte [Quiz slide properties](advanced-properties-grid.md#propiedades-de-las-diapositivas-de-quiz) para ver una descripción de todas las propiedades de una diapositiva.

Los elementos de la diapositiva se pueden seleccionar y redimensionar haciendo clic con el botón izquierdo en uno de los tiradores de tamaño y arrastrándolo hasta el tamaño deseado. Cuando hay varios elementos seleccionados, ya sea con la tecla Ctrl o arrastrando un cuadro de selección con el ratón, al editar las propiedades que se muestran en el panel de propiedades (o al usar los controles de la cinta de opciones) se cambian las propiedades de todos los elementos seleccionados a la vez. Esto resulta práctico, por ejemplo, cuando desea establecer la fuente de todas las respuestas de una pregunta de una sola vez: primero seleccione todas las respuestas y después cambie la propiedad ‘font’ en el panel de propiedades. Al mover objetos, estos se ajustan a las [guías inteligentes](#guias-inteligentes) y a una cuadrícula invisible; mantenga pulsada la tecla *Ctrl* mientras arrastra para desactivar este ajuste.

## Guías inteligentes

Mientras mueve o redimensiona elementos de una diapositiva, Quiz Studio muestra guías inteligentes: líneas rojas que indican cuándo los elementos están alineados, y el elemento se ajusta a su posición en cuanto se acerca. Esto facilita crear diapositivas ordenadas y coherentes sin medir nada.

![Guías inteligentes al mover una respuesta](../../assets/images/smart-guides-spacing.webp){ loading=lazy }

- **Alineación de bordes**: aparece una línea roja discontinua cuando un borde del elemento queda alineado con un borde de otro elemento o con el borde de la diapositiva. Unas pequeñas cruces rojas marcan los elementos alineados.
- **Alineación de centros**: aparece una línea roja de trazo y punto cuando el centro del elemento queda alineado con el centro de otro elemento o con el centro de la diapositiva.
- **Espaciado igual**: cuando el elemento está a la misma distancia del elemento superior (o anterior) que del inferior (o posterior), o a la misma distancia que la que separa a otros elementos de la misma fila o columna, aparecen flechas con la distancia en píxeles en cada espacio igual. En la imagen anterior, las cuatro respuestas están separadas por 20 píxeles.
- **Tamaño igual**: mientras redimensiona un elemento, este se ajusta al ancho o al alto de otro elemento de la diapositiva, y se muestra un marcador de tamaño en cada elemento que tiene ese tamaño.

![Guías inteligentes al redimensionar una respuesta](../../assets/images/smart-guides-size.webp){ loading=lazy }

Mientras arrastra, una copia transparente del elemento muestra dónde quedará, y una pequeña etiqueta indica su posición (X e Y) o, al redimensionar, su tamaño, en píxeles de la diapositiva. Las guías inteligentes también funcionan cuando mueve varios elementos seleccionados a la vez.

- Mantenga pulsada la tecla *Ctrl* mientras arrastra para colocar un elemento libremente, sin guías inteligentes ni cuadrícula.
- Pulse *Esc* mientras arrastra para cancelar el movimiento y dejar el elemento donde estaba.

Para desactivar (o volver a activar) las guías inteligentes, haga clic con el botón derecho en el fondo de la diapositiva y haga clic en ‘Smart guides’. Quiz Studio recuerda este ajuste. Entonces los elementos solo se ajustan a la cuadrícula invisible.

![Guías inteligentes en el menú contextual de la diapositiva](../../assets/images/smart-guides-menu.webp){ width="200" loading=lazy }

!!! tip
    Para alinear varios elementos de una sola vez, selecciónelos y utilice las [herramientas de alineación](../other-functionality/home-alignment-size-order.md) de la cinta de opciones HOME.

## Insertar una diapositiva

Para insertar una nueva diapositiva, vaya al menú INSERT y elija uno de los diseños predefinidos de la sección ‘Quiz Slides’. Los recuadros azul oscuro representan marcadores de posición para insertar una imagen o un vídeo.

![](../../assets/images/image13.webp){ loading=lazy }

Al elegir los diseños de la fila inferior, puede insertar, respectivamente, un minijuego, un Trivia Board, un Trivia Ladder, un juego Trivia Feud o una ronda de Bingo.

También puede cambiar el diseño de una diapositiva existente desde el menú DESIGN haciendo clic en la flecha desplegable de la sección ‘Change Layout’. Aparece la misma lista desplegable mostrada arriba, que le permite elegir un nuevo diseño. Los elementos del diseño actual que encajen en el nuevo diseño se copiarán. Por ejemplo, al pasar de un diseño con una pregunta, una imagen y tres respuestas a un diseño con una pregunta, una imagen y cuatro respuestas, la imagen, la pregunta y las tres respuestas se copiarán al nuevo diseño.
