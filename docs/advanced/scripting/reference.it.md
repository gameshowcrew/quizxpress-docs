# Riferimento

Tutti i gestori, oggetti, proprietà e funzioni che gli script possono usare. Nell'editor di script, il modello elenca tutti i gestori e i suggerimenti (digitare un punto o premere Ctrl+Spazio) mostrano il resto.

## Gestori

QuizXpress chiama queste funzioni quando esistono nello script di una diapositiva. Un gestore non definito non cambia nulla.

### La diapositiva

| Gestore | Chiamato quando… |
|---|---|
| `onLoadSlide(slide)` | La diapositiva viene mostrata. `slide` è la [diapositiva](#slide) corrente, la stessa di `qx.slide`. Può essere `async` per usare `await` su un [`fetch()`](#funzioni-globali): QuizXpress Live lo attende prima di mostrare la diapositiva. |
| `onUnloadSlide(slide)` | Si sta per lasciare la diapositiva, per qualsiasi motivo: successiva, precedente o salto dal Director. Ripulire qui, ad esempio fermare la musica avviata. |

### Il conto alla rovescia

| Gestore | Chiamato quando… |
|---|---|
| `onStartCountdown()` | Il conto alla rovescia parte, o riprende dopo una pausa. |
| `onCountdownTick(secondsLeft)` | Ogni secondo del conto alla rovescia. `secondsLeft` è il numero sull'orologio. |
| `onEndCountdown(isPaused)` | Il conto alla rovescia si ferma. `isPaused` è `true` se il conto alla rovescia è stato messo in pausa, `false` se è terminato. |
| `onTimeout()` | Il tempo per rispondere è scaduto. Vedere [la fine di una domanda](working-with-quizxpress.md#reagire-allo-show). |

### Le risposte

| Gestore | Chiamato quando… |
|---|---|
| `onVote(player, answer, isCorrect)` | Una squadra ha risposto con il keypad (scelta multipla, voto). `answer` è la risposta come sul keypad, ad esempio `'A'`. `isCorrect` è `false` quando la risposta è sbagliata o la diapositiva non ha una risposta corretta. Viene chiamato anche quando una squadra cambia la risposta. |
| `onFastestFinger(player)` | Una squadra ha premuto per prima in una domanda di dito più veloce. |
| `onCorrectAnswer(player)` | La risposta della squadra più veloce è stata giudicata corretta. |
| `onIncorrectAnswer(player)` | La risposta della squadra più veloce è stata giudicata sbagliata. |
| `onScoreChanged(player, oldScore, newScore)` | Il punteggio di una squadra è cambiato. |

`player` è un [giocatore](#player).

### Cosa viene dopo

| Gestore | Chiamato quando… |
|---|---|
| `onCommandNext()` | Viene dato il comando 'next' (pulsante, tasto o telecomando). Restituire `true` se lo script ha gestito il comando e QuizXpress deve ignorarlo; restituire `false` per lasciare che QuizXpress lo gestisca come al solito. |
| `onNextSlide(currentSlideNumber)` | QuizXpress sta per passare alla diapositiva successiva, e la diapositiva non ha un 'Next slide' impostato. Restituire la diapositiva a cui andare: un numero (il numero della diapositiva, a partire da 0), una stringa con l'id della diapositiva (ad esempio `'#final'`), o una diapositiva da `qx.slides`. Non restituire nulla per passare alla diapositiva successiva. |

## qx

L'oggetto globale `qx` è il punto di ingresso a QuizXpress.

| Nome | Descrizione | Esempio |
|---|---|---|
| `qx.slide` | La [diapositiva](#slide) corrente. | `let notes = qx.slide.notes;` |
| `qx.slides` | Tutte le diapositive del quiz. | `let final = qx.slides.find(s => s.id === 'final');` |
| `qx.teams` | Tutte le squadre, come [giocatori](#player). | `let votedA = qx.teams.filter(t => t.lastVote === 'A').length;` |
| `qx.leaderBoard` | Tutte le squadre ordinate per punteggio, la prima in testa. | `let leader = qx.leaderBoard[0];` |
| `qx.roundLeaderBoard` | I punteggi del round corrente (dall'ultima diapositiva End of Round). Ogni voce ha `team` (un [giocatore](#player)) e `roundScore`. | `let best = qx.roundLeaderBoard[0].team.name;` |
| `qx.groups` | I nomi dei gruppi demografici. | |
| `qx["name"]` | Legge o imposta un valore globale con nome, mantenuto tra le diapositive e mostrato su una diapositiva con `[jsvar.name]`. | `qx["roundname"] = "Geography";` |
| `qx.utils.message(text)` | Scrive una riga nel file di log di QuizXpress Live. | |
| `qx.sink` | QuizXpress Live stesso, vedere [qx.sink](#qxsink). | `let player = qx.sink.playerFromDevice(10);` |

## slide

La diapositiva corrente (`qx.slide`, o l'argomento `slide` di un gestore), e le diapositive in `qx.slides`.

| Nome | Descrizione |
|---|---|
| `slide.slideType` | Il tipo di diapositiva, vedere [SlideType](#slidetype). |
| `slide.slideNumber` | Il numero della diapositiva, a partire da 0. |
| `slide.question` | Il testo della domanda. |
| `slide.answers` | Array con i testi di tutte le risposte. |
| `slide.correctAnswer` | La risposta corretta. |
| `slide.notes` | Le note della diapositiva. |
| `slide.category` | La categoria (argomento) della diapositiva. |
| `slide.hasVideo` | `true` se la diapositiva contiene un video. |
| `slide.hasAudio` | `true` se la diapositiva contiene audio. |
| `slide.isPictureQuestion` | `true` se si tratta di una domanda con immagine. |
| `slide.answerTime` | Il tempo del conto alla rovescia in secondi. |
| `slide.pointsAtStart` | Punti all'inizio della domanda. |
| `slide.pointsAtEnd` | Punti alla fine della domanda. |
| `slide.penaltyPointsAtStart` | Punti di penalità (risposta sbagliata) all'inizio. |
| `slide.penaltyPointsAtEnd` | Punti di penalità alla fine. |
| `slide.id` | L'id della diapositiva (sezione 'Metadata' delle proprietà della diapositiva). |
| `slide.class` | La classe della diapositiva (sezione 'Metadata' delle proprietà della diapositiva). |
| `slide["fieldName"]` | Legge un [campo diapositiva personalizzato](../custom-data-fields.md), ad esempio `slide["DasLightScene"]`. |
| `slide.setQuestion(text)` | Sostituisce il testo della domanda, solo per questo show. |
| `slide.setAnswers(answers)` | Sostituisce le risposte in ordine (A, B, C…), solo per questo show. Al massimo tante risposte quante ne ha la diapositiva. |
| `slide.setCorrectAnswer(letters)` | Imposta la risposta corretta: `'B'`, oppure `'AC'` quando più risposte sono corrette. Solo per questo show. |

Vedere [Modificare la domanda](working-with-quizxpress.md#modificare-la-domanda).

### SlideType

Il `SlideType` globale fornisce i tipi di diapositiva per nome:

```javascript
if (slide.slideType === SlideType.Question) {
    console.log("It's a question!");
}
```

`SlideType.Question`, `TestQuestion`, `Banner` (billboard), `EndOfRound`, `Demographic`, `LastManStanding`, `AudienceResponse`, `Wager`, `Minigame`, `MajorityRules`, `JeopardyRound` (round Trivia Board), `TriviaLadderRound`, `BingoRound`, `TriviaFeud`, `SpeedRound`, `PairingQuestion`.

## player

Gli oggetti in `qx.teams` e `qx.leaderBoard`, l'argomento `player` dei gestori, e quelli restituiti da `playerFromDevice` e `winnerOfLastQuestion`.

| Nome | Descrizione |
|---|---|
| `player.name` | Legge o imposta il nome del giocatore. |
| `player.group` | Il gruppo demografico del giocatore. |
| `player.lastVote` | L'ultima risposta ricevuta, ad esempio `'A'`. |
| `player.keypad` | Il numero di keypad del giocatore. |
| `player.score` | Legge o imposta il punteggio corrente. Vedere [Modificare i punteggi](working-with-quizxpress.md#modificare-i-punteggi). |
| `player.excluded` | Legge o imposta se il giocatore è escluso. |
| `player.timeUsed` | Tempo impiegato (numero decimale). |
| `player.isMobilePlayer` | `true` se il giocatore è connesso tramite un dispositivo mobile. |
| `player.id` | Id univoco (GUID) del giocatore. |

## qx.sink

| Nome | Descrizione |
|---|---|
| `qx.sink.gotoSlide(slideNumber)` | Salta a una diapositiva (numero a partire da 0). |
| `qx.sink.endQuiz()` | Termina il quiz. |
| `qx.sink.restartQuiz()` | Riavvia il quiz. |
| `qx.sink.playerFromDevice(device)` | Il [giocatore](#player) su un numero di dispositivo. |
| `qx.sink.winnerOfLastQuestion` | Il [giocatore](#player) che ha vinto l'ultima domanda. |
| `qx.sink.players` | Tutti i giocatori. |
| `qx.sink.quizFile` | Il nome del file del quiz in esecuzione. |
| `qx.sink.keypads` | Accesso al sottosistema dei buzzer. |
| `qx.sink.sound` | Accesso al [sottosistema audio](#sound). |

## sound

Disponibile come `qx.sink.sound`.

| Nome | Descrizione | Esempio |
|---|---|---|
| `loadMusic(name, filename, loop)` | Carica da disco un file audio con un nome. | `qx.sink.sound.loadMusic("song1", "C:\\Music\\song1.mp3", false);` |
| `playMusic(name)` | Riproduce un suono caricato, o riprende dopo `pauseMusic()`. | `qx.sink.sound.playMusic("song1");` |
| `pauseMusic(name)` | Mette in pausa la riproduzione. | `qx.sink.sound.pauseMusic("song1");` |
| `stopMusic(name)` | Ferma la riproduzione. | `qx.sink.sound.stopMusic("song1");` |
| `unloadMusic(name)` | Scarica il suono e libera le sue risorse. | `qx.sink.sound.unloadMusic("song1");` |
| `setMusicVolume(name, volume)` | Imposta il volume di un singolo suono (0–100). | `qx.sink.sound.setMusicVolume("song1", 50);` |
| `setVolume(volume)` | Imposta il volume di riproduzione (0–100). | |
| `startPlaylist(files[], volume)` | Avvia la riproduzione di un elenco di brani. | |
| `endPlaylist()` | Ferma la playlist. | |
| `playBuzzerSound(keypad)` | Riproduce il suono del buzzer per un keypad. | |

!!! tip
    Nelle stringhe JavaScript, una barra rovesciata deve essere raddoppiata: scrivere i percorsi Windows come `"C:\\Music\\song1.mp3"`.

Fermare sempre in `onUnloadSlide()` la musica avviata: il conduttore del quiz può lasciare la diapositiva in qualsiasi momento. Con 'Test' in Studio, le funzioni audio non fanno nulla.

## Funzioni globali

| Nome | Descrizione | Esempio |
|---|---|---|
| `console.log(…)`, `console.info(…)`, `console.warn(…)`, `console.error(…)` | Scrivono nella [console di script](debugging.md). | `console.log("Votes:", votes);` |
| `fetch(url)` | Scarica una pagina web o la risposta di un servizio web. Restituisce un oggetto con `status` (ad esempio 200), `statusText` e `text`. Attende al massimo 10 secondi; in caso di errore, genera un errore che è possibile intercettare. Vedere [Domande dal web](examples.md#domande-dal-web). | `let response = await fetch(url);` |
| `setTimeout(function, ms)` | Esegue una funzione una volta, dopo un certo numero di millisecondi. | `setTimeout(() => console.log('later'), 2000);` |
| `setInterval(function, ms)` | Esegue una funzione ripetutamente. Restituisce un id per `clearInterval()`. Si ferma automaticamente quando si lascia la diapositiva. | Vedere l'[esempio Orologio](examples.md#orologio). |
| `clearInterval(id)` | Ferma un `setInterval()`. | |
| `sendUDP(ip, port, message)` | Invia un messaggio di testo via UDP (senza gestione degli errori). | `sendUDP("127.0.0.1", 53432, "start");` |
| `sendTCP(ip, port, message)` | Invia un messaggio di testo via TCP. | `sendTCP("127.0.0.1", 53432, "end");` |
| `sendOSC(ip, port, oscaddress, p1, [p2])` | Invia dati a un gestore OSC. | `sendOSC("127.0.0.1", 4532, "/scene1", 20);` |
| `getEnv("name")` | Il valore di una variabile d'ambiente. | `let port = getEnv("DASLIGHT_PORT");` |
| `sleep(ms)` | Attende un certo numero di millisecondi. Anche lo show attende, quindi restare brevi. | |
| `alert(message)` | Mostra una finestra di messaggio. Solo per il debug; blocca lo show. Usare invece `console.log()`. | `alert("hello world");` |
