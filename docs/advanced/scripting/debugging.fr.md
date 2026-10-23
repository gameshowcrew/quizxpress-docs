# Test et débogage

QuizXpress dispose d'une console de script, comparable à la console d'un navigateur web. Elle affiche ce que votre script écrit avec `console.log()`, ainsi que chaque erreur d'un script avec la diapositive, la ligne et la colonne où elle s'est produite.

## Écrire dans la console

```javascript
console.log('Slide ' + (slide.slideNumber + 1) + ': ' + slide.question);
console.warn('No music file set');
console.error('Something went wrong');
```

`console.log()`, `console.info()`, `console.warn()` et `console.error()` acceptent un nombre quelconque de valeurs, y compris des objets et des tableaux. Les avertissements et les erreurs sont comptés séparément, afin qu'ils ressortent.

!!! tip
    Utilisez `console.log()` plutôt que `alert()`. `alert()` affiche une boîte de message qui bloque tout le quiz tant que personne ne la ferme.

## Dans Quiz Studio

La console se trouve sous l'éditeur de script. Cliquez sur 'Test' pour exécuter le script : sa sortie apparaît dans la console, suivie de 'Test run finished'. Lorsque le script échoue, la console affiche l'erreur et l'éditeur marque la ligne. Double-cliquez sur un message pour accéder à sa ligne dans le script.

- 'Clear' vide la console, 'Copy' copie tous les messages, par exemple pour demander de l'aide à un assistant IA.
- 'Errors' et 'Warnings' indiquent leur nombre.
- Les messages qui se répètent, par exemple ceux d'un minuteur, sont regroupés en une seule ligne avec un compteur.

## Pendant un show

Une erreur de script n'arrête jamais le show : QuizXpress la signale et continue. La console de script de QuizXpress Director montre ce que les scripts ont fait. Elle n'est jamais affichée sur l'écran projeté.

Dès qu'un script écrit dans la console ou échoue, le Director affiche un bouton 'Script' parmi les boutons de commande, avec le nombre d'erreurs. Cliquez sur ce bouton pour ouvrir la console de script.

La visibilité de la console est une option. Faites un clic droit sur les boutons de commande du Director et choisissez 'Script errors' :

| Option | Effet |
|---|---|
| 'Automatic (open the console when testing from Quiz Studio)' | Lorsque vous testez le quiz depuis Quiz Studio, la console s'ouvre à la première erreur. Dans un vrai show, vous n'obtenez que le bouton. C'est la valeur par défaut. |
| 'Show a button with the number of errors' | Uniquement le bouton. |
| 'Open the console on the first error' | La console s'ouvre à la première erreur, y compris dans un vrai show. |
| 'Do not show' | Ni bouton ni console. |

'Open script console' dans le même menu ouvre la console à tout moment.

!!! tip
    La console est aussi un bon endroit pour des informations destinées à l'animateur de quiz. L'exemple [Questions issues du web](examples.md#questions-issues-du-web) écrit dans la console la question qu'il a téléchargée, avec la bonne réponse marquée.
