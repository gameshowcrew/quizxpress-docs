# Animaciones de entrada

Desde la versión 8.6, la pregunta y las respuestas pueden hacer una entrada en Quiz Show: en lugar de aparecer sin más, aparecen gradualmente, se deslizan desde un lado, saltan, caen y rebotan, etc. Eliges un efecto para la pregunta y otro para las respuestas, y decides si las respuestas entran una tras otra o todas a la vez.

## Configurar una entrada

Selecciona la diapositiva en Quiz Studio y abre la sección «Animación» de las propiedades de la diapositiva (en la [cuadrícula de propiedades avanzadas](../user-interface-overview/advanced-properties-grid.md) encontrarás los mismos ajustes en «Apariencia»):

| Ajuste | Qué hace |
|---|---|
| «Entrada de la pregunta» | Cómo entra la pregunta. Las imágenes que no son respuestas entran junto con la pregunta. |
| «Entrada de las respuestas» | Cómo entran las respuestas. En una pregunta con varias imágenes, las imágenes de respuesta entran como respuestas. |
| «Orden de las respuestas» | «Una a una»: las respuestas entran una tras otra. «Todas a la vez»: entran al mismo tiempo. Se muestra cuando hay una entrada de las respuestas. |
| «Velocidad de animación» | «Normal», «Lenta» o «Rápida». Se aplica a la pregunta y a las respuestas. |
| «Cuenta atrás durante la animación» | Si está activado, la cuenta atrás empieza mientras la pregunta y las respuestas aún están entrando. Si está desactivado (valor predeterminado), la cuenta atrás empieza en cuanto todo está en la pantalla. |

«Orden de las respuestas», «Velocidad de animación» y «Cuenta atrás durante la animación» solo aparecen cuando hay una entrada para la pregunta o las respuestas.

Cuando la pregunta y las respuestas tienen entrada, las respuestas empiezan cuando la pregunta va por la mitad, de modo que una animación fluye hacia la otra.

## Efectos

| Efecto | Lo que se ve |
|---|---|
| «Ninguna» | Sin animación: el elemento simplemente aparece (valor predeterminado). |
| «Aparecer gradualmente» | El elemento aparece de forma gradual. |
| «Deslizar desde la izquierda» / «la derecha» / «arriba» / «abajo» | El elemento entra deslizándose desde fuera de la pantalla. |
| «Alternar izquierda y derecha» | Las respuestas llegan por turnos desde la izquierda y la derecha, empezando por la izquierda. Para la pregunta, esta se desliza desde la izquierda. |
| «Acercar» | El elemento crece desde la mitad de su tamaño mientras aparece gradualmente. |
| «Saltar» | El elemento salta, se pasa un poco de su tamaño y se asienta. |
| «Voltear» | El elemento se voltea como una carta. |
| «Girar» | El elemento gira hasta su posición mientras crece. |
| «Caer y rebotar» | El elemento cae desde arriba y rebota antes de asentarse. |

Con la velocidad «Normal» un elemento tarda unos 0,6 segundos en entrar, con «Lenta» unos 0,9 segundos y con «Rápida» unos 0,35 segundos. «Girar» y «Caer y rebotar» tardan un poco más para que se puedan seguir bien.

## Respuestas que se muestran después

Si las respuestas no se muestran enseguida, porque «Acción al mostrar respuestas» está en «Ocultar y mostrar una a una» u «Ocultar y mostrar a la vez», la «Entrada de las respuestas» se usa cada vez que aparecen respuestas.

## Diapositivas compatibles

Las animaciones de entrada funcionan en las diapositivas de pregunta y en los demás tipos de diapositiva que muestran una pregunta y respuestas. No están disponibles en Trivia Feud, rondas de Bingo, minijuegos, rondas Trivia Board y Trivia Ladder; en esas diapositivas no se muestran los ajustes de «Animación».

!!! tip
    Las animaciones de entrada combinan bien con las [animaciones de revelado de texto](text-reveal-animations.md): haz que la pregunta entre deslizándose y luego revela su texto palabra por palabra, o haz caer las respuestas una a una después de leer la pregunta.
