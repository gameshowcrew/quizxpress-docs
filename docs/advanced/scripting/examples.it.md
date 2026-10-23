# Esempi

## Quiz di esempio

I nostri [script di esempio su GitHub](https://github.com/gameshowcrew/samples/tree/main/script) sono quiz pronti all'uso, ciascuno con il proprio script in un file separato e una spiegazione. Anche l'editor di script rimanda a essi: 'Example scripts on GitHub' in alto a destra. Dal più semplice al più elaborato:

| Esempio | Cosa mostra | Funzioni di script |
|---|---|---|
| [Orologio in tempo reale](https://github.com/gameshowcrew/samples/tree/main/script/live_clock) | Un orologio in tempo reale e un conto alla rovescia verso l'inizio del quiz su una diapositiva billboard | `setInterval()`, `[jsvar.name]` su una diapositiva |
| [Contatore dei voti](https://github.com/gameshowcrew/samples/tree/main/script/vote_counter) | "7 squadre su 12 hanno risposto" mentre il conto alla rovescia è in corso | `onVote()`, `qx.teams` |
| [Sbrigatevi!](https://github.com/gameshowcrew/samples/tree/main/script/countdown_hurry_up) | "Sbrigatevi!" negli ultimi secondi, musica di tensione facoltativa, "Tempo scaduto!" | `onCountdownTick()`, `onTimeout()`, `qx.sink.sound` |
| [Ordine casuale delle domande](https://github.com/gameshowcrew/samples/tree/main/script/random_question_order) | 5 domande casuali da un insieme, in ordine casuale | `onNextSlide()`, valori che restano tra una diapositiva e l'altra |
| [Domande dal web](https://github.com/gameshowcrew/samples/tree/main/script/fetching_dynamic_content) | Una nuova domanda dall'Open Trivia Database ogni volta | `fetch()`, `slide.setQuestion()`/`setAnswers()` |
| [Bonus serie vincente](https://github.com/gameshowcrew/samples/tree/main/script/hot_streak_bonus) | Punti bonus per 3 risposte corrette di fila e una tabella punteggi delle serie | tutto quanto sopra, modifica dei punteggi |

Per provarne uno, scaricare il file `.qx`, aprirlo in Quiz Studio e guardare la proprietà 'Script' delle sue diapositive, oppure eseguirlo.

Gli esempi qui sotto sono brevi script da copiare nel proprio quiz.

## Orologio

Mostra l'ora corrente su una diapositiva, aggiornata ogni secondo, usando un [simbolo di testo `[jsvar]`](working-with-quizxpress.md#mostrare-i-valori-dello-script-su-una-diapositiva).

Creare una diapositiva billboard e sostituire il testo della domanda con il simbolo `[jsvar.time]`:

![Diapositiva billboard con il simbolo jsvar.time](../../assets/images/js-clock-slide.webp){ loading=lazy }

Assegnare alla diapositiva questo script:

```javascript
function onLoadSlide(slide) {
    showTime();
    setInterval(showTime, 1000);     // chiama showTime() ogni secondo
}

function showTime() {
    qx["time"] = new Date().toLocaleTimeString();
}
```

`onLoadSlide()` mostra l'ora e avvia un timer che la aggiorna ogni secondo. Il timer si ferma da solo quando si lascia la diapositiva.

## Riprodurre un MP3

Carica un file MP3 e lo riproduce due secondi dopo la fine del conto alla rovescia:

```javascript
qx.sink.sound.loadMusic('levels', 'C:\\Music\\Jingles\\Levels.mp3', false);

function onEndCountdown(isPaused) {
    if (isPaused)
        return;
    // avvia dopo 2 secondi
    setTimeout(() => {
        qx.sink.sound.playMusic('levels');
    }, 2000);
}

function onUnloadSlide(slide) {
    qx.sink.sound.stopMusic('levels');
    qx.sink.sound.unloadMusic('levels');
}
```

## Passare a una diapositiva in base ai voti

Usa `onNextSlide()` per proseguire con il round A o il round B, a seconda di quale risposta ha ottenuto più voti. La prima diapositiva di ogni round ha la classe di diapositiva `roundA` o `roundB`.

!!! tip
    Per i casi semplici, l'[instradamento delle diapositive](../../studio/other-functionality/slide-routing.md) integrato fa lo stesso senza script.

```javascript
// Vai alla diapositiva con classe 'roundA' o 'roundB',
// a seconda di quale risposta ha ottenuto più voti
function onNextSlide(currentSlideNumber) {
    let slides = qx.slides;
    let roundA = slides.find((slide) => slide.class === 'roundA');
    let roundB = slides.find((slide) => slide.class === 'roundB');

    if (!roundA || !roundB) {
        console.error('round A or round B not found!');
        return;     // semplicemente la diapositiva successiva
    }

    let teams = qx.teams;
    let votedA = teams.filter(t => t.lastVote === 'A').length;
    let votedB = teams.filter(t => t.lastVote === 'B').length;

    if (votedB > votedA)
        return roundB.slideNumber;
    else
        return roundA.slideNumber;
}
```

## Domande dal web

Usa `fetch()` per ottenere una nuova domanda dall'[Open Trivia Database](https://opentdb.com) ogni volta che la diapositiva viene mostrata, e la inserisce nella diapositiva. Assegnare questo script a una diapositiva a scelta multipla con 4 risposte; quanto digitato in Studio viene usato quando non c'è connessione a internet.

```javascript
async function onLoadSlide(slide) {
    let response;
    try {
        response = await fetch('https://opentdb.com/api.php?amount=1&type=multiple&encode=url3986');
    } catch (error) {
        console.warn('No question, the slide stays as it is.', error.message);
        return;
    }

    const trivia = JSON.parse(response.text).results[0];
    const answers = trivia.incorrect_answers.map(answer => decodeURIComponent(answer));

    // la risposta corretta in una posizione casuale
    const position = Math.floor(Math.random() * 4);
    answers.splice(position, 0, decodeURIComponent(trivia.correct_answer));

    slide.setQuestion(decodeURIComponent(trivia.question));
    slide.setAnswers(answers);
    slide.setCorrectAnswer('ABCD'[position]);

    console.log('Correct answer: ' + 'ABCD'[position]);   // per il conduttore del quiz
}
```

QuizXpress Live attende il download prima di mostrare la diapositiva, al massimo 10 secondi. L'[esempio completo](https://github.com/gameshowcrew/samples/tree/main/script/fetching_dynamic_content) sceglie anche una categoria e una difficoltà, e gestisce gli errori del servizio.

## Selezionare una squadra a caso

Sceglie una squadra a caso, mostra la selezione sullo schermo come in una lotteria, e poi esclude tutte le altre squadre per la domanda successiva.

Creare una diapositiva con il simbolo di testo `[jsvar.selected-team]`, che mostra la selezione mentre avviene:

![Diapositiva con il simbolo jsvar.selected-team](../../assets/images/js-random-team-slide.webp){ loading=lazy }

Assegnare alla diapositiva questo script:

```javascript
function onLoadSlide(slide) {
    // assicurarsi che tutte le squadre siano attive
    qx.teams.forEach((team) => {
        team.excluded = false;
    });
    qx["selected-team"] = "...";
    randomize(50);
}

function randomize(start) {
    function step(i) {
        if (i >= 0) {
            // scegliere una squadra a caso
            var randomIndex = Math.floor(Math.random() * qx.teams.length);
            var selectedTeam = qx.teams[randomIndex];

            if (i === 0) {
                // mostrare il vincitore
                qx["selected-team"] = "*** " + selectedTeam.name + " ***";
                qx["playing-team"] = selectedTeam.name;

                // escludere tutte le altre squadre
                qx.teams.forEach((team) => {
                    if (team != selectedTeam)
                        team.excluded = true;
                });
            }
            else {
                // mostrare questa squadra e programmare il passo successivo
                qx["selected-team"] = selectedTeam.name;
                setTimeout(() => step(i - 1), 750 * 1 / i);
            }
        }
    }
    step(start);
}
```

La diapositiva mostra un nome di squadra 50 volte, rallentando via via, poi mostra la squadra scelta tra `***` ed esclude tutti gli altri giocatori per la domanda successiva. Il nome della squadra scelta viene salvato anche in `playing-team`, così da poterlo mostrare nella diapositiva successiva con `[jsvar.playing-team]`.
