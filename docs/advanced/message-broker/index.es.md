# Message Broker

Message Broker es un plugin avanzado de QuizXpress que intercambia datos con aplicaciones y dispositivos externos, como controladores de luces MIDI y DMX. Utilícelo para crear efectos que respondan a lo que ocurre en el quiz, configurar salas de quiz, controlar la iluminación, crear formatos de juego personalizados o construir sus propios módulos externos en entornos como [Cycling ‘74 Max](https://cycling74.com/).

Esta sección describe QuizXpress 8.5 y versiones posteriores.

!!! note
    Message Broker es un complemento con licencia para QuizXpress y requiere una compra única.

## Canales de datos

- **TCP/UDP:** comunicación de entrada y de salida mediante mensajes de texto sin formato (ASCII o UTF-8). Consulte [Canal IP de entrada](ip-inbound.md) y [Canal IP de salida](ip-outbound.md).
- **Telnet:** envíe comandos y reciba datos directamente desde una consola Telnet. Consulte [Canal IP de entrada](ip-inbound.md).
- **OSC:** el canal de salida también puede enviar mensajes de [Open Sound Control](ip-outbound.md#ajustes), para herramientas como Max, QLab y TouchOSC. Para enviar los mensajes exactos que espera una consola de iluminación u otro dispositivo, como una ETC Eos o Ion, utilice [OSC Out](osc-out.md).
- **MIDI:** los eventos de QuizXpress activan mensajes MIDI configurables, que se utilizan a menudo para controlar mesas de luces DMX. Consulte [MIDI y DMX](midi-and-dmx.md).

Esta vista general muestra cómo está todo conectado:

![Cómo Message Broker conecta QuizXpress con dispositivos externos](../../assets/images/mb-overview-diagram.webp){ loading=lazy }

## Abrir los ajustes de Message Broker

Message Broker se configura desde QuizXpress Director mientras se ejecuta un quiz. Inicie un quiz, pulse la tecla 'D' para abrir [QuizXpress Director](../../live/quizxpress-director/index.md) y vaya a la pestaña 'Extensions':

![La pestaña Extensions en QuizXpress Director](../../assets/images/mb-director-extensions.webp){ loading=lazy }

!!! warning
    Cierre los ajustes de Message Broker con 'OK', no con 'Cancel'. 'Cancel' descarta todos sus cambios.

## Registro de mensajes

El registro de mensajes muestra todo lo que hace Message Broker mientras se ejecuta el quiz: los comandos que llegan con su resultado, los mensajes que salen por UDP, OSC y MIDI, y lo que hacen los servidores (escucha, conexiones, inicios de sesión y remitentes rechazados). Úselo para configurar y probar una conexión, o para averiguar por qué una aplicación externa no responde como se espera.

Ábralo con 'Message log...' en la parte inferior de los ajustes de Message Broker. Para abrirlo automáticamente cada vez que se inicia un quiz, marque 'Open the message log at start' en la pestaña 'IP Inbound'.

![El registro de mensajes](../../assets/images/mb-message-log.webp){ loading=lazy }

- El icono delante de cada línea indica de qué se trata: una flecha azul hacia abajo para un comando entrante, una flecha verde hacia arriba para un mensaje saliente, y un signo de información, advertencia o error para todo lo demás.
- Los comandos entrantes muestran su resultado a la derecha: 'OK' con la respuesta, o 'ERR' con el motivo por el que falló el comando.
- Escriba en el cuadro de filtro para mostrar solo las líneas que contienen ese texto, por ejemplo un comando, un mensaje o una dirección IP.
- 'Incoming' y 'Outgoing' muestran u ocultan comandos y mensajes. 'Timer ticks' muestra los ticks de la cuenta atrás y los latidos (heartbeats), que se envían cada segundo y están ocultos de forma predeterminada.
- 'Pause' impide que aparezcan nuevas líneas para que pueda leer la lista; cuenta las líneas nuevas, que aparecen al hacer clic de nuevo en 'Pause'.
- Haga clic en una línea para ver su texto completo y su respuesta debajo de la lista. 'Copy' copia las líneas visibles, por ejemplo para enviarlas a soporte. 'Clear' vacía el registro.

El registro conserva las últimas 5000 líneas. Las contraseñas nunca aparecen en él: se muestran como `****`.

!!! note
    El registro de mensajes se abre en la pantalla de QuizXpress Director. Cuando se abre al inicio de un quiz, antes de que se muestre Director, se abre en una pantalla sin el quiz, de modo que puede mantenerlo abierto durante un espectáculo en directo. Con una sola pantalla, se abre encima del quiz.
