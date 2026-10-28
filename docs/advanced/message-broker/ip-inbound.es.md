# Canal IP de entrada

Con el canal de entrada, las aplicaciones externas envían comandos de texto a QuizXpress, por ejemplo para pasar a la siguiente diapositiva, juzgar una respuesta o cambiar una puntuación. Los comandos pueden llegar por UDP, TCP o Telnet.

Configúrelo en la pestaña 'IP Inbound' de los [ajustes de Message Broker](index.md#abrir-los-ajustes-de-message-broker):

![La pestaña IP Inbound](../../assets/images/mb-ip-inbound-tab.webp){ width="420" loading=lazy }

## Ajustes

**On/Off**
:   Activa o desactiva los mensajes de entrada.

**Protocol**
:   Puntos finales para UDP, TCP y Telnet. Puede habilitar los tres al mismo tiempo, pero cada uno necesita su propio número de puerto. El puerto Telnet predeterminado es 23.

**Settings**
:   - 'Local IP address' muestra la dirección IP de este ordenador, que necesita el lado emisor.
    - 'Open the message log at start' abre el [registro de mensajes](index.md#registro-de-mensajes) cada vez que se inicia un quiz, para que pueda seguir cada comando entrante.
    - 'TCP replies with OK/ERR status' hace que cada comando TCP responda con su resultado. Consulte [Respuestas](#respuestas).

## Seguridad

De forma predeterminada, cualquier persona de la red puede enviar comandos a QuizXpress. En un local con una red Wi-Fi pública, utilice los ajustes de 'Security' para mantener el control del espectáculo. Deje un campo vacío para mantenerlo abierto.

**Listen on**
:   El adaptador de red que recibe los comandos:

    - 'All network adapters': todas las redes a las que está conectado este ordenador (el valor predeterminado).
    - 'This computer only (127.0.0.1)': solo las aplicaciones de este ordenador pueden enviar comandos.
    - Una dirección IP de este ordenador: solo la red de ese adaptador.

    Si elige una dirección y más adelante el ordenador obtiene otra, por ejemplo en otra red, la lista muestra la dirección guardada como '(not available)' y el [registro de mensajes](index.md#registro-de-mensajes) muestra un error indicando que el canal de entrada no pudo iniciarse.

**Password**
:   Cuando establece una contraseña, los comandos solo se aceptan después de que el remitente demuestre que conoce la contraseña:

    - **TCP:** envíe `login <password>` una vez después de conectarse. Tras tres contraseñas incorrectas, QuizXpress cierra la conexión.
    - **Telnet:** Telnet solicita la contraseña en cuanto se conecta.
    - **Cualquier comando, también por UDP:** añada `-pw:<password>` al comando, por ejemplo `next -pw:quiz123`. UDP no tiene una conexión en la que iniciar sesión, por lo que por UDP todos los comandos la necesitan.

    Los comandos sin la contraseña correcta se ignoran y se muestran como una advertencia en el registro de mensajes.

**Allowed senders**
:   Las direcciones IP que pueden enviar comandos, separadas por comas. Un rango se escribe con una longitud de prefijo: `192.168.1.0/24` permite de `192.168.1.0` a `192.168.1.255`. Ejemplo: `192.168.1.20, 192.168.1.30, 10.0.0.0/8`. QuizXpress ignora todo lo que procede de otras direcciones y lo muestra como 'Rejected' en el registro de mensajes. Si una entrada no es una dirección o un rango válido, la sugerencia se vuelve roja y 'OK' permanece deshabilitado hasta que la corrija.

!!! note
    Este ordenador siempre está permitido, sea cual sea lo que introduzca en 'Allowed senders'.

!!! warning
    La contraseña protege el espectáculo frente a quienes no la conocen, pero se envía como texto sin formato por la red, igual que los comandos. La contraseña se almacena como texto sin formato en los ajustes de Message Broker.

## Comandos

Estos comandos funcionan por Telnet, TCP y UDP. Telnet y TCP envían una respuesta; UDP nunca lo hace.

| Comando | Qué hace |
|---|---|
| `next` | Avanza, por ejemplo a la siguiente diapositiva. |
| `showleaderboard` | Muestra el marcador general. |
| `showresponsechart` | Muestra el gráfico de respuestas después de una pregunta de opción múltiple. |
| `judgecorrect` | Juzga como correcta una pregunta abierta o manual. |
| `judgeincorrect` | Juzga como incorrecta una pregunta abierta o manual. |
| `pausetimer` | Pausa el temporizador de la cuenta atrás. Si el temporizador ya está en pausa, no ocurre nada. |
| `resumetimer` | Reanuda el temporizador de la cuenta atrás. Si el temporizador ya está en marcha, no ocurre nada. |
| `endquiz` | Finaliza el quiz y pasa a la pantalla de puntuación final. |
| `restart` | Reinicia el quiz. |
| `goto` | Va a una diapositiva por número o por id de diapositiva, por ejemplo `goto 10` o `goto #banner1`. Los números de diapositiva empiezan en 1, como en Studio. El id es un valor de texto único que puede establecer en una diapositiva. Pause primero la cuenta atrás: mientras la cuenta atrás está en marcha, el salto se ignora. |
| `enableallplayers` | Habilita a todos los jugadores registrados. |
| `selectplayer` | Habilita al jugador del número de dispositivo indicado y excluye a todos los demás. |
| `selectplayers` | Habilita un rango de jugadores, como `1-5` o `1,2,10`, y excluye a todos los demás. |
| `addplayer` | Añade un jugador con un número de dispositivo y un nombre, por ejemplo `addplayer 1 "John Trivialta"`. |
| `resetplayers` | Elimina a todos los jugadores. |
| `addscore` | Suma puntos a la puntuación de un jugador, por número de dispositivo o nombre de equipo, por ejemplo `addscore 3 5` o `addscore "The Quizzers" -2`. |
| `setscore` | Establece la puntuación de un jugador, por número de dispositivo o nombre de equipo, por ejemplo `setscore 3 0`. |
| `setteamname` | Establece el nombre del equipo de un dispositivo, por ejemplo `setteamname 1 "John Trivialta"`. |
| `setvolume` | Establece el volumen del reproductor del quiz (0–100). |
| `buzz` | Envía un voto de un jugador, por ejemplo `buzz 1 FF` o `buzz 1 A`. Añada `-f` para forzar el voto incluso cuando la diapositiva bloquea los pulsadores. |
| `buzzwithtext` | Envía un voto de texto, para preguntas numéricas, de letra o de texto completo, por ejemplo `buzzwithtext 3 "Paris"`. Añada `-f` para forzarlo. |
| `playjoker` | Juega un comodín para un jugador: `playjoker <device> <joker>`, donde el comodín es `FreeRide`, `PointBooster` o `TimeWarp`. |
| `sendkey` | Pulsa una tecla en el reproductor del quiz, como si se hubiera escrito en el teclado, por ejemplo `sendkey Space` o `sendkey Up`. |
| `getcurrentscreen` | Devuelve la pantalla actual: `WelcomeScreen`, `SignOnScreen`, `CountdownScreen`, `QuizScreen` o `FinalScoreScreen`. |
| `getplayers` | Devuelve todos los jugadores con sus atributos (puntuación, nombre, dispositivo, etc.). Añada `-f json` o `-f osc` para elegir el formato. |
| `getquiz` | Devuelve una exportación completa del quiz en XML, sin imágenes, sonido ni vídeo. Puede ser una gran cantidad de datos. |
| `getslide` | Devuelve los detalles de una diapositiva en XML, sin imágenes, sonido ni vídeo, por ejemplo `getslide 10`. Sin número, devuelve la diapositiva actual. |
| `login` | Inicia sesión en una conexión TCP cuando hay establecida una [contraseña](#seguridad): `login <password>`. |

Escriba el texto con espacios entre comillas dobles: `setteamname 1 "The Quizzers"`. Las comillas simples también funcionan: `setteamname 1 'The Quizzers'`. Los nombres de equipo pueden contener apóstrofos y dos puntos, como `"Bart's Team"` o `12:30`. El comando en sí no distingue entre mayúsculas y minúsculas; los nombres de equipo y las respuestas conservan sus mayúsculas.

Ejemplo de salida de `getplayers`:

![Ejemplo de salida de getplayers](../../assets/images/mb-getplayers-example.webp){ loading=lazy }

Ejemplo de salida de `getslide 10`:

![Ejemplo de salida de getslide](../../assets/images/mb-getslide-example.webp){ loading=lazy }

## Respuestas

Telnet siempre responde con `OK:` o `FAILED:`, seguido de la respuesta.

Por TCP, QuizXpress envía solo el texto de respuesta de un comando que se ha ejecutado correctamente, y nada cuando falla o no tiene respuesta. Esto dificulta que una aplicación sepa cuándo una respuesta está completa. Marque 'TCP replies with OK/ERR status' para obtener una respuesta a cada comando, con este formato:

- una primera línea `OK`, o `ERR` seguida del motivo por el que falló el comando;
- para `OK`, las líneas de la respuesta;
- una última línea con solo un punto (`.`).

Una línea de respuesta que empieza con un punto recibe un punto adicional delante, de modo que su aplicación puede leer líneas hasta recibir un único `.`. Por ejemplo, `setscore 3 0` seguido de `setscore 9 5` (no existe el dispositivo 9) da como resultado:

```
OK
0
.
ERR team 9 not found
.
```

## Probar comandos con Telnet

Telnet es la forma más sencilla de probar comandos a mano o de depurar. Windows no incluye el cliente Telnet de forma predeterminada; para instalarlo:

1. Abra 'Control Panel'.
2. Abra 'Programs'.
3. Seleccione 'Turn Windows features on or off'.
4. Marque 'Telnet Client'.
5. Haga clic en 'OK'. Windows busca los archivos necesarios e instala el cliente.

A continuación, abra un símbolo del sistema y escriba `telnet localhost` (suponiendo que QuizXpress utiliza el puerto predeterminado 23). Se abre una ventana de Telnet con el indicador `qx>`. Escriba `help` para ver todos los comandos, o `help <command>` para obtener ayuda sobre un comando:

![Sesión de Telnet con el comando help](../../assets/images/mb-telnet-help.webp){ loading=lazy }

!!! tip
    Abra el [registro de mensajes](index.md#registro-de-mensajes) junto a su ventana de Telnet: muestra cada comando que recibe QuizXpress y el resultado.
