# Realizar su quiz en un stand de feria con QuizXpress Solo

QuizXpress Solo es una variante de QuizXpress Live que permite jugar un quiz a una sola persona. Sin embargo, antes de comenzar el quiz, esta persona debe introducir algunos datos personales, tras lo cual se inicia el quiz. Mediante un único pulsador, esta persona puede responder a las preguntas presentadas. La puntuación final, así como el tiempo empleado en responder a todas las preguntas (solo las correctas), se registran y pueden mostrarse, ordenados por puntuación, cuando se desee.

Imagine que se encuentra en una feria comercial y desea atraer a la gente a su stand haciéndola jugar a un quiz. Por supuesto, le gustaría recopilar cierta información de estas personas, por lo que deben rellenar algunos datos antes de que comience el quiz. Cuando una persona ha terminado el quiz, la pantalla de inicio (introducción de datos) de QuizXpress Live se muestra de nuevo, lista para el siguiente jugador. Como todas las puntuaciones se guardan en un archivo de Excel, al final del día puede seleccionar al ganador que (por ejemplo) gana un premio. QuizXpress Solo puede iniciarse desde el menú Inicio mediante Inicio > Todos los programas > QuizXpress > QuizXpress Solo.

La pantalla de inicio de QuizXpress Solo tiene el siguiente aspecto:

El botón ‘Results’, que sirve para mostrar los resultados almacenados, se muestra en la parte superior derecha de la pantalla. Sin embargo, no se muestra automáticamente: es un ‘botón oculto’ que solo aparece al pulsar la tecla Control (Ctrl), para evitar que personas no autorizadas vean las puntuaciones.

Al pulsar Control, también aparece un botón ‘Setup’. Al pulsarlo, puede personalizar los campos de introducción de datos que se muestran, personalizar el color del panel central y de las etiquetas, y seleccionar una imagen para utilizarla como fondo.

Al pulsar la tecla Ctrl también aparece el botón Exit para cerrar la aplicación.

Una vez rellenada toda la información necesaria (los campos de entrada subrayados son obligatorios), el botón ‘Start’ se vuelve verde, y el usuario debe pulsarlo para comenzar el quiz. Se muestra la pantalla de bienvenida del quiz. Al pulsar el pulsador se avanza a la primera pregunta. Las preguntas se responden con el botón A, B, C o D del pulsador. Cuando se ha respondido a una pregunta, el jugador puede continuar pulsando cualquier tecla del pulsador. En resumen, todo el quiz puede manejarse con un único pulsador. Cuando una persona ha terminado el quiz, se muestra la pantalla de puntuación, que tiene el siguiente aspecto (según el skin elegido; en el ejemplo siguiente estaba activo el skin Techno):

![](assets/images/image468.webp){ loading=lazy }

La pantalla de puntuación muestra tanto la puntuación del jugador como el tiempo necesario para responder a las preguntas. Solo se cuenta el tiempo empleado en responder correctamente. Después de pulsar uno de los botones del pulsador, se muestra de nuevo la pantalla inicial de QuizXpress Live.

Al pulsar ‘Results’ se muestra la pantalla de puntuación con todos los participantes que han jugado hasta el momento:

![](assets/images/image469.webp){ loading=lazy }

### Personalizar la pantalla de introducción de datos de QuizXpress Solo

Tanto el fondo como los campos que se pueden (o se deben) rellenar pueden personalizarse.

#### Personalizar la imagen de fondo

La imagen de fondo de la pantalla de introducción de datos de QuizXpress Solo puede personalizarse (re)colocando un archivo .jpg llamado “QuizXpressSolo.jpg”, o un archivo .png llamado “QuizXpressSolo.png”, en el directorio de instalación de QuizXpress.

#### Personalizar los campos de introducción de datos

Los campos de introducción de datos de QuizXpress Solo también pueden personalizarse. Para personalizar los campos, pulse el botón ‘Setup’ que se muestra en la parte superior de la pantalla (al igual que el botón ‘Results’, se hace visible al pulsar \<Ctrl>). Tras pulsar ‘Setup’, se muestra la siguiente pantalla:

En la ventana mostrada (véase la página siguiente), se pueden configurar todos los campos de introducción de datos (hay un máximo de 10 campos). Si un participante debe rellenar un campo antes de poder iniciar el quiz, marque la casilla de la columna ‘Mandatory’ de ese campo. En este caso, el campo aparecerá subrayado en la pantalla de inicio de QuizXpress Solo, lo que indica al participante que debe rellenarlo antes de poder comenzar el quiz. Cuando todos los campos obligatorios están rellenados, el botón ‘Start’ se vuelve verde, y el usuario debe pulsarlo para comenzar el quiz.

!!! note

    si se cambia el número de campos, las puntuaciones almacenadas anteriormente se borrarán tras la confirmación. En este caso, se mostrará un mensaje que le recordará que guarde primero los resultados anteriores si es necesario (esto puede hacerse pulsando el botón ‘Results’ para mostrar los resultados actuales y eligiendo después ‘Save as CSV’).

![](assets/images/image470.webp){ loading=lazy }
