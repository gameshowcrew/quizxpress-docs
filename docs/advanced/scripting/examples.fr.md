# Exemples

## Quiz d'exemple

Nos [exemples de scripts sur GitHub](https://github.com/gameshowcrew/samples/tree/main/script) sont des quiz prêts à l'emploi, chacun avec son script dans un fichier séparé et une explication. L'éditeur de script y renvoie aussi : 'Example scripts on GitHub' en haut à droite. Du plus simple au plus élaboré :

| Exemple | Ce qu'il montre | Fonctions de script |
|---|---|---|
| [Horloge en direct](https://github.com/gameshowcrew/samples/tree/main/script/live_clock) | Une horloge en direct et un compte à rebours avant le début du quiz sur une diapositive billboard | `setInterval()`, `[jsvar.name]` sur une diapositive |
| [Compteur de votes](https://github.com/gameshowcrew/samples/tree/main/script/vote_counter) | « 7 équipes sur 12 ont répondu » pendant que le compte à rebours tourne | `onVote()`, `qx.teams` |
| [Dépêchez-vous !](https://github.com/gameshowcrew/samples/tree/main/script/countdown_hurry_up) | « Dépêchez-vous ! » dans les dernières secondes, musique de tension facultative, « Temps écoulé ! » | `onCountdownTick()`, `onTimeout()`, `qx.sink.sound` |
| [Ordre des questions aléatoire](https://github.com/gameshowcrew/samples/tree/main/script/random_question_order) | 5 questions au hasard parmi un ensemble, dans un ordre aléatoire | `onNextSlide()`, valeurs conservées entre les diapositives |
| [Questions issues du web](https://github.com/gameshowcrew/samples/tree/main/script/fetching_dynamic_content) | Une nouvelle question de l'Open Trivia Database à chaque fois | `fetch()`, `slide.setQuestion()`/`setAnswers()` |
| [Bonus de série](https://github.com/gameshowcrew/samples/tree/main/script/hot_streak_bonus) | Des points bonus pour 3 bonnes réponses d'affilée, et un tableau des scores des séries | tout ce qui précède, modification des scores |

Pour en essayer un, téléchargez le fichier `.qx`, ouvrez-le dans Quiz Studio et regardez la propriété 'Script' de ses diapositives, ou lancez-le.

Les exemples ci-dessous sont de courts scripts à copier dans votre propre quiz.

## Horloge

Affiche l'heure actuelle sur une diapositive, mise à jour chaque seconde, à l'aide d'un [symbole de texte `[jsvar]`](working-with-quizxpress.md#afficher-des-valeurs-du-script-sur-une-diapositive).

Créez une diapositive billboard et remplacez le texte de la question par le symbole `[jsvar.time]` :

![Diapositive billboard avec le symbole jsvar.time](../../assets/images/js-clock-slide.webp){ loading=lazy }

Donnez ce script à la diapositive :

```javascript
function onLoadSlide(slide) {
    showTime();
    setInterval(showTime, 1000);     // appeler showTime() chaque seconde
}

function showTime() {
    qx["time"] = new Date().toLocaleTimeString();
}
```

`onLoadSlide()` affiche l'heure et démarre un minuteur qui la met à jour chaque seconde. Le minuteur s'arrête de lui-même lorsque la diapositive est quittée.

## Lire un MP3

Charge un fichier MP3 et le lit deux secondes après la fin du compte à rebours :

```javascript
qx.sink.sound.loadMusic('levels', 'C:\\Music\\Jingles\\Levels.mp3', false);

function onEndCountdown(isPaused) {
    if (isPaused)
        return;
    // démarrer après 2 secondes
    setTimeout(() => {
        qx.sink.sound.playMusic('levels');
    }, 2000);
}

function onUnloadSlide(slide) {
    qx.sink.sound.stopMusic('levels');
    qx.sink.sound.unloadMusic('levels');
}
```

## Sauter à une diapositive selon les votes

Utilise `onNextSlide()` pour continuer avec la manche A ou la manche B, selon la réponse qui a obtenu le plus de votes. La première diapositive de chaque manche a la classe de diapositive `roundA` ou `roundB`.

!!! tip
    Pour les cas simples, le [routage des diapositives](../../studio/other-functionality/slide-routing.md) intégré fait cela sans script.

```javascript
// Aller à la diapositive de classe 'roundA' ou 'roundB',
// selon la réponse qui a obtenu le plus de votes
function onNextSlide(currentSlideNumber) {
    let slides = qx.slides;
    let roundA = slides.find((slide) => slide.class === 'roundA');
    let roundB = slides.find((slide) => slide.class === 'roundB');

    if (!roundA || !roundB) {
        console.error('round A or round B not found!');
        return;     // simplement la diapositive suivante
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

## Questions issues du web

Utilise `fetch()` pour obtenir une nouvelle question de l'[Open Trivia Database](https://opentdb.com) à chaque affichage de la diapositive, et la place sur la diapositive. Donnez ce script à une diapositive à choix multiple avec 4 réponses ; ce que vous avez saisi dans Studio est utilisé lorsqu'il n'y a pas de connexion internet.

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

    // la bonne réponse à une position aléatoire
    const position = Math.floor(Math.random() * 4);
    answers.splice(position, 0, decodeURIComponent(trivia.correct_answer));

    slide.setQuestion(decodeURIComponent(trivia.question));
    slide.setAnswers(answers);
    slide.setCorrectAnswer('ABCD'[position]);

    console.log('Correct answer: ' + 'ABCD'[position]);   // pour l'animateur de quiz
}
```

QuizXpress Live attend la fin du téléchargement avant d'afficher la diapositive, 10 secondes au maximum. L'[exemple complet](https://github.com/gameshowcrew/samples/tree/main/script/fetching_dynamic_content) choisit aussi une catégorie et une difficulté, et gère les erreurs du service.

## Sélectionner une équipe au hasard

Choisit une équipe au hasard, affiche la sélection à l'écran comme une loterie, puis exclut toutes les autres équipes pour la question suivante.

Créez une diapositive avec le symbole de texte `[jsvar.selected-team]`, qui affiche la sélection au fur et à mesure :

![Diapositive avec le symbole jsvar.selected-team](../../assets/images/js-random-team-slide.webp){ loading=lazy }

Donnez ce script à la diapositive :

```javascript
function onLoadSlide(slide) {
    // s'assurer que toutes les équipes sont activées
    qx.teams.forEach((team) => {
        team.excluded = false;
    });
    qx["selected-team"] = "...";
    randomize(50);
}

function randomize(start) {
    function step(i) {
        if (i >= 0) {
            // choisir une équipe au hasard
            var randomIndex = Math.floor(Math.random() * qx.teams.length);
            var selectedTeam = qx.teams[randomIndex];

            if (i === 0) {
                // afficher le gagnant
                qx["selected-team"] = "*** " + selectedTeam.name + " ***";
                qx["playing-team"] = selectedTeam.name;

                // exclure toutes les autres équipes
                qx.teams.forEach((team) => {
                    if (team != selectedTeam)
                        team.excluded = true;
                });
            }
            else {
                // afficher cette équipe et planifier l'étape suivante
                qx["selected-team"] = selectedTeam.name;
                setTimeout(() => step(i - 1), 750 * 1 / i);
            }
        }
    }
    step(start);
}
```

La diapositive affiche un nom d'équipe 50 fois, en ralentissant au fur et à mesure, puis affiche l'équipe choisie entre `***` et exclut tous les autres joueurs pour la question suivante. Le nom de l'équipe choisie est aussi conservé dans `playing-team`, ce qui vous permet de l'afficher sur la diapositive suivante avec `[jsvar.playing-team]`.
