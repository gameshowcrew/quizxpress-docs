# Referentie

Alle handlers, objecten, eigenschappen en functies die scripts kunnen gebruiken. In de scripteditor toont het sjabloon alle handlers en de suggesties (typ een punt of druk op Ctrl+Spatie) tonen de rest.

## Handlers

QuizXpress roept deze functies aan wanneer ze in het script van een dia voorkomen. Een handler die niet is gedefinieerd, verandert niets.

### De dia

| Handler | Wordt aangeroepen wanneer… |
|---|---|
| `onLoadSlide(slide)` | De dia wordt getoond. `slide` is de huidige [dia](#slide), hetzelfde als `qx.slide`. Kan `async` zijn om een [`fetch()`](#globale-functies) af te wachten met `await`: QuizXpress Live wacht erop voordat de dia wordt getoond. |
| `onUnloadSlide(slide)` | De dia staat op het punt te worden verlaten, om welke reden dan ook: volgende, vorige of een sprong vanuit de Director. Ruim hier op, bijvoorbeeld door de muziek te stoppen die u hebt gestart. |

### Het aftellen

| Handler | Wordt aangeroepen wanneer… |
|---|---|
| `onStartCountdown()` | Het aftellen begint, of wordt hervat na een pauze. |
| `onCountdownTick(secondsLeft)` | Elke seconde van het aftellen. `secondsLeft` is het getal op de klok. |
| `onEndCountdown(isPaused)` | Het aftellen stopt. `isPaused` is `true` als het aftellen werd gepauzeerd, `false` als het is afgelopen. |
| `onTimeout()` | De antwoordtijd is om. Zie [het einde van een vraag](working-with-quizxpress.md#reageren-op-de-show). |

### De antwoorden

| Handler | Wordt aangeroepen wanneer… |
|---|---|
| `onVote(player, answer, isCorrect)` | Een team heeft geantwoord met het keypad (meerkeuze, stemmen). `answer` is het antwoord zoals op het keypad, bijvoorbeeld `'A'`. `isCorrect` is `false` wanneer het antwoord onjuist is of de dia geen juist antwoord heeft. Wordt ook aangeroepen wanneer een team zijn antwoord wijzigt. |
| `onFastestFinger(player)` | Een team drukte als eerste bij een vraag van het type snelste vinger. |
| `onCorrectAnswer(player)` | Het antwoord van het snelste team is juist beoordeeld. |
| `onIncorrectAnswer(player)` | Het antwoord van het snelste team is onjuist beoordeeld. |
| `onScoreChanged(player, oldScore, newScore)` | De score van een team is veranderd. |

`player` is een [speler](#player).

### Wat volgt

| Handler | Wordt aangeroepen wanneer… |
|---|---|
| `onCommandNext()` | Het commando 'volgende' wordt gegeven (knop, toets of afstandsbediening). Geef `true` terug als het script het commando heeft afgehandeld en QuizXpress het moet negeren; geef `false` terug om QuizXpress het zoals gewoonlijk te laten afhandelen. |
| `onNextSlide(currentSlideNumber)` | QuizXpress staat op het punt naar de volgende dia te gaan en de dia heeft geen 'Volgende slide' ingesteld. Geef de dia terug waarnaar moet worden gegaan: een getal (het diagnummer, beginnend bij 0), een tekenreeks met de dia-id (bijvoorbeeld `'#final'`) of een dia uit `qx.slides`. Geef niets terug om naar de volgende dia te gaan. |

## qx

Het globale object `qx` is het toegangspunt tot QuizXpress.

| Naam | Beschrijving | Voorbeeld |
|---|---|---|
| `qx.slide` | De huidige [dia](#slide). | `let notes = qx.slide.notes;` |
| `qx.slides` | Alle dia's in de quiz. | `let final = qx.slides.find(s => s.id === 'final');` |
| `qx.teams` | Alle teams, als [spelers](#player). | `let votedA = qx.teams.filter(t => t.lastVote === 'A').length;` |
| `qx.leaderBoard` | Alle teams gesorteerd op score, de leider eerst. | `let leader = qx.leaderBoard[0];` |
| `qx.roundLeaderBoard` | De scores van de huidige ronde (sinds de laatste dia Einde ronde). Elk item heeft `team` (een [speler](#player)) en `roundScore`. | `let best = qx.roundLeaderBoard[0].team.name;` |
| `qx.groups` | De namen van de demografische groepen. | |
| `qx["name"]` | Een globale benoemde waarde ophalen of instellen, die behouden blijft tussen dia's en op een dia wordt getoond met `[jsvar.name]`. | `qx["roundname"] = "Geography";` |
| `qx.utils.message(text)` | Schrijf een regel naar het logbestand van QuizXpress Live. | |
| `qx.sink` | QuizXpress Live zelf, zie [qx.sink](#qxsink). | `let player = qx.sink.playerFromDevice(10);` |

## slide

De huidige dia (`qx.slide`, of het argument `slide` van een handler) en de dia's in `qx.slides`.

| Naam | Beschrijving |
|---|---|
| `slide.slideType` | Het type dia, zie [SlideType](#slidetype). |
| `slide.slideNumber` | Het diagnummer, beginnend bij 0. |
| `slide.question` | De tekst van de vraag. |
| `slide.answers` | Array met de teksten van alle antwoorden. |
| `slide.correctAnswer` | Het juiste antwoord. |
| `slide.notes` | De dianotities. |
| `slide.category` | De categorie (het onderwerp) van de dia. |
| `slide.hasVideo` | `true` als de dia een video heeft. |
| `slide.hasAudio` | `true` als de dia audio heeft. |
| `slide.isPictureQuestion` | `true` als dit een beeldvraag is. |
| `slide.answerTime` | De aftelduur in seconden. |
| `slide.pointsAtStart` | Punten aan het begin van de vraag. |
| `slide.pointsAtEnd` | Punten aan het einde van de vraag. |
| `slide.penaltyPointsAtStart` | Strafpunten (onjuist antwoord) aan het begin. |
| `slide.penaltyPointsAtEnd` | Strafpunten aan het einde. |
| `slide.id` | De dia-id (sectie 'Metagegevens' van de diaeigenschappen). |
| `slide.class` | De diaklasse (sectie 'Metagegevens' van de diaeigenschappen). |
| `slide["fieldName"]` | Lees een [aangepast diaveld](../custom-data-fields.md), bijvoorbeeld `slide["DasLightScene"]`. |
| `slide.setQuestion(text)` | Vervang de vraagtekst, alleen voor deze show. |
| `slide.setAnswers(answers)` | Vervang de antwoorden op volgorde (A, B, C…), alleen voor deze show. Maximaal zoveel antwoorden als de dia heeft. |
| `slide.setCorrectAnswer(letters)` | Stel het juiste antwoord in: `'B'`, of `'AC'` wanneer meer antwoorden juist zijn. Alleen voor deze show. |

Zie [De vraag wijzigen](working-with-quizxpress.md#de-vraag-wijzigen).

### SlideType

Het globale `SlideType` geeft de diatypen bij naam:

```javascript
if (slide.slideType === SlideType.Question) {
    console.log("It's a question!");
}
```

`SlideType.Question`, `TestQuestion`, `Banner` (billboard), `EndOfRound`, `Demographic`, `LastManStanding`, `AudienceResponse`, `Wager`, `Minigame`, `MajorityRules`, `JeopardyRound` (ronde Trivia Bord), `TriviaLadderRound`, `BingoRound`, `TriviaFeud`, `SpeedRound`, `PairingQuestion`.

## player

De objecten in `qx.teams` en `qx.leaderBoard`, het argument `player` van handlers, en de objecten die `playerFromDevice` en `winnerOfLastQuestion` teruggeven.

| Naam | Beschrijving |
|---|---|
| `player.name` | De naam van de speler ophalen of instellen. |
| `player.group` | De demografische groep van de speler. |
| `player.lastVote` | Het laatst ontvangen antwoord, bijvoorbeeld `'A'`. |
| `player.keypad` | Het keypadnummer van de speler. |
| `player.score` | De huidige score ophalen of instellen. Zie [Scores wijzigen](working-with-quizxpress.md#scores-wijzigen). |
| `player.excluded` | Ophalen of instellen of de speler is uitgesloten. |
| `player.timeUsed` | Gebruikte tijd (decimaal getal). |
| `player.isMobilePlayer` | `true` als de speler is verbonden via een mobiel apparaat. |
| `player.id` | Unieke id (GUID) van de speler. |

## qx.sink

| Naam | Beschrijving |
|---|---|
| `qx.sink.gotoSlide(slideNumber)` | Spring naar een dia (nummer beginnend bij 0). |
| `qx.sink.endQuiz()` | Beëindig de quiz. |
| `qx.sink.restartQuiz()` | Start de quiz opnieuw. |
| `qx.sink.playerFromDevice(device)` | De [speler](#player) op een apparaatnummer. |
| `qx.sink.winnerOfLastQuestion` | De [speler](#player) die de laatste vraag won. |
| `qx.sink.players` | Alle spelers. |
| `qx.sink.quizFile` | De bestandsnaam van de lopende quiz. |
| `qx.sink.keypads` | Toegang tot het buzzersubsysteem. |
| `qx.sink.sound` | Toegang tot het [geluidssubsysteem](#sound). |

## sound

Beschikbaar als `qx.sink.sound`.

| Naam | Beschrijving | Voorbeeld |
|---|---|---|
| `loadMusic(name, filename, loop)` | Laad een geluidsbestand van schijf onder een naam. | `qx.sink.sound.loadMusic("song1", "C:\\Music\\song1.mp3", false);` |
| `playMusic(name)` | Speel een geladen geluid af, of ga verder na `pauseMusic()`. | `qx.sink.sound.playMusic("song1");` |
| `pauseMusic(name)` | Onderbreek het afspelen. | `qx.sink.sound.pauseMusic("song1");` |
| `stopMusic(name)` | Stop het afspelen. | `qx.sink.sound.stopMusic("song1");` |
| `unloadMusic(name)` | Laad het geluid uit en geef de bronnen vrij. | `qx.sink.sound.unloadMusic("song1");` |
| `setMusicVolume(name, volume)` | Stel het volume van één geluid in (0–100). | `qx.sink.sound.setMusicVolume("song1", 50);` |
| `setVolume(volume)` | Stel het afspeelvolume in (0–100). | |
| `startPlaylist(files[], volume)` | Begin met het afspelen van een lijst nummers. | |
| `endPlaylist()` | Stop de afspeellijst. | |
| `playBuzzerSound(keypad)` | Speel het buzzergeluid voor een keypad af. | |

!!! tip
    In JavaScript-tekenreeksen moet een backslash worden verdubbeld: schrijf Windows-paden als `"C:\\Music\\song1.mp3"`.

Stop de muziek die u hebt gestart altijd in `onUnloadSlide()`: de quizmaster kan de dia op elk moment verlaten. Met 'Testen' in Studio doen de geluidsfuncties niets.

## Globale functies

| Naam | Beschrijving | Voorbeeld |
|---|---|---|
| `console.log(…)`, `console.info(…)`, `console.warn(…)`, `console.error(…)` | Schrijf naar de [scriptconsole](debugging.md). | `console.log("Votes:", votes);` |
| `fetch(url)` | Download een webpagina of het antwoord van een webservice. Geeft een object met `status` (zoals 200), `statusText` en `text`. Wacht maximaal 10 seconden; wanneer het mislukt, geeft het een fout die u kunt afvangen. Zie [Vragen van het web](examples.md#vragen-van-het-web). | `let response = await fetch(url);` |
| `setTimeout(function, ms)` | Voer een functie eenmalig uit, na een aantal milliseconden. | `setTimeout(() => console.log('later'), 2000);` |
| `setInterval(function, ms)` | Voer een functie herhaaldelijk uit. Geeft een id terug voor `clearInterval()`. Stopt automatisch wanneer de dia wordt verlaten. | Zie het [Klok-voorbeeld](examples.md#klok). |
| `clearInterval(id)` | Stop een `setInterval()`. | |
| `sendUDP(ip, port, message)` | Verstuur een tekstbericht via UDP (geen foutafhandeling). | `sendUDP("127.0.0.1", 53432, "start");` |
| `sendTCP(ip, port, message)` | Verstuur een tekstbericht via TCP. | `sendTCP("127.0.0.1", 53432, "end");` |
| `sendOSC(ip, port, oscaddress, p1, [p2])` | Verstuur gegevens naar een OSC-handler. | `sendOSC("127.0.0.1", 4532, "/scene1", 20);` |
| `getEnv("name")` | De waarde van een omgevingsvariabele. | `let port = getEnv("DASLIGHT_PORT");` |
| `sleep(ms)` | Wacht een aantal milliseconden. De show wacht ook, houd het dus kort. | |
| `alert(message)` | Toon een berichtvenster. Alleen voor debuggen; het stopt de show. Gebruik in plaats daarvan `console.log()`. | `alert("hello world");` |
