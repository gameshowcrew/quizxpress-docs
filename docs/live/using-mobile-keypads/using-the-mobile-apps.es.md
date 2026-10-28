# Uso de las aplicaciones móviles de QuizXpress

QuizXpress Mobile también ofrece dos aplicaciones, ambas disponibles para Android e iOS.

**QuizXpress Smart Buzzer**

Esta es la aplicación que utilizan los jugadores del quiz. Antes de iniciar su primer quiz, indique a sus jugadores que descarguen la aplicación gratuita QuizXpress Smart Buzzer desde la tienda de aplicaciones de su teléfono. Basta con buscar *QuizXpress Smart Buzzer*, instalarla y ya pueden jugar.

![](../../assets/images/image366.webp){ width="226" loading=lazy }

**Aplicación QuizXpress Director**

Para el anfitrión/presentador del quiz, disponemos de una aplicación independiente llamada *QuizXpress Director*. Esta aplicación permite al anfitrión controlar el quiz (mostrar la siguiente pregunta, revelar la respuesta, mostrar puntuaciones intermedias o gráficos), gestionar equipos (cambiar puntuaciones o nombres de equipo), iniciar minijuegos, reproducir sonidos mediante un soundboard y hacer muchas otras cosas.

Las siguientes secciones describen las aplicaciones con más detalle.

## Aplicación QuizXpress Smart Buzzer

Al iniciar la aplicación, los jugadores ven la opción de unirse a una partida por Wi-Fi local o mediante PIN.

![](../../assets/images/image367.webp){ width="177" loading=lazy }

Cuando la partida se ejecuta con un router Wi-Fi conectado al ordenador, el botón ‘Join local Wi-Fi game’ está habilitado. Al tocar el botón, se establece la conexión con el quiz que se ejecuta en el Wi-Fi local.

Cuando se juega sin un router Wi-Fi y, por tanto, se conecta de forma remota a través de internet, el quiz player muestra un código PIN en pantalla. Los jugadores pueden introducir este código PIN pulsando ‘Join game with PIN’.

Una vez iniciada la sesión, se muestra la pantalla de bienvenida configurada en la sección Branding de los ajustes (consulte [Configuración de la compatibilidad con mandos móviles](../../setup/setting-up-mobile-keypad-support.md)).

Si ha configurado jingles definiendo la carpeta Jingles en los ajustes, se mostrará a los jugadores una lista de todos los fragmentos de sonido disponibles. Cada jugador puede elegir un jingle que se utilizará durante la partida en las siguientes situaciones:

- Puntos de bonificación: el sonido del jugador que fue el primero en dar la respuesta correcta se reproduce cuando se muestra la pantalla de puntos de bonificación.

- Fastest finger: se reproduce el sonido del jugador que pulsó primero, y el nombre del jugador aparece en pantalla en el quiz player.

- Resúmenes de puntuación intermedios: el sonido del jugador que ocupa el primer puesto se reproduce al mostrar la clasificación.

> Como presentador del quiz, siempre puede activar manualmente la selección de jingle para un dispositivo concreto en la pestaña Mobile de Director.

A la izquierda se ve un ejemplo de pregunta de tipo ‘first letter’.

En pantalla se ven varios elementos:

- En la parte superior izquierda se ve el número asignado a su pulsador móvil.

- En la parte superior derecha se muestra el nombre del jugador.

- La barra superior contiene:

  - El índice de la pregunta actual (en este caso, la primera de 21)

  - Un trofeo con el número de puntos que se pueden ganar. Si los puntos disminuyen con el tiempo, se reflejará aquí. Es un valor aproximado.

  - Un reloj con cuenta atrás que muestra los segundos restantes. Durante los últimos 5 segundos, el reloj parpadea para indicar que se acaba el tiempo.

- La cuadrícula de letras utilizada para responder a la pregunta.

QuizXpress Smart Buzzer admite una variedad de tipos de pregunta:

