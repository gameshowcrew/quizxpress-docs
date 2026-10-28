# Referencia

Todos los manejadores, objetos, propiedades y funciones que pueden utilizar los scripts. En el editor de scripts, la plantilla enumera todos los manejadores y las sugerencias (escriba un punto o pulse Ctrl+Espacio) muestran el resto.

## Manejadores

QuizXpress llama a estas funciones cuando existen en el script de una diapositiva. Un manejador que no está definido no cambia nada.

### La diapositiva

| Manejador | Se llama cuando… |
|---|---|
| `onLoadSlide(slide)` | Se muestra la diapositiva. `slide` es la [diapositiva](#slide) actual, igual que `qx.slide`. Puede ser `async` para hacer `await` de un [`fetch()`](#funciones-globales): QuizXpress Live espera a que termine antes de mostrar la diapositiva. |
| `onUnloadSlide(slide)` | Está a punto de abandonarse la diapositiva, por cualquier motivo: siguiente, anterior o un salto desde el Director. Limpie aquí, por ejemplo detenga la música que inició. |

### La cuenta atrás

| Manejador | Se llama cuando… |
|---|---|
| `onStartCountdown()` | La cuenta atrás se inicia o se reanuda tras una pausa. |
| `onCountdownTick(secondsLeft)` | Cada segundo de la cuenta atrás. `secondsLeft` es el número que muestra el reloj. |
| `onEndCountdown(isPaused)` | La cuenta atrás se detiene. `isPaused` es `true` si la cuenta atrás se puso en pausa, `false` si terminó. |
| `onTimeout()` | Se agotó el tiempo para responder. Consulte [el final de una pregunta](working-with-quizxpress.md#responder-al-desarrollo-del-show). |

### Las respuestas

| Manejador | Se llama cuando… |
|---|---|
| `onVote(player, answer, isCorrect)` | Un equipo respondió con el mando (opción múltiple, votación). `answer` es la respuesta tal como figura en el mando, como `'A'`. `isCorrect` es `false` cuando la respuesta es incorrecta o la diapositiva no tiene respuesta correcta. También se llama cuando un equipo cambia su respuesta. |
| `onFastestFinger(player)` | Un equipo pulsó primero en una pregunta de fastest finger. |
| `onCorrectAnswer(player)` | La respuesta del equipo más rápido se juzgó correcta. |
| `onIncorrectAnswer(player)` | La respuesta del equipo más rápido se juzgó incorrecta. |
| `onScoreChanged(player, oldScore, newScore)` | La puntuación de un equipo cambió. |

`player` es un [jugador](#player).

### Qué viene a continuación

| Manejador | Se llama cuando… |
|---|---|
| `onCommandNext()` | Se da el comando 'next' (botón, tecla o mando a distancia). Devuelva `true` si el script gestionó el comando y QuizXpress debe ignorarlo; devuelva `false` para que QuizXpress lo gestione como de costumbre. |
| `onNextSlide(currentSlideNumber)` | QuizXpress está a punto de pasar a la siguiente diapositiva, y la diapositiva no tiene definido 'Next slide'. Devuelva la diapositiva a la que ir: un número (el número de diapositiva, empezando en 0), una cadena con el id de la diapositiva (por ejemplo `'#final'`), o una diapositiva de `qx.slides`. No devuelva nada para pasar a la siguiente diapositiva. |

## qx

El objeto global `qx` es el punto de entrada a QuizXpress.

| Nombre | Descripción | Ejemplo |
|---|---|---|
| `qx.slide` | La [diapositiva](#slide) actual. | `let notes = qx.slide.notes;` |
| `qx.slides` | Todas las diapositivas del quiz. | `let final = qx.slides.find(s => s.id === 'final');` |
| `qx.teams` | Todos los equipos, como [jugadores](#player). | `let votedA = qx.teams.filter(t => t.lastVote === 'A').length;` |
| `qx.leaderBoard` | Todos los equipos ordenados por puntuación, con el líder primero. | `let leader = qx.leaderBoard[0];` |
| `qx.roundLeaderBoard` | Las puntuaciones de la ronda actual (desde la última diapositiva End of Round). Cada entrada tiene `team` (un [jugador](#player)) y `roundScore`. | `let best = qx.roundLeaderBoard[0].team.name;` |
| `qx.groups` | Los nombres de los grupos demográficos. | |
| `qx["name"]` | Obtiene o define un valor global con nombre, que se conserva entre diapositivas y se muestra en una diapositiva con `[jsvar.name]`. | `qx["roundname"] = "Geography";` |
| `qx.utils.message(text)` | Escribe una línea en el archivo de registro de QuizXpress Live. | |
| `qx.sink` | El propio QuizXpress Live, vea [qx.sink](#qxsink). | `let player = qx.sink.playerFromDevice(10);` |

## slide

La diapositiva actual (`qx.slide`, o el argumento `slide` de un manejador), y las diapositivas de `qx.slides`.

| Nombre | Descripción |
|---|---|
| `slide.slideType` | El tipo de diapositiva, vea [SlideType](#slidetype). |
| `slide.slideNumber` | El número de diapositiva, empezando en 0. |
| `slide.question` | El texto de la pregunta. |
| `slide.answers` | Matriz con los textos de todas las respuestas. |
| `slide.correctAnswer` | La respuesta correcta. |
| `slide.notes` | Las notas de la diapositiva. |
| `slide.category` | La categoría (tema) de la diapositiva. |
| `slide.hasVideo` | `true` si la diapositiva tiene un vídeo. |
| `slide.hasAudio` | `true` si la diapositiva tiene audio. |
| `slide.isPictureQuestion` | `true` si es una pregunta con imagen. |
| `slide.answerTime` | El tiempo de la cuenta atrás en segundos. |
| `slide.pointsAtStart` | Puntos al inicio de la pregunta. |
| `slide.pointsAtEnd` | Puntos al final de la pregunta. |
| `slide.penaltyPointsAtStart` | Puntos de penalización (respuesta incorrecta) al inicio. |
| `slide.penaltyPointsAtEnd` | Puntos de penalización al final. |
| `slide.id` | El id de la diapositiva (sección 'Metadata' de las propiedades de la diapositiva). |
| `slide.class` | La clase de la diapositiva (sección 'Metadata' de las propiedades de la diapositiva). |
| `slide["fieldName"]` | Lee un [campo de diapositiva personalizado](../custom-data-fields.md), por ejemplo `slide["DasLightScene"]`. |
| `slide.setQuestion(text)` | Sustituye el texto de la pregunta, solo para este show. |
| `slide.setAnswers(answers)` | Sustituye las respuestas en orden (A, B, C…), solo para este show. Como máximo tantas respuestas como tenga la diapositiva. |
| `slide.setCorrectAnswer(letters)` | Define la respuesta correcta: `'B'`, o `'AC'` cuando hay más respuestas correctas. Solo para este show. |

Consulte [Cambiar la pregunta](working-with-quizxpress.md#cambiar-la-pregunta).

### SlideType

El `SlideType` global proporciona los tipos de diapositiva por nombre:

```javascript
if (slide.slideType === SlideType.Question) {
    console.log("It's a question!");
}
```

`SlideType.Question`, `TestQuestion`, `Banner` (billboard), `EndOfRound`, `Demographic`, `LastManStanding`, `AudienceResponse`, `Wager`, `Minigame`, `MajorityRules`, `JeopardyRound` (Trivia Board round), `TriviaLadderRound`, `BingoRound`, `TriviaFeud`, `SpeedRound`, `PairingQuestion`.

## player

Los objetos de `qx.teams` y `qx.leaderBoard`, el argumento `player` de los manejadores, y los devueltos por `playerFromDevice` y `winnerOfLastQuestion`.

| Nombre | Descripción |
|---|---|
| `player.name` | Obtiene o define el nombre del jugador. |
| `player.group` | El grupo demográfico del jugador. |
| `player.lastVote` | La última respuesta recibida, como `'A'`. |
| `player.keypad` | El número de mando del jugador. |
| `player.score` | Obtiene o define la puntuación actual. Consulte [Cambiar las puntuaciones](working-with-quizxpress.md#cambiar-las-puntuaciones). |
| `player.excluded` | Obtiene o define si el jugador está excluido. |
| `player.timeUsed` | Tiempo utilizado (número decimal). |
| `player.isMobilePlayer` | `true` si el jugador está conectado mediante un dispositivo móvil. |
| `player.id` | Id único (GUID) del jugador. |

## qx.sink

| Nombre | Descripción |
|---|---|
| `qx.sink.gotoSlide(slideNumber)` | Salta a una diapositiva (número empezando en 0). |
| `qx.sink.endQuiz()` | Finaliza el quiz. |
| `qx.sink.restartQuiz()` | Reinicia el quiz. |
| `qx.sink.playerFromDevice(device)` | El [jugador](#player) de un número de dispositivo. |
| `qx.sink.winnerOfLastQuestion` | El [jugador](#player) que ganó la última pregunta. |
| `qx.sink.players` | Todos los jugadores. |
| `qx.sink.quizFile` | El nombre de archivo del quiz en ejecución. |
| `qx.sink.keypads` | Acceso al subsistema de pulsadores. |
| `qx.sink.sound` | Acceso al [subsistema de sonido](#sound). |

## sound

Disponible como `qx.sink.sound`.

| Nombre | Descripción | Ejemplo |
|---|---|---|
| `loadMusic(name, filename, loop)` | Carga un archivo de sonido del disco con un nombre. | `qx.sink.sound.loadMusic("song1", "C:\\Music\\song1.mp3", false);` |
| `playMusic(name)` | Reproduce un sonido cargado, o continúa tras `pauseMusic()`. | `qx.sink.sound.playMusic("song1");` |
| `pauseMusic(name)` | Pausa la reproducción. | `qx.sink.sound.pauseMusic("song1");` |
| `stopMusic(name)` | Detiene la reproducción. | `qx.sink.sound.stopMusic("song1");` |
| `unloadMusic(name)` | Descarga el sonido y libera sus recursos. | `qx.sink.sound.unloadMusic("song1");` |
| `setMusicVolume(name, volume)` | Define el volumen de un sonido (0–100). | `qx.sink.sound.setMusicVolume("song1", 50);` |
| `setVolume(volume)` | Define el volumen de reproducción (0–100). | |
| `startPlaylist(files[], volume)` | Inicia la reproducción de una lista de canciones. | |
| `endPlaylist()` | Detiene la lista de reproducción. | |
| `playBuzzerSound(keypad)` | Reproduce el sonido del pulsador para un mando. | |

!!! tip
    En las cadenas de JavaScript, una barra invertida debe duplicarse: escriba las rutas de Windows como `"C:\\Music\\song1.mp3"`.

Detenga siempre en `onUnloadSlide()` la música que inició: el presentador del quiz puede abandonar la diapositiva en cualquier momento. Con 'Test' en Studio, las funciones de sonido no hacen nada.

## Funciones globales

| Nombre | Descripción | Ejemplo |
|---|---|---|
| `console.log(…)`, `console.info(…)`, `console.warn(…)`, `console.error(…)` | Escriben en la [consola de scripts](debugging.md). | `console.log("Votes:", votes);` |
| `fetch(url)` | Descarga una página web o la respuesta de un servicio web. Devuelve un objeto con `status` (como 200), `statusText` y `text`. Espera como máximo 10 segundos; cuando falla, lanza un error que puede capturar. Consulte [Preguntas de la web](examples.md#preguntas-de-la-web). | `let response = await fetch(url);` |
| `setTimeout(function, ms)` | Ejecuta una función una vez, tras un número de milisegundos. | `setTimeout(() => console.log('later'), 2000);` |
| `setInterval(function, ms)` | Ejecuta una función repetidamente. Devuelve un id para `clearInterval()`. Se detiene automáticamente cuando se abandona la diapositiva. | Vea el [ejemplo del reloj](examples.md#reloj). |
| `clearInterval(id)` | Detiene un `setInterval()`. | |
| `sendUDP(ip, port, message)` | Envía un mensaje de texto por UDP (sin gestión de errores). | `sendUDP("127.0.0.1", 53432, "start");` |
| `sendTCP(ip, port, message)` | Envía un mensaje de texto por TCP. | `sendTCP("127.0.0.1", 53432, "end");` |
| `sendOSC(ip, port, oscaddress, p1, [p2])` | Envía datos a un manejador OSC. | `sendOSC("127.0.0.1", 4532, "/scene1", 20);` |
| `getEnv("name")` | El valor de una variable de entorno. | `let port = getEnv("DASLIGHT_PORT");` |
| `sleep(ms)` | Espera un número de milisegundos. El show también espera, así que manténgalo breve. | |
| `alert(message)` | Muestra un cuadro de mensaje. Solo para depuración; detiene el show. Utilice `console.log()` en su lugar. | `alert("hello world");` |
