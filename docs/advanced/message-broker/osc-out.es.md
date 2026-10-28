# OSC Out

Con OSC Out usted decide qué mensaje OSC envía QuizXpress cuando ocurre algo en el quiz. Úselo para dispositivos que solo reaccionan a sus propios comandos, como una consola de iluminación ETC Eos o Ion: una respuesta correcta puede disparar el cue 20, el dedo más rápido en el mando 3 puede disparar una macro y cada nueva diapositiva puede disparar el cue con el mismo número.

El [canal de salida IP](ip-outbound.md) siempre envía los mismos mensajes fijos, como `/correct` y `/buzz 3 A`. Eso funciona para su propio software, pero una consola de iluminación ignora los mensajes que no conoce. OSC Out envía exactamente los mensajes que la consola espera, y puede usar ambos al mismo tiempo.

## Preparar una consola ETC Eos o Ion

Una consola de la familia Eos (Eos, Gio, Ion, Element, ETCnomad) solo acepta mensajes OSC que empiecen por `/eos/`. Antes de que QuizXpress pueda controlarla:

1. En los ajustes de red de la consola, marque 'UDP Strings & OSC' para el puerto de red que se conecta al ordenador con QuizXpress.
2. En Setup, en 'Show Control', active 'OSC RX' y 'String RX', y defina el 'OSC RX Port'. ETC recomienda el puerto 8000.
3. Anote la dirección IP de la consola. Envíe los mensajes a la consola principal, no a una de respaldo ni a un cliente.

Los nombres de estos ajustes difieren ligeramente entre las versiones del software Eos; el manual de ETC de su versión incluye los detalles.

## Activar OSC Out

