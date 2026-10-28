# MIDI y DMX

QuizXpress puede controlar dispositivos externos mediante MIDI. Un ejemplo típico es un controlador de luces DMX: cuando ocurre algo en el quiz, como una respuesta correcta o el final de la cuenta atrás, QuizXpress envía mensajes MIDI que cambian las luces a una escena acorde.

## Activar la compatibilidad con MIDI

Abra los [ajustes de Message Broker](index.md#abrir-los-ajustes-de-message-broker), active la compatibilidad con MIDI y haga clic en 'Configure':

![Ajustes de Message Broker](../../assets/images/mb-settings.webp){ width="300" loading=lazy }

Se abre la pantalla de configuración de MIDI:

![Pantalla de configuración de MIDI](../../assets/images/mb-midi-configuration.webp){ loading=lazy }

- **Arriba:** seleccione el dispositivo de entrada y de salida MIDI. El dispositivo de entrada solo se utiliza para la función 'Learn' (véase más abajo). El dispositivo de salida recibe los mensajes MIDI que QuizXpress envía cuando ocurren eventos en el quiz.
- **Centro, izquierda:** los disparadores, que son eventos que ocurren dentro de QuizXpress.
- **Centro, derecha:** los mensajes MIDI que se envían para el disparador seleccionado.

## Añadir un disparador

Haga clic en el botón 'Add' de la izquierda y elija el tipo de disparador:

![Añadir un disparador](../../assets/images/mb-midi-add-trigger.webp){ width="300" loading=lazy }

Algunos disparadores tienen un parámetro opcional que acota cuándo se activan. En este ejemplo, el disparador solo se activa cuando el pulsador 2 gana una pregunta de dedo más rápido:

![Un disparador Fastest Finger filtrado por el pulsador 2](../../assets/images/mb-midi-trigger-fastest-finger.webp){ width="300" loading=lazy }

### Disparadores disponibles

| Disparador | Se activa cuando… |
|---|---|
| Timeout | La pregunta actual agota su tiempo, por ejemplo porque nadie respondió a tiempo. |
| Correct Answer | El presentador del quiz juzga correcta una respuesta. |
| Incorrect Answer | El presentador del quiz juzga incorrecta una respuesta. |
| Answer Revealed | La respuesta correcta se muestra en la diapositiva. En una diapositiva de Trivia Feud, cada respuesta que se da la vuelta en el tablero. |
| Start Countdown | Se inicia el temporizador de la cuenta atrás. |
| End Countdown | Termina el temporizador de la cuenta atrás. |
| Pause Countdown | El presentador del quiz pausa el temporizador de la cuenta atrás. |
| Countdown Tick | Avanza el temporizador de la cuenta atrás. Puede filtrar por el número de segundos restantes. |
| Restart | El quiz se reinicia y vuelve a la pantalla de bienvenida. |
| Fastest Finger | Un jugador es el primero en responder a una pregunta de dedo más rápido. Puede filtrar por el número de dispositivo (mando o pulsador). |
| Screen Changed | Cambia la pantalla, por ejemplo pantalla de bienvenida → pantalla de registro de pulsadores → pantalla del quiz → pantalla de puntuación. Puede filtrar por el tipo de pantalla. |
| Slide Changed | El quiz avanza a otra diapositiva. Puede filtrar por el número de diapositiva de origen/destino o por la clase de la diapositiva. Los números de diapositiva empiezan en 0 (la primera diapositiva es la 0), a menos que 'Number slides from 1' esté marcado en la pestaña [IP Outbound](ip-outbound.md#ajustes). |
| Remote Command | Llega un comando del mando a distancia del presentador del quiz. |
| Receive Keypad | Llega una señal de un mando o pulsador. Puede filtrar por el número de mando y la tecla (A = 1, B = 2, etc.; dedo más rápido = 0). |
| Claim Bingo | Un jugador reclama Bingo. |
| False Bingo | Un Bingo reclamado no supera la validación. |
| Bingo | Un Bingo reclamado es válido y el jugador gana. |

!!! tip
    Filtrar 'Slide Changed' por una **clase de diapositiva** es más robusto que filtrar por números de diapositiva. Usted asigna una clase a una diapositiva en QuizXpress Studio; si más adelante reordena sus diapositivas, los disparadores basados en clase siguen funcionando, mientras que los basados en números habría que actualizarlos.

## Definir los mensajes MIDI

Para cada disparador, defina la secuencia de mensajes MIDI que se enviarán al dispositivo de salida (la lista de la derecha). Hay dos maneras de hacerlo.

**Aprenderlos desde su controlador (recomendado).** Haga clic en 'Learn' (se pone en verde) y, a continuación, ajuste su controlador de luces a la escena que desee. Los mensajes MIDI aparecen en la lista a medida que avanza. Haga clic de nuevo en 'Learn' cuando termine.

**Introducirlos manualmente.** Haga clic en el botón 'Add' de la derecha:

![Añadir un mensaje MIDI manualmente](../../assets/images/mb-midi-add-message.webp){ width="300" loading=lazy }

Haga doble clic en un mensaje o disparador de la lista para editarlo.

Haga clic en 'Test' para enviar los mensajes seleccionados al dispositivo de salida y comprobar que el controlador responde correctamente.

Cuando todo esté configurado, cierre la pantalla de configuración de MIDI y luego cierre los ajustes de Message Broker con 'OK'. A partir de ese momento, QuizXpress envía los mensajes MIDI al dispositivo de salida seleccionado.

## Probar sin hardware MIDI

Dos herramientas gratuitas le permiten probar sin ningún dispositivo MIDI físico:

1. **[loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html)** crea un dispositivo MIDI virtual, de modo que los programas pueden comunicarse mediante MIDI entre sí sin hardware.

    ![loopMIDI](../../assets/images/mb-loopmidi.webp){ width="500" loading=lazy }

2. **[Virtual MIDI Sliders](http://www.granucon.com/SoftwarePages/Vms.aspx)** muestra cómo QuizXpress controla un controlador MIDI genérico. La función 'Learn' también funciona con este dispositivo virtual.

    ![Virtual MIDI Sliders](../../assets/images/mb-virtual-midi-sliders.webp){ loading=lazy }
