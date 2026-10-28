# Fondos

Cada estilo de QuizXpress tiene un fondo. Puede cambiar el fondo de una diapositiva (también después de seleccionar un estilo) haciendo clic con el botón derecho en una diapositiva y eligiendo 'Select background picture…'.

También puede elegir una imagen de fondo en la galería de fondos de la sección Background Image de la cinta Design. Además, puede añadir sus propios fondos a la galería.

Al igual que con los estilos, puede organizar mejor su espacio de trabajo filtrando los fondos que no utiliza. Puede acceder al filtro desde el botón 'dialog launcher' de la sección Background Image de la cinta Design.

![](../assets/images/image279.webp){ width="466" loading=lazy }

## Vídeo de fondo

En lugar de una imagen fija, una diapositiva también puede tener un vídeo que se reproduce detrás: nubes en movimiento, una cuenta atrás, una animación en bucle con sus propios colores. La pregunta, las respuestas y todo lo demás de la diapositiva permanecen por encima del vídeo.

Para añadir uno, haga clic con el botón derecho en el fondo de la diapositiva, elija 'Background video…' y seleccione un archivo de vídeo. También puede establecerlo en el panel de propiedades: seleccione la diapositiva y haga clic en la propiedad 'Background video' de la sección Background de la página Design. Si selecciona varias diapositivas y establece la propiedad, todas reciben el mismo vídeo de fondo; el vídeo se almacena una sola vez en el archivo de quiz.

![Menú contextual del fondo de la diapositiva con las opciones del vídeo de fondo](../assets/images/background-video-context-menu.webp){ loading=lazy }

En el editor, la diapositiva muestra el primer fotograma del vídeo, con un pequeño icono de vídeo en la esquina superior izquierda para que pueda ver qué diapositivas tienen un vídeo de fondo. Para verlo en movimiento, haga clic con el botón derecho en el fondo y elija 'Play background video' (y 'Stop background video' para detenerlo). La vista previa (F5) también lo reproduce.

Un vídeo de fondo no ocupa un marcador de posición de imagen o vídeo, de modo que en la misma diapositiva aún puede colocar una imagen o un [vídeo en un marcador de posición](adding-multimedia-content/video.md#combinar-un-video-de-fondo-con-un-video-en-un-marcador-de-posicion); se reproduce por encima del vídeo de fondo.

Cuando una diapositiva tiene un vídeo de fondo, los siguientes ajustes aparecen debajo de la propiedad 'Background video':

![Ajustes del vídeo de fondo en el panel de propiedades](../assets/images/properties-panel-background-video.webp){ width="322" loading=lazy }

| Propiedad          | Descripción                                                                                                                                                                                                 |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Video storage type | Embedded (el vídeo se almacena en el archivo de quiz) o linked (el quiz hace referencia al archivo de vídeo en el disco). Consulte [Vídeo](adding-multimedia-content/video.md#insertar-un-video) para saber cuándo usar cada uno. |
| Linked file        | El nombre del archivo de vídeo, en el caso de un vídeo vinculado                                                                                                                                            |
| Loop               | Vuelve a iniciar el vídeo cuando termina. Activado de forma predeterminada.                                                                                                                                 |
| Silent             | Reproduce el vídeo sin sonido. Activado de forma predeterminada, para que el vídeo de fondo no moleste a los sonidos de sus preguntas.                                                                      |
| Sync with quiz     | Pausa el vídeo cuando un equipo pulsa el pulsador, la cuenta atrás se pausa o termina la pregunta, y lo reanuda cuando la pregunta continúa. Desactivado de forma predeterminada: el vídeo simplemente sigue reproduciéndose. (En 'More options'.) |

Para quitar el vídeo de fondo, haga clic con el botón derecho en el fondo de la diapositiva y elija 'Remove background video'.

!!! tip
    Asigne un vídeo de fondo a una [categoría](using-categories.md) y todas las diapositivas que formatee con esa categoría lo recibirán también.

Durante el quiz, el vídeo de fondo se inicia en cuanto aparece la diapositiva. Mantenga los vídeos de fondo cortos y ligeros: un bucle de unos pocos segundos en HD suele ser suficiente.
