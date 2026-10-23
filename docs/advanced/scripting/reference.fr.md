# Référence

Tous les gestionnaires, objets, propriétés et fonctions que les scripts peuvent utiliser. Dans l'éditeur de script, le modèle liste tous les gestionnaires et les suggestions (tapez un point ou appuyez sur Ctrl+Espace) montrent le reste.

## Gestionnaires

QuizXpress appelle ces fonctions lorsqu'elles existent dans le script d'une diapositive. Un gestionnaire non défini ne change rien.

### La diapositive

| Gestionnaire | Appelé quand… |
|---|---|
| `onLoadSlide(slide)` | La diapositive est affichée. `slide` est la [diapositive](#slide) en cours, identique à `qx.slide`. Peut être `async` pour faire un `await` sur un [`fetch()`](#fonctions-globales) : QuizXpress Live l'attend avant d'afficher la diapositive. |
| `onUnloadSlide(slide)` | La diapositive est sur le point d'être quittée, pour une raison quelconque : suivante, précédente ou saut depuis le Director. Nettoyez ici, par exemple arrêtez la musique que vous avez lancée. |

### Le compte à rebours

| Gestionnaire | Appelé quand… |
|---|---|
| `onStartCountdown()` | Le compte à rebours démarre, ou reprend après une pause. |
| `onCountdownTick(secondsLeft)` | Chaque seconde du compte à rebours. `secondsLeft` est le nombre affiché sur l'horloge. |
| `onEndCountdown(isPaused)` | Le compte à rebours s'arrête. `isPaused` vaut `true` si le compte à rebours a été mis en pause, `false` s'il s'est terminé. |
| `onTimeout()` | Le temps pour répondre est écoulé. Voir [la fin d'une question](working-with-quizxpress.md#reagir-au-show). |

### Les réponses

| Gestionnaire | Appelé quand… |
|---|---|
| `onVote(player, answer, isCorrect)` | Une équipe a répondu avec le keypad (choix multiple, vote). `answer` est la réponse telle qu'elle figure sur le keypad, comme `'A'`. `isCorrect` vaut `false` lorsque la réponse est fausse ou que la diapositive n'a pas de bonne réponse. Également appelé lorsqu'une équipe change sa réponse. |
| `onFastestFinger(player)` | Une équipe a appuyé la première lors d'une question de doigt le plus rapide. |
| `onCorrectAnswer(player)` | La réponse de l'équipe la plus rapide a été jugée correcte. |
| `onIncorrectAnswer(player)` | La réponse de l'équipe la plus rapide a été jugée fausse. |
| `onScoreChanged(player, oldScore, newScore)` | Le score d'une équipe a changé. |

`player` est un [joueur](#player).

### Ce qui vient ensuite

| Gestionnaire | Appelé quand… |
|---|---|
| `onCommandNext()` | La commande 'next' est donnée (bouton, touche ou télécommande). Renvoyez `true` si le script a géré la commande et que QuizXpress doit l'ignorer ; renvoyez `false` pour laisser QuizXpress la gérer comme d'habitude. |
| `onNextSlide(currentSlideNumber)` | QuizXpress est sur le point de passer à la diapositive suivante, et la diapositive n'a pas de 'Next slide' défini. Renvoyez la diapositive à afficher : un nombre (le numéro de la diapositive, à partir de 0), une chaîne avec l'id de la diapositive (par exemple `'#final'`), ou une diapositive de `qx.slides`. Ne renvoyez rien pour passer à la diapositive suivante. |

## qx

L'objet global `qx` est le point d'entrée vers QuizXpress.

| Nom | Description | Exemple |
|---|---|---|
| `qx.slide` | La [diapositive](#slide) en cours. | `let notes = qx.slide.notes;` |
| `qx.slides` | Toutes les diapositives du quiz. | `let final = qx.slides.find(s => s.id === 'final');` |
| `qx.teams` | Toutes les équipes, sous forme de [joueurs](#player). | `let votedA = qx.teams.filter(t => t.lastVote === 'A').length;` |
| `qx.leaderBoard` | Toutes les équipes triées par score, le leader en premier. | `let leader = qx.leaderBoard[0];` |
| `qx.roundLeaderBoard` | Les scores de la manche en cours (depuis la dernière diapositive End of Round). Chaque entrée possède `team` (un [joueur](#player)) et `roundScore`. | `let best = qx.roundLeaderBoard[0].team.name;` |
| `qx.groups` | Les noms des groupes démographiques. | |
| `qx["name"]` | Lit ou définit une valeur globale nommée, conservée d'une diapositive à l'autre et affichée sur une diapositive avec `[jsvar.name]`. | `qx["roundname"] = "Geography";` |
| `qx.utils.message(text)` | Écrit une ligne dans le fichier journal de QuizXpress Live. | |
| `qx.sink` | QuizXpress Live lui-même, voir [qx.sink](#qxsink). | `let player = qx.sink.playerFromDevice(10);` |

## slide

La diapositive en cours (`qx.slide`, ou l'argument `slide` d'un gestionnaire), et les diapositives de `qx.slides`.

| Nom | Description |
|---|---|
| `slide.slideType` | Le type de diapositive, voir [SlideType](#slidetype). |
| `slide.slideNumber` | Le numéro de la diapositive, à partir de 0. |
| `slide.question` | Le texte de la question. |
| `slide.answers` | Tableau avec les textes de toutes les réponses. |
| `slide.correctAnswer` | La bonne réponse. |
| `slide.notes` | Les notes de la diapositive. |
| `slide.category` | La catégorie (thème) de la diapositive. |
| `slide.hasVideo` | `true` si la diapositive contient une vidéo. |
| `slide.hasAudio` | `true` si la diapositive contient de l'audio. |
| `slide.isPictureQuestion` | `true` s'il s'agit d'une question image. |
| `slide.answerTime` | Le temps du compte à rebours en secondes. |
| `slide.pointsAtStart` | Points au début de la question. |
| `slide.pointsAtEnd` | Points à la fin de la question. |
| `slide.penaltyPointsAtStart` | Points de pénalité (mauvaise réponse) au début. |
| `slide.penaltyPointsAtEnd` | Points de pénalité à la fin. |
| `slide.id` | L'id de la diapositive (section 'Metadata' des propriétés de la diapositive). |
| `slide.class` | La classe de la diapositive (section 'Metadata' des propriétés de la diapositive). |
| `slide["fieldName"]` | Lit un [champ de diapositive personnalisé](../custom-data-fields.md), par exemple `slide["DasLightScene"]`. |
| `slide.setQuestion(text)` | Remplace le texte de la question, pour ce show uniquement. |
| `slide.setAnswers(answers)` | Remplace les réponses dans l'ordre (A, B, C…), pour ce show uniquement. Au maximum autant de réponses que la diapositive en possède. |
| `slide.setCorrectAnswer(letters)` | Définit la bonne réponse : `'B'`, ou `'AC'` lorsque plusieurs réponses sont correctes. Pour ce show uniquement. |

Voir [Modifier la question](working-with-quizxpress.md#modifier-la-question).

### SlideType

Le `SlideType` global donne les types de diapositive par nom :

```javascript
if (slide.slideType === SlideType.Question) {
    console.log("It's a question!");
}
```

`SlideType.Question`, `TestQuestion`, `Banner` (billboard), `EndOfRound`, `Demographic`, `LastManStanding`, `AudienceResponse`, `Wager`, `Minigame`, `MajorityRules`, `JeopardyRound` (manche Trivia Board), `TriviaLadderRound`, `BingoRound`, `TriviaFeud`, `SpeedRound`, `PairingQuestion`.

## player

Les objets de `qx.teams` et `qx.leaderBoard`, l'argument `player` des gestionnaires, et ceux renvoyés par `playerFromDevice` et `winnerOfLastQuestion`.

| Nom | Description |
|---|---|
| `player.name` | Lit ou définit le nom du joueur. |
| `player.group` | Le groupe démographique du joueur. |
| `player.lastVote` | La dernière réponse reçue, comme `'A'`. |
| `player.keypad` | Le numéro de keypad du joueur. |
| `player.score` | Lit ou définit le score actuel. Voir [Modifier les scores](working-with-quizxpress.md#modifier-les-scores). |
| `player.excluded` | Lit ou définit si le joueur est exclu. |
| `player.timeUsed` | Temps utilisé (nombre décimal). |
| `player.isMobilePlayer` | `true` si le joueur est connecté via un appareil mobile. |
| `player.id` | Id unique (GUID) du joueur. |

## qx.sink

| Nom | Description |
|---|---|
| `qx.sink.gotoSlide(slideNumber)` | Saute à une diapositive (numéro à partir de 0). |
| `qx.sink.endQuiz()` | Termine le quiz. |
| `qx.sink.restartQuiz()` | Redémarre le quiz. |
| `qx.sink.playerFromDevice(device)` | Le [joueur](#player) associé à un numéro d'appareil. |
| `qx.sink.winnerOfLastQuestion` | Le [joueur](#player) qui a gagné la dernière question. |
| `qx.sink.players` | Tous les joueurs. |
| `qx.sink.quizFile` | Le nom de fichier du quiz en cours. |
| `qx.sink.keypads` | Accès au sous-système des buzzers. |
| `qx.sink.sound` | Accès au [sous-système audio](#sound). |

## sound

Disponible via `qx.sink.sound`.

| Nom | Description | Exemple |
|---|---|---|
| `loadMusic(name, filename, loop)` | Charge un fichier audio depuis le disque sous un nom. | `qx.sink.sound.loadMusic("song1", "C:\\Music\\song1.mp3", false);` |
| `playMusic(name)` | Lit un son chargé, ou reprend après `pauseMusic()`. | `qx.sink.sound.playMusic("song1");` |
| `pauseMusic(name)` | Met la lecture en pause. | `qx.sink.sound.pauseMusic("song1");` |
| `stopMusic(name)` | Arrête la lecture. | `qx.sink.sound.stopMusic("song1");` |
| `unloadMusic(name)` | Décharge le son et libère ses ressources. | `qx.sink.sound.unloadMusic("song1");` |
| `setMusicVolume(name, volume)` | Règle le volume d'un son (0–100). | `qx.sink.sound.setMusicVolume("song1", 50);` |
| `setVolume(volume)` | Règle le volume de lecture (0–100). | |
| `startPlaylist(files[], volume)` | Démarre la lecture d'une liste de morceaux. | |
| `endPlaylist()` | Arrête la liste de lecture. | |
| `playBuzzerSound(keypad)` | Joue le son de buzzer d'un keypad. | |

!!! tip
    Dans les chaînes JavaScript, une barre oblique inverse doit être doublée : écrivez les chemins Windows sous la forme `"C:\\Music\\song1.mp3"`.

Arrêtez toujours dans `onUnloadSlide()` la musique que vous avez lancée : l'animateur de quiz peut quitter la diapositive à tout moment. Avec 'Test' dans Studio, les fonctions audio ne font rien.

## Fonctions globales

| Nom | Description | Exemple |
|---|---|---|
| `console.log(…)`, `console.info(…)`, `console.warn(…)`, `console.error(…)` | Écrivent dans la [console de script](debugging.md). | `console.log("Votes:", votes);` |
| `fetch(url)` | Télécharge une page web ou la réponse d'un service web. Renvoie un objet avec `status` (comme 200), `statusText` et `text`. Attend 10 secondes au maximum ; en cas d'échec, lève une erreur que vous pouvez intercepter. Voir [Questions issues du web](examples.md#questions-issues-du-web). | `let response = await fetch(url);` |
| `setTimeout(function, ms)` | Exécute une fonction une fois, après un certain nombre de millisecondes. | `setTimeout(() => console.log('later'), 2000);` |
| `setInterval(function, ms)` | Exécute une fonction de façon répétée. Renvoie un id pour `clearInterval()`. S'arrête automatiquement lorsque la diapositive est quittée. | Voir l'[exemple Horloge](examples.md#horloge). |
| `clearInterval(id)` | Arrête un `setInterval()`. | |
| `sendUDP(ip, port, message)` | Envoie un message texte en UDP (sans gestion d'erreurs). | `sendUDP("127.0.0.1", 53432, "start");` |
| `sendTCP(ip, port, message)` | Envoie un message texte en TCP. | `sendTCP("127.0.0.1", 53432, "end");` |
| `sendOSC(ip, port, oscaddress, p1, [p2])` | Envoie des données à un gestionnaire OSC. | `sendOSC("127.0.0.1", 4532, "/scene1", 20);` |
| `getEnv("name")` | La valeur d'une variable d'environnement. | `let port = getEnv("DASLIGHT_PORT");` |
| `sleep(ms)` | Attend un certain nombre de millisecondes. Le show attend aussi, alors restez bref. | |
| `alert(message)` | Affiche une boîte de message. Uniquement pour le débogage ; elle bloque le show. Utilisez plutôt `console.log()`. | `alert("hello world");` |