| ![](../../assets/images/image368.webp){ width="96" loading=lazy }                                                                                               | ![](../../assets/images/image369.webp){ width="96" loading=lazy }            | ![](../../assets/images/image370.webp){ width="96" loading=lazy }           | ![](../../assets/images/image371.webp){ width="96" loading=lazy }              | ![](../../assets/images/image372.webp){ width="95" loading=lazy }        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Fastest finger*                                                                                                                                                                                                             | *Multiple Choice regular/ordered/multiple answer/eliminator*                                                                                                                                                               | *First Letter*                                                                                                                                                                                                            | *Full text*                                                                                                                                                                                                                  | *Numeric*                                                                                                                                                                                                                  |
| ![](../../assets/images/image373.webp){ width="98" loading=lazy } | ![](../../assets/images/image374.webp){ width="99" loading=lazy } | ![](../../assets/images/image375.webp){ width="100" loading=lazy } | ![](../../assets/images/image376.webp){ width="100" loading=lazy } | ![](../../assets/images/image377.webp){ width="98" loading=lazy } |
| *Multiple Choice with picture*                                                                                                                                                                                               | *Multiple Choice with picture effect*                                                                                                                                                                                      | *Fastest finger with picture*                                                                                                                                                                                             | *Multiple Choice pictures regular/ordered/multiple answer*                                                                                                                                                                   | *Numeric/First letter with picture*                                                                                                                                                                                        |

El Smart Buzzer da información después de cada pregunta sobre si acertó o falló, y si recibió puntos de bonificación:

| ![](../../assets/images/image378.webp){ width="109" loading=lazy } | ![](../../assets/images/image379.webp){ width="109" loading=lazy } | ![](../../assets/images/image380.webp){ width="108" loading=lazy } | ![](../../assets/images/image381.webp){ width="109" loading=lazy } | ![](../../assets/images/image382.webp){ width="109" loading=lazy } |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Respuesta correcta*                                                                                                                 | *Respuesta incorrecta*                                                                                                                                                                                                | *Letra incorrecta*                                                                                                                                                                                                   | *Animación de puntos de bonificación*                                                                                                                                                                                         | *Puntos de bonificación ganados*                                                                                                                                                                                      |

Las puntuaciones también se muestran en el teléfono. Las puntuaciones finales se muestran en dos o tres pasos: primero un anuncio, después su clasificación entre los 3 primeros (si está entre los 3 primeros) y, por último, su puntuación y posición individuales.

| ![](../../assets/images/image383.webp){ width="136" loading=lazy } | ![](../../assets/images/image384.webp){ width="137" loading=lazy } | ![](../../assets/images/image385.webp){ width="137" loading=lazy } | ![](../../assets/images/image386.webp){ width="137" loading=lazy } |
|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| *Puntuaciones intermedias*                                                                                                           | *Anuncio de las puntuaciones finales*                                                                                                                                                                                          | *Puntuación final individual entre los 3 primeros*                                                                                            | *Puntuación individual, posición y los 3 primeros*                                                                                            |

El uso de la aplicación es obligatorio si tiene previsto jugar mediante Wi-Fi independiente. Desde QuizXpress 8, el buzzer web de buzzerpad ofrece la misma funcionalidad que la aplicación Smart Buzzer, excepto la opción de Wi-Fi local y la selección de jingles.

## Promociones

La aplicación Smart Buzzer permite mostrar imágenes ‘promocionales’ durante el quiz o durante un descanso. Las imágenes se pueden enviar desde la pantalla *Media Player* de QuizXpress Director. Primero debe añadir su imagen a la lista de medios disponibles. Para presentar la imagen en la aplicación Smart Buzzer, selecciónela en la lista y haga clic en *Show on Mobile* en la barra de herramientas.

![](../../assets/images/image387.webp){ width="526" loading=lazy }

## Thumbs Up/Thumbs Down

Con este modo de juego, los jugadores pueden ganar puntos extra votando sobre la corrección de la respuesta verbal de otro jugador a una pregunta abierta. Esto se aplica a situaciones en las que es posible la interacción directa con los jugadores (por lo tanto, no para una configuración de transmisión). Funciona de la siguiente manera:

- Se presenta una pregunta de fastest finger a los jugadores. Aparecen pulsadores en todas las aplicaciones Smart Buzzer

- Un jugador cree saber la respuesta y pulsa el pulsador; todos los demás quedan bloqueados.

