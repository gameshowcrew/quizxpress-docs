# Travailler avec QuizXpress

## L'objet qx

QuizXpress expose ses éléments internes aux scripts via un objet global appelé `qx`. Par exemple, `qx.slide` renvoie la diapositive en cours, et la diapositive possède à son tour des propriétés telles que `notes`. Ce script écrit les notes de la diapositive dans la console lorsque vous cliquez sur 'Test' dans Studio :

```javascript
console.log(qx.slide.notes);
```

L'éditeur vous aide à trouver les propriétés : tapez `qx.` ou `slide.` et une liste de toutes les propriétés disponibles apparaît, avec une brève explication de chacune.

![Saisie semi-automatique dans l'éditeur de script](../../assets/images/js-autocomplete.webp){ loading=lazy }

Les parties de `qx` les plus utilisées :

| | |
|---|---|
| `qx.slide` | La diapositive en cours : question, réponses, bonne réponse, points, id, classe… |
| `qx.slides` | Toutes les diapositives du quiz. |
| `qx.teams` | Toutes les équipes, avec leur nom, keypad, score et dernier vote. |
| `qx.leaderBoard` | Les équipes triées par score, le leader en premier. |
| `qx.roundLeaderBoard` | Les scores de la manche en cours. |
| `qx.sink` | QuizXpress Live lui-même : aller à une diapositive, terminer le quiz, lire de la musique… |
| `qx["name"]` | Une valeur qui reste d'une diapositive à l'autre, voir ci-dessous. |

La [Référence](reference.md) liste chaque objet, propriété et fonction avec sa signification.

## Réagir au show

Les gestionnaires sont la façon dont un script participe au show. Quelques exemples :

```javascript
// chaque seconde du compte à rebours
function onCountdownTick(secondsLeft) {
    if (secondsLeft === 10)
        qx['message'] = 'Ten seconds left!';
}

// une équipe a répondu avec son keypad
function onVote(player, answer, isCorrect) {
    console.log(player.name + ' answered ' + answer);
}

// la diapositive est quittée : nettoyer
function onUnloadSlide(slide) {
    qx.sink.sound.stopMusic('tension');
}
```

!!! note "La fin d'une question"
    Selon les paramètres de la question, QuizXpress Live appelle `onEndCountdown()` lorsque le temps est écoulé ou que tout le monde a répondu, ou uniquement `onTimeout()`. Un script qui doit faire quelque chose une seule fois à la fin d'une question gère les deux, et mémorise qu'il l'a déjà fait :

    ```javascript
    let done = false;

    function onTimeout() { endOfQuestion(); }
    function onEndCountdown(isPaused) { if (!isPaused) endOfQuestion(); }

    function endOfQuestion() {
        if (done)
            return;
        done = true;
        // ...
    }
    ```

## Partager des données entre diapositives

Les variables d'un script disparaissent lorsque sa diapositive est quittée ; les variables JavaScript ordinaires ne survivent donc pas jusqu'à la diapositive suivante. Pour conserver des données d'une diapositive à l'autre, utilisez le stockage global de l'objet `qx`.

Sur la première diapositive d'une manche, vous pourriez écrire :

```javascript
qx["roundname"] = "Movies";
```

et sur n'importe quelle diapositive ultérieure :

```javascript
let roundName = qx["roundname"];   // "Movies"
```

Les valeurs restent jusqu'à la fermeture de QuizXpress Live, y compris lorsque le quiz est redémarré. Pour repartir de zéro avec un quiz redémarré, effacez les valeurs dans le script de la première diapositive.

Pour conserver une liste ou un objet, stockez-le sous forme de texte avec `JSON.stringify()` et reconvertissez-le avec `JSON.parse()` :

```javascript
let played = JSON.parse(qx['played'] || '[]');   // une liste vide la première fois
played.push(qx.slide.slideNumber);
qx['played'] = JSON.stringify(played);
```

## Afficher des valeurs du script sur une diapositive

Vous pouvez afficher ces valeurs nommées sur une diapositive avec le symbole de texte `[jsvar.<name>]`. Ajoutez une forme de texte à la diapositive et saisissez le symbole, par exemple `[jsvar.roundname]` :

![Une forme de texte avec le symbole de texte jsvar](../../assets/images/js-jsvar-text-symbol.webp){ width="560" loading=lazy }

Définissez la variable dans le script :

![Définition de la variable dans le script](../../assets/images/js-jsvar-set-variable.webp){ width="560" loading=lazy }

Lorsque le quiz s'exécute, la diapositive affiche la valeur :

![La valeur apparaît sur la diapositive](../../assets/images/js-jsvar-result.webp){ loading=lazy }

Cela fonctionne aussi en temps réel : chaque fois que le script modifie la valeur, la diapositive affiche immédiatement la nouvelle valeur, y compris lorsqu'elle change dans un minuteur. L'[exemple Horloge](examples.md#horloge) s'en sert pour afficher l'heure actuelle.

## Modifier la question

Un script peut modifier la question, les réponses et la bonne réponse de la diapositive en cours, par exemple avec une question qu'il a téléchargée :

```javascript
function onLoadSlide(slide) {
    slide.setQuestion('What is the capital of Australia?');
    slide.setAnswers(['Sydney', 'Canberra', 'Melbourne', 'Perth']);
    slide.setCorrectAnswer('B');
}
```

- `setAnswers()` remplace les réponses dans l'ordre (A, B, C…). La diapositive doit déjà comporter ce nombre de réponses ; elle ne peut pas en ajouter.
- `setCorrectAnswer()` prend la lettre de la bonne réponse, ou plusieurs lettres (`'AC'`) lorsque plusieurs réponses sont correctes.
- Faites-le dans `onLoadSlide()`, avant l'affichage de la diapositive.

Ces modifications ne valent que pour le show : le fichier du quiz reste inchangé. Avec 'Test' dans Studio, la diapositive ne change pas non plus. Voir l'exemple [Questions issues du web](examples.md#questions-issues-du-web).

## Modifier les scores

Le score d'un joueur peut être lu et modifié :

```javascript
team.score += 50;   // 50 points bonus
```

Le bonus est ajouté au score de l'équipe. Dans Analyzer, les résultats d'une question n'affichent que les points de cette question. Sur une question de test, le score ne change pas. Voir l'exemple [Bonus de série](examples.md#quiz-dexemple).

## Choisir la diapositive suivante

`onNextSlide(currentSlideNumber)` décide quelle diapositive vient ensuite, lorsque la diapositive n'a pas de 'Next slide' défini. Renvoyez un numéro de diapositive (à partir de 0), un id de diapositive comme `'#final'`, ou une diapositive de `qx.slides`. Ne renvoyez rien pour passer simplement à la diapositive suivante.

```javascript
function onNextSlide(currentSlideNumber) {
    let leader = qx.leaderBoard[0];
    if (leader && leader.score >= 100)
        return '#final';
}
```

Donnez aux diapositives un id ou une classe dans la section 'Metadata' des propriétés de la diapositive, afin que votre script puisse les retrouver. L'exemple [Ordre des questions aléatoire](examples.md#quiz-dexemple) choisit la question suivante au hasard.
