# Scripts

Depuis la version 8.5, QuizXpress dispose d'un moteur JavaScript intégré. Avec les scripts, vous pouvez créer des comportements et des éléments de jeu personnalisés qui ne sont pas possibles autrement. Outre tout ce que propose le langage JavaScript, un script peut lire des informations sur la diapositive en cours, les joueurs, les scores et les buzzers, réagir aux événements du quiz, modifier la question et les scores pendant le show, récupérer des données sur internet et communiquer avec d'autres équipements.

Cette section explique comment fonctionnent les scripts dans QuizXpress. Elle n'enseigne pas JavaScript lui-même : il existe beaucoup d'informations sur le web, et les assistants IA aident très bien à écrire des scripts. Des connaissances de base en programmation sont supposées. Pour savoir exactement ce que le moteur prend en charge, consultez [Jint](https://github.com/sebastienros/jint), le moteur JavaScript utilisé par QuizXpress.

!!! warning "À utiliser avec précaution"
    Les scripts s'adressent aux utilisateurs avancés et ne sont pas nécessaires pour une utilisation normale de QuizXpress. Un script peut corrompre les scores ou perturber le déroulement de votre quiz. Une erreur dans un script n'arrête jamais le show, mais la partie du script située après l'erreur ne s'exécute pas. Testez soigneusement avant d'utiliser un script dans un show en direct.

    Nous n'offrons pas de support (gratuit) pour l'écriture de scripts.

## Comment un script s'exécute

Un script appartient à une diapositive. Lorsque QuizXpress Live affiche la diapositive, il exécute le script : d'abord le code situé en dehors des fonctions, puis le gestionnaire `onLoadSlide()`. Tant que la diapositive est affichée, QuizXpress appelle les autres gestionnaires lorsque quelque chose se produit : le compte à rebours démarre, une équipe vote, le temps est écoulé… Lorsque la diapositive est quittée, `onUnloadSlide()` s'exécute et le script s'arrête. Ses variables disparaissent et ses minuteurs `setInterval()` s'arrêtent.

Pour conserver des informations d'une diapositive à la suivante, ou pour afficher une valeur sur la diapositive, utilisez l'objet `qx` : voir [Travailler avec QuizXpress](working-with-quizxpress.md).

## L'éditeur de script

Chaque diapositive possède une propriété 'Script'. Dans QuizXpress Studio, cliquez sur les trois points de la propriété 'Script' pour ouvrir l'éditeur de script. Lorsqu'une diapositive n'a pas encore de script, l'éditeur affiche un modèle qui explique les bases et liste tous les gestionnaires, mis en commentaire (affichés en vert). Supprimez le `//` devant un gestionnaire pour l'utiliser.

![L'éditeur de script avec le modèle par défaut](../../assets/images/js-script-editor-template.webp){ loading=lazy }

Les **gestionnaires** sont des fonctions portant un nom précis que QuizXpress appelle automatiquement lorsque quelque chose se produit, si elles existent dans le script. Par exemple, `onLoadSlide(slide)` s'exécute lorsque la diapositive est affichée, et `onVote(player, answer, isCorrect)` s'exécute chaque fois qu'une équipe répond. La [Référence](reference.md#gestionnaires) les liste tous.

Vous pouvez aussi placer du code en dehors des gestionnaires. Il s'exécute dès que le script est chargé, ce qui est utile pour les paramètres en tête de script et pour le chargement de la musique.

L'éditeur vous aide pendant la saisie :

- **Suggestions** : tapez un point après `qx`, `slide` ou un joueur, ou appuyez sur Ctrl+Espace, et une liste montre ce que vous pouvez utiliser, avec une brève explication. Entre les parenthèses d'une fonction, une info-bulle indique ses arguments.
- **Vérification de la syntaxe** : une faute de frappe, comme une parenthèse manquante, est soulignée d'une ligne ondulée rouge, et l'erreur est affichée à côté du bouton 'Test'. Cliquez sur l'erreur pour aller à sa ligne.
- **Console** : sous l'éditeur, la console affiche la sortie de `console.log()` et les erreurs d'une exécution de test. Voir [Test et débogage](debugging.md).
- **'Example scripts on GitHub'**, en haut à droite, ouvre notre collection de quiz d'exemple prêts à l'emploi avec leurs scripts.

Les boutons :

- **'Save'** enregistre le script dans la diapositive, et donc dans votre quiz.
- **'Test'** exécute le script comme le fait QuizXpress Live lorsqu'il affiche la diapositive : le code en dehors des fonctions, puis `onLoadSlide()`. Il s'exécute dans un bac à sable avec cette diapositive et dix équipes d'exemple, et ne touche pas à votre quiz. Les autres gestionnaires ne sont pas appelés, car il ne se passe rien dans le bac à sable.

![Test d'un script : la sortie apparaît dans la console](../../assets/images/js-test-console.webp){ loading=lazy }

## Étapes suivantes

- [Travailler avec QuizXpress](working-with-quizxpress.md) : l'objet `qx`, le partage de données entre diapositives, l'affichage de valeurs du script sur une diapositive, et la modification de la question et des scores.
- [Test et débogage](debugging.md) : la console dans Studio et dans le Director.
- [Référence](reference.md) : tous les gestionnaires, objets, propriétés et fonctions disponibles pour les scripts.
- [Exemples](examples.md) : scripts prêts à l'emploi et quiz d'exemple.