Abra los [ajustes de Message Broker](index.md#abrir-los-ajustes-de-message-broker) y vaya a la pestaña 'OSC Out':

![La pestaña OSC Out](../../assets/images/mb-osc-out-tab.webp){ width="420" loading=lazy }

**Mode**
:   Activa o desactiva OSC Out.

**Send to**
:   La dirección IP y el puerto de recepción OSC de la consola; para una consola ETC, el 'OSC RX Port' de sus ajustes de Show Control.

**Rules**
:   Cada regla indica a QuizXpress qué mensajes enviar para un evento. 'Add...' crea una regla y 'Edit...' (o un doble clic) modifica una. Desmarque una regla para desactivarla sin eliminarla. Las flechas cambian el orden, y 'Test' envía de inmediato la regla seleccionada a la consola, de modo que puede comprobar que reacciona.

## Editar una regla

![Edición de una regla OSC](../../assets/images/mb-osc-rule.webp){ width="420" loading=lazy }

**Event**
:   Lo que sucede en el quiz, por ejemplo 'Correct answer' o 'Slide changes'. Consulte [Eventos y filtros](#eventos-y-filtros).

**Filters**
:   Algunos eventos pueden acotarse, por ejemplo 'Fastest finger' a un solo mando, o 'Slide changes' a las diapositivas de una determinada clase. Un filtro que no está marcado acepta todo.

**OSC messages**
:   Los mensajes que se enviarán, uno por línea, en el orden en que los escriba. 'Examples' inserta líneas predefinidas para ETC Eos y QLab.

**Enabled**
:   Activa o desactiva la regla.

**Test**
:   Envía los mensajes a la consola ahora. Los marcadores de posición reciben un valor de ejemplo, por ejemplo la diapositiva 1.

Mientras escribe, el editor comprueba cada línea y muestra qué está mal, por ejemplo unas comillas que faltan.

### Escribir mensajes

Escriba un mensaje como lo escribe ETC en sus manuales: la dirección, luego `=` y los argumentos, separados por comas.

| Usted escribe | QuizXpress envía |
|---|---|
| `/eos/cue/1/20/fire` | Solo la dirección, sin argumentos: dispara el cue 20 de la lista de cues 1. |
| `/eos/sub/1=1.0` | Un número decimal (`1.0`): el submaster 1 al máximo. |
| `/eos/macro/fire=5` | Un número entero (`5`): dispara la macro 5. |
| `/eos/newcmd="Chan 1 At Full#"` | Texto entre comillas dobles: escribe el comando en la línea de comandos de la consola. |
| `# finale lights` | Nada: una línea que empieza por `#` es una nota. |

El texto entre comillas dobles siempre se envía como texto, también cuando es un número (`"7"`). Sin comillas, un número con punto decimal se envía como número decimal, un número sin punto como número entero y cualquier otra cosa como texto.

### Marcadores de posición

Los marcadores de posición entre llaves se sustituyen por valores del quiz cuando se envía el mensaje. `/eos/cue/1/{slide}/fire` dispara el cue 5 cuando aparece la diapositiva 5, de modo que una sola regla cubre todo el quiz.

| Marcador de posición | Valor | Disponible para |
|---|---|---|
| `{slide}` | El número de la diapositiva actual, contado desde 1 como en Studio. | Todos los eventos |
| `{previous}` | El número de la diapositiva anterior, `0` para la primera diapositiva. | Todos los eventos |
| `{class}`, `{id}` | La clase y el id de la diapositiva actual, definidos en los metadatos de la diapositiva en Studio. | Todos los eventos |
| `{type}` | El tipo de diapositiva, por ejemplo `question`. | Todos los eventos |
| `{device}` | El número del mando o del pulsador. | Fastest finger, Keypad press |
| `{key}` | La tecla que se pulsó, por ejemplo `A`. | Keypad press |
| `{keynumber}` | La tecla como número: A = 1, B = 2 y así sucesivamente; el botón de fastest finger = 0. | Keypad press |
| `{seconds}`, `{ms}` | El tiempo restante en segundos y en milisegundos. | Countdown tick |
| `{screen}` | La pantalla, por ejemplo `quizscreen` o `finalscorescreen`. | Screen changes |
| `{command}` | El botón del mando a distancia, por ejemplo `ok` o `f1`. | Remote control button |

Un marcador de posición que no corresponde al evento se envía tal como está escrito; el editor le avisa de ello.

!!! note
    OSC Out siempre cuenta las diapositivas desde 1, como hace Studio, también cuando 'Number slides from 1' en la pestaña 'IP Outbound' está desactivado.

### Eventos y filtros

| Evento | Se dispara cuando… | Filtros |
|---|---|---|
| Slide changes | Se muestra una nueva diapositiva. | 'From slide', 'To slide', 'Slide class' |
| Screen changes | El reproductor del quiz cambia de pantalla, por ejemplo al quiz o a las puntuaciones finales. | 'Screen' |
| Countdown starts | La cuenta atrás se inicia o continúa tras una pausa. | – |
| Countdown paused | La cuenta atrás se pone en pausa. | – |
| Countdown tick | Cada segundo mientras la cuenta atrás está en marcha. | 'Seconds left' |
| Countdown ends | La cuenta atrás se detiene. | – |
| Timeout | Se agotó el tiempo de la pregunta. | – |
| Correct answer | Una respuesta se juzga correcta. | – |
| Incorrect answer | Una respuesta se juzga incorrecta. | – |
| Answer revealed | La respuesta correcta se muestra en la diapositiva, también en preguntas de votación en las que nadie juzga una respuesta. En una diapositiva Trivia Feud, cada respuesta que se da la vuelta en el tablero. | – |
| Fastest finger | Un jugador es el primero en una pregunta de fastest finger. | 'Keypad' |
| Keypad press | Se pulsa una tecla en un mando o pulsador. | 'Keypad', 'Key' (A = 1, B = 2, fastest finger = 0) |
| Remote control button | Se pulsa un botón del mando a distancia del presentador del quiz. | 'Button' |
| Quiz restarts | El quiz se reinicia. | – |
| Bingo claimed, False bingo, Bingo | Se reclama un Bingo, resulta ser falso o es válido. | – |

- 'Countdown tick' sin filtro envía sus mensajes cada segundo. Con 'Seconds left' los envía una sola vez, cuando la cuenta atrás pasa por ese momento, por ejemplo 5 segundos antes del final.
- Justo después de un fastest finger, la cuenta atrás termina. Ese 'Countdown ends' se omite, de modo que las luces pueden quedarse en el ganador.
- Los números de diapositiva en los filtros 'From slide' y 'To slide' se cuentan desde 1. El filtrado por clase de diapositiva sigue funcionando cuando reordena las diapositivas.

## Ejemplos para ETC Eos

| Qué debe ocurrir | Evento y filtro | Mensaje OSC |
|---|---|---|
| Cada diapositiva dispara el cue con su número en la lista de cues 1 | Slide changes | `/eos/cue/1/{slide}/fire` |
| Una respuesta correcta dispara el cue 20 | Correct answer | `/eos/cue/1/20/fire` |
| La revelación de cada pregunta tiene su propio aspecto, en la lista de cues 2 | Answer revealed | `/eos/cue/2/{slide}/fire` |
| Se enciende la luz del ganador | Fastest finger | `/eos/newcmd="Chan %1 At Full#",{device}` |
| Un aspecto especial para el final | Slide changes, 'Slide class' finale | `/eos/macro/99/fire` |
| Pulsar Go 5 segundos antes del final | Countdown tick, 'Seconds left' 5 | `/eos/key/go_0` |
| Atenuar el submaster 1 cuando la cuenta atrás se pone en pausa | Countdown paused | `/eos/sub/1=0.3` |

En `/eos/newcmd`, Eos sustituye `%1` por el primer argumento, aquí el número del mando, de modo que el comando pasa a ser, por ejemplo, `Chan 3 At Full`. El `#` del final funciona como la tecla Intro.

!!! tip
    Otros dispositivos funcionan del mismo modo. QLab, por ejemplo, inicia el cue 5 con `/cue/5/start`; utilice `/cue/{slide}/start` para seguir las diapositivas.

## Comprobar lo que se envía

El [registro de mensajes](index.md#registro-de-mensajes) muestra cada mensaje OSC que sale, con el evento que lo envió. Una línea que no se pudo enviar, por ejemplo porque un marcador de posición hizo que la dirección no fuera válida, aparece como un error.

![Mensajes OSC en el registro de mensajes](../../assets/images/mb-osc-message-log.webp){ loading=lazy }

!!! note
    OSC Out envía por UDP a una sola consola. La consola no responde, por lo que el registro de mensajes muestra lo que QuizXpress envió, no lo que la consola hizo con ello.