- En la pantalla o aplicación de Director aparece una ventana emergente de juicio correcto/incorrecto con los botones *Thumbs Down/Poll/Thumbs Up*.

![](../../assets/images/image388.webp){ width="145" loading=lazy }

- El presentador del quiz habla con el jugador para oír la respuesta verbal y después puede juzgar la respuesta como correcta o incorrecta, o consultar al resto de los jugadores si *ellos* creen que la respuesta dada era correcta o incorrecta, tocando el botón *Poll* en la aplicación Director.

- En los dispositivos de los demás jugadores aparece durante 10 segundos una ventana emergente de votación Thumbs Up/Thumbs Down, y los jugadores pueden emitir su voto (o abstenerse, en cuyo caso no hay riesgo de perder puntos).

![](../../assets/images/image389.webp){ width="141" loading=lazy }

- Ahora el presentador del quiz juzga la respuesta dada por el jugador de fastest finger tocando el botón ‘Right’ o ‘Wrong’ en la aplicación Director. Como resultado, el jugador que pulsó primero gana o pierde puntos (según los ajustes de la pregunta). Los demás jugadores ganan o pierden el 50 % de los puntos de la pregunta, según si su juicio sobre la respuesta del jugador que pulsó primero fue correcto.

Este modo mantiene implicados a todos los jugadores en una ronda de fastest finger, ya que no es solo el jugador más rápido quien puede ganar puntos: todos los participantes tienen la oportunidad de ganar puntos.

## Aplicación de control remoto: Mobile Director

Para controlar el quiz desde su tableta o teléfono, puede utilizar la aplicación de control remoto QuizXpress Director para iOS y Android. Tras instalar e iniciar la aplicación, verá la siguiente pantalla:

Puede registrar el ordenador que desea controlar con el control remoto QuizXpress Director pulsando el botón amarillo de ‘más’ en la parte inferior derecha de la pantalla de su móvil.

Al pulsar el botón, se mostrará un escáner de códigos QR. El código QR que debe escanear se muestra en la pestaña Mobile de QuizXpress Setup (consulte [Configuración de la compatibilidad con mandos móviles](../../setup/setting-up-mobile-keypad-support.md)). Escanee el código que se muestra aquí y el nombre del ordenador aparecerá en la aplicación QuizXpress Director. Solo tiene que seguir este procedimiento una vez para registrar su ordenador en la aplicación.

Tras iniciar un quiz, seleccione de la lista el ordenador que desea controlar y tóquelo: la aplicación de control remoto móvil quedará entonces conectada a la sesión del quiz.

!!! note

    Asegúrese de que el servidor seleccionado en la aplicación QuizXpress Director sea el mismo que el seleccionado en QuizXpress Setup. Haga clic en el botón de menú ![](../../assets/images/image390.webp){ .inline-icon width="23" } situado en la parte superior izquierda de la aplicación. Haga clic en ‘Settings’ y compruebe el ajuste ‘Mobile server to connect to’. Este ajuste debe coincidir con el configurado en QuizXpress Setup (consulte [Configuración de la compatibilidad con mandos móviles](../../setup/setting-up-mobile-keypad-support.md) para obtener información sobre cómo establecer el servidor (o el Wi-Fi local) que utiliza el quiz player).

