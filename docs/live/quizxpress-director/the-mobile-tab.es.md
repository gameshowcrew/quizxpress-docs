# La pestaña Mobile

La pestaña Mobile muestra todos los dispositivos móviles conectados actualmente.

![](../../assets/images/image455.webp){ loading=lazy }

Desde aquí puede:

- Select Jingle: forzar la **selección de jingle** para todos los jugadores que utilizan la aplicación Smart Buzzer

- **Send Message:** enviar un mensaje a los jugadores seleccionados

- **Blacklist Player: bloquear de forma permanente al jugador seleccionado para que ya no pueda volver a unirse a su quiz**

- **Latency Test: comprobar la calidad de la conexión de todos los dispositivos**

- **Pair with Host Remote: mostrar el código QR que debe escanear la aplicación Director (mando a distancia móvil del presentador del quiz) para añadir este ordenador a la lista de ordenadores que se pueden controlar.**

- Settings: abrir el cuadro de diálogo de ajustes móviles

- Chat: abrir una sesión de chat que le permite chatear con todos los jugadores

- A la derecha puede ver el PIN actual (cuando se ejecuta en modo servidor)

## Prueba de latencia

La prueba de latencia se utiliza sobre todo cuando se trabaja en modo Wi-Fi local, para comprobar si todos sus jugadores tienen una conexión sólida con su router. Envía un ping a todos los dispositivos y mide el tiempo que tarda en recibir una respuesta. Esto se representa detrás de cada dispositivo móvil en un gráfico como este:

![](../../assets/images/image456.webp){ loading=lazy }

Cuando un dispositivo es muy lento o está desconectado, el gráfico se pone en rojo y, como presentador del quiz, puede avisar al jugador de que se acerque al punto de acceso. Nota: no deje la prueba de latencia en ejecución durante su quiz, ya que la prueba consume ancho de banda Wi-Fi y capacidad del servidor.

## Chat instantáneo

Puede iniciar una sesión de chat con los jugadores haciendo clic en el botón Chat.

![](../../assets/images/image457.webp){ width="171" loading=lazy }  
Tras iniciar el chat, los jugadores ven un botón de chat en su teléfono.

![](../../assets/images/image458.webp){ width="163" loading=lazy } ![](../../assets/images/image459.webp){ width="166" loading=lazy }

Al pulsar el botón de chat, los jugadores pueden enviar mensajes de chat al presentador del quiz, que se muestran en una pestaña denominada ‘Chat’. El presentador del quiz ve todos los mensajes de chat por usuario y puede enviar un mensaje de respuesta a cada jugador individualmente.

![](../../assets/images/image460.webp){ width="416" loading=lazy }

!!! note

    actualmente, esta función solo está disponible para los jugadores del pulsador web buzzerpad. Todavía no está disponible en la aplicación Smart Buzzer.*

## Ajustes

Hay algunos ajustes avanzados que puede encontrar bajo el botón *Settings*:

![](../../assets/images/image461.webp){ width="332" loading=lazy }

Las casillas superiores controlan los mensajes de confirmación opcionales que se envían a los dispositivos conectados. Estos mensajes ayudan a los usuarios a entender lo que sucede. La primera opción informa al dispositivo de cada respuesta recibida con un mensaje como ‘We received answer D’. La segunda opción solo envía una advertencia cuando no se ha recibido ninguna respuesta o cuando la respuesta no se procesó a tiempo (por ejemplo, debido a la latencia en la transmisión de vídeo). La tercera opción envía al dispositivo un mensaje con los puntos ganados/perdidos después de cada pregunta, y la última opción le permite controlar si el dispositivo muestra si el jugador respondió correcta o incorrectamente.

Con el ajuste ‘Game PIN indicator’ puede configurar un indicador de PIN que se muestra en cuatro ubicaciones distintas de la pantalla del quiz durante el quiz. Este ajuste no se aplica en el modo Wi-Fi, ya que en ese modo no se utiliza PIN. El indicador de PIN tiene este aspecto:

![](../../assets/images/image462.webp){ width="310" loading=lazy }

También hay algunos ajustes para controlar el mando móvil, como si debe reproducir sonidos y, para el sitio web buzzerpad, una opción para establecerlo en el comportamiento de mando simple, es decir, que solo mostrará un mando de 7 botones (modo heredado). También puede indicar aquí si desea mostrar imágenes también en los teléfonos móviles.

La sección de visualización del código QR le permite indicar si desea mostrar un código QR que apunte al pulsador web indicado en QuizXpress Setup, o si desea mostrar un enlace a la aplicación Smart Buzzer en las tiendas de aplicaciones de iOS y Android. Si muestra la URL del pulsador web, puede especificar parámetros adicionales en el campo URL Extension, que pueden utilizarse para personalizar la imagen de marca del mando web. Para obtener más información, consulte [Personalización de la marca del sitio web buzzerpad](../using-mobile-keypads/branding-the-buzzerpad-website.md).

El control deslizante Server delay se puede utilizar para retrasar todas las acciones enviadas a los dispositivos móviles, con el fin de lograr una mejor sincronización con su transmisión. Mantenga este valor en 0 cuando no esté transmitiendo. Por ejemplo, si la latencia de su transmisión de YouTube es de ~3 segundos, puede establecer el retraso en 3 segundos. Esto significa que cuando la cuenta atrás comienza en la transmisión de YouTube de los jugadores, también comenzará en su dispositivo. Sin el retraso, la cuenta atrás del dispositivo empezaría 3 segundos antes de que arranque el temporizador en YouTube, lo que puede resultar confuso.

Cuando la opción ‘Extend answer time’ está marcada, el sistema sigue aceptando votos incluso después de que el reloj de la cuenta atrás haya expirado, durante el tiempo establecido en el control deslizante ‘Server delay’. Esto puede utilizarse para compensar la latencia de la transmisión. Por ejemplo, si hay un retraso de 5 segundos en la transmisión, los jugadores al otro lado siguen viendo avanzar el reloj durante 5 segundos después de que ya se haya detenido en el estudio. Así, con esta opción activada, el sistema seguirá aceptando votos en esos últimos 5 segundos, evitando que los jugadores se pierdan una pregunta.

**Cambiar el rango de dispositivos móviles sobre la marcha**

Imagine que ha lanzado un quiz en línea en el que espera hasta 20 jugadores (rango de dispositivos “1-20”) y, 10 minutos después de empezar su introducción, otros 15 jugadores quieren unirse. Antes, tenía que reiniciar el quiz y hacer que todos se registraran de nuevo con el nuevo PIN, etc. Para evitarlo, ahora puede actualizar el rango de dispositivos móviles mientras su quiz está en marcha.

Para ello, abra Director en el reproductor del quiz, vaya a la pestaña Mobile y haga clic en el botón Settings. A continuación, haga clic en el botón Change device range e introduzca el nuevo rango:

![](../../assets/images/image463.webp){ loading=lazy }

El sistema comprobará la validez del rango y pedirá confirmación. Tras su aprobación, se actualizará el servidor. Tenga en cuenta que si reduce el rango (por ejemplo, de “1-50” a “1-20”), los jugadores conectados que queden fuera del nuevo rango serán desconectados.
