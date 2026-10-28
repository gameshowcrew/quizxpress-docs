# La pantalla de registro de mandos y pulsadores

La finalidad de la pantalla de registro es averiguar qué pulsadores/mandos participan en el evento del quiz. Al hacer que los participantes se registren de forma explícita, el software sabe cuántos dispositivos hay presentes. Existen tres ‘variantes’ de pantallas de asignación de pulsadores:

- Pantalla de asignación de pulsadores Sony

- Pantalla de asignación de pulsadores para menos de 100 participantes

- Pantalla de asignación de pulsadores para más de 100 equipos

## Pantalla de asignación de pulsadores Sony

Al utilizar pulsadores Sony, pueden introducirse nombres en el programa Quiz Setup para cada participante/equipo. Como un pulsador Sony no tiene un identificador explícito, no es posible vincular el nombre de un equipo a un pulsador concreto al definir los nombres de los equipos en Quiz Setup. La pantalla de asignación de pulsadores resuelve este problema: muestra los nombres de los equipos uno a uno y, cuando un equipo ve aparecer su nombre al frente del ‘Buzzer Assignment Carousel’, debe pulsar el pulsador para registrarse en el quiz. A continuación puede ver una captura de pantalla de la pantalla de asignación de pulsadores Sony.

![](../../assets/images/image403.webp){ width="605" loading=lazy }

En la parte inferior hay dos botones: el de la izquierda (la flecha redonda) restablece los datos para que la asignación de pulsadores empiece de nuevo; el botón situado más a la derecha es el botón de ‘inicio’, que inicia el quiz.

## Pantalla de asignación de pulsadores, menos de 100 participantes

Cada mando Reply/QuizXpress tiene un identificador único, que también se utiliza en el software QuizXpress Live para identificar a un participante (por ejemplo, pulsador con ID 1: Equipo 1). Cuando participan menos de 100 pulsadores en el quiz (según el ajuste ‘Keypads’ introducido en Quiz Setup), se muestra una cuadrícula con todos los identificadores de pulsador.

Cuando se pulsa una tecla de un mando, queda registrado como activo en el sistema QuizXpress Live. En la cuadrícula aparece una marca de verificación en el número correspondiente al ID del pulsador pulsado.

Hablando con propiedad, no es necesario que los pulsadores se registren de forma explícita. Sin embargo, el software QuizXpress Live necesita saber exactamente cuántos equipos participan, para poder determinar cuándo han respondido todos los equipos a una pregunta y detener la cuenta atrás.

El botón que se muestra en la parte inferior de la pantalla es el botón de ‘inicio’, que inicia el quiz. A continuación puede ver dos capturas de pantalla: una con la pantalla antes de que nadie se haya registrado y otra con el estado de la pantalla una vez que todos se han registrado.

| ![](../../assets/images/image404.webp){ loading=lazy } | ![](../../assets/images/image405.webp){ loading=lazy } |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------|

!!! note

    para realizar pruebas, puede asignar los 100 pulsadores a la vez pulsando F1, o todos los pulsadores configurados en Quiz Setup pulsando F2.*

## Pantalla de asignación de pulsadores, más de 100 participantes

Cuando se utilizan más de 100 pulsadores, una cuadrícula resulta cada vez más difícil de leer. Por eso QuizXpress Live utiliza en ese caso una pantalla de asignación de pulsadores diferente. Vea a continuación una captura de pantalla.

El botón que se muestra en la parte inferior de la pantalla es el botón de ‘inicio’, que inicia el quiz.

!!! note

    no se muestra ninguna pantalla de asignación de pulsadores cuando se utilizan pulsadores de tipo Keyboard o Game port, ya que estos sistemas tienen una asignación fija.*