| **Mobile server to connect to** | **Settings server**                           |
|---------------------------------|-----------------------------------------------|
| Central US                      | [www.buzzerpad.com](http://www.buzzerpad.com) |
| Western Europe                  | [www.buzzerpad.eu](http://www.buzzerpad.eu)   |
| Local Wi-Fi                     | Local Wi-Fi                                   |

Tras conectarse al quiz en ejecución, verá la aplicación QuizXpress Director, que tiene 5 pestañas:

| ![](../../assets/images/image391.webp){ width="103" loading=lazy } | ![](../../assets/images/image392.webp){ width="114" loading=lazy } | ![](../../assets/images/image393.webp){ width="113" loading=lazy } | ![](../../assets/images/image394.webp){ width="116" loading=lazy } | ![](../../assets/images/image395.webp){ width="115" loading=lazy } |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Control remoto                                                                                                                                                                    | Iniciar/detener y controlar minijuegos                                          | Navegar por las preguntas del quiz                                              | Resumen de jugadores y puntuaciones                                             | Sound Pad para reproducir efectos de sonido aleatorios                          |

La pestaña de control remoto permite controlar el quiz. Están disponibles los siguientes botones:

- Leaderboard: muestra la clasificación actual. Inicialmente se muestran los 22 primeros. Al pulsar los botones Up y Down se desplaza por las puntuaciones. Al pulsar los botones E,R,T se muestran las pantallas de puntuación ampliadas (consulte [Pantallas de control de puntuación](../starting-a-quiz/the-leaderboard.md#pantallas-de-control-de-puntuaciones))

- Response Grid: muestra una cuadrícula que indica para cada jugador si acertó/falló o no respondió a la pregunta de opción múltiple actual.

- Chart: muestra un gráfico con el número de votos de cada respuesta.

- Round Scores: muestra las puntuaciones de la ronda actual.

- Round Winners: muestra el ganador de cada ronda.

- Pause/Resume: pausa/reanuda la cuenta atrás.

- Stop: finaliza la pregunta actual cuando el reloj está en pausa.

- Up/Down: desplaza la clasificación hacia arriba/abajo cuando hay más de 22 jugadores.

- Next: pasa a la siguiente diapositiva / al siguiente paso de un minijuego / al siguiente paso de las acciones de fin de pregunta (para las acciones de fin de pregunta, consulte [Acciones de fin de pregunta](../../setup/end-of-question-actions.md))

- Right/Wrong: juzga la respuesta que se dio verbalmente a una pregunta de fastest finger.

- Control de volumen: cambia de forma remota y en tiempo real el volumen de reproducción del quiz player

- Filtrado de quizzes: al usar el control remoto para conectarse a Quiz Center, ahora puede filtrar rápidamente la lista de quizzes disponibles.

!!! note

    Los botones ERT y el control de volumen solo están disponibles actualmente en Android; la versión de iOS llegará más adelante.*

1.  La pestaña de minijuegos permite iniciar minijuegos sobre la marcha. Seleccione un minijuego y pulse el botón. Avance por el minijuego haciendo clic en la tecla de flecha.

2.  La pestaña de preguntas muestra todas las preguntas, las respuestas correctas, las notas y una miniatura de las diapositivas. En la barra de herramientas inferior están disponibles los siguientes botones:

- Botón **Pause**: pausa y reanuda la cuenta atrás.

- Botón **Stop**: finaliza una pregunta cuando el temporizador está en pausa.

- Botón **Chart**: muestra un gráfico de respuestas de la pregunta actual.

- Botón **Leaderboard**: muestra las puntuaciones intermedias actuales.

- Botón de alternancia **Current/List**: alterna entre los detalles de la pregunta actual y la lista de todas las preguntas

- Botón **Next** (flecha): avanza a la siguiente diapositiva

Las diapositivas visitadas se colorean de amarillo; la pregunta actual se colorea de verde.

> Después de cada pregunta de ‘everyone answers’, la aplicación de control remoto muestra el número de jugadores que respondieron correctamente (en verde), el número de los que respondieron incorrectamente (en rojo) y el número de los que no respondieron en absoluto (en azul).

![](../../assets/images/image396.webp){ width="189" loading=lazy }

3.  La pestaña de jugadores muestra todos los jugadores y sus puntuaciones. En la parte superior están disponibles los siguientes botones:

- Actualizar la página.

- Editar un jugador: cambiar nombre, puntuación, número de mando (en caso de un mando físico)

- Añadir un jugador: nombre, puntuación, número de mando (en caso de un mando físico)

- Desactivar un jugador.

- Eliminar un jugador.

4.  La pestaña Sound Pad permite reproducir hasta 12 efectos de sonido diferentes en el quiz player. Los efectos de sonido se cargan desde una carpeta definida por el usuario que puede configurar en QuizXpress Setup (consulte [Configuración de los sonidos: la pestaña Sounds](../../setup/configuring-sounds-the-sounds-tab-page.md) para obtener más información).
