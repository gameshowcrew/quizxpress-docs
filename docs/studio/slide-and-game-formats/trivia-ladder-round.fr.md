# Trivia Ladder round

Un Trivia Ladder round vous permet de créer une manche de style ‘Qui veut gagner des millions®’ (‘Who Wants to Be a Millionaire®’) dans laquelle un ou plusieurs joueurs essaient de grimper une échelle en répondant correctement aux questions.

![](../../assets/images/image72.webp){ width="570" loading=lazy }

Comme les diapositives de quiz classiques, un Trivia Ladder peut être entièrement stylisé (veuillez consulter [Trivia Ladder properties](../user-interface-overview/advanced-properties-grid.md#proprietes-du-trivia-ladder) pour plus de détails sur toutes les options).

## Comment créer un Trivia Ladder ?

Pour créer un Trivia Ladder, commencez par insérer une diapositive Trivia Ladder dans le quiz (allez dans le menu INSERT, cliquez sur la liste déroulante de la section Quiz Slides et choisissez la mise en page Trivia Ladder). Le Trivia Ladder sera généré automatiquement à partir des questions qui la suivent.

!!! note

    contrairement à tous les autres types de diapositives, la diapositive Trivia Ladder n’est pas affichée en tant que telle pendant le quiz. Son seul but est de créer l’échelle, qui sera affichée sur chaque diapositive de la manche Trivia Ladder pendant le quiz.

Pour remplir l’échelle, créez *après* la diapositive Trivia Ladder autant de questions que vous souhaitez d’échelons. Vous voyez ci-dessous un échelon de l’échelle.

![](../../assets/images/image73.webp){ width="425" loading=lazy }

Échelon de l’échelle

Les numéros de question sont affichés à gauche de l’échelle. Les points affichés à droite du numéro de question sont définis par les points des questions correspondantes de la manche Trivia Ladder. Il est également possible d’ajouter des prix à l’échelle à la place des points. À droite de chaque échelon, les keypads qui se trouvent sur cet échelon sont affichés.

Le séparateur situé le plus à gauche (un losange) indique si la question de l’échelon a été jouée.

Ce n’est qu’à la fin, lorsque la dernière question de l’échelle est terminée, que chaque joueur (keypad) reçoit les points de l’échelon sur lequel il se trouve.

Les échelons de sécurité de l’échelle sont généralement colorés différemment (en blanc sur l’image ci-dessous, par exemple) pour indiquer sur quels échelons les joueurs retombent lorsqu’ils répondent incorrectement (si l’action en cas de mauvaise réponse (*wrong answer action*) de l’échelle est définie sur ‘Fall to safety net’).

Comme le Trivia Board, un Trivia Ladder peut être combiné avec d’autres formats de jeu QuizXpress. Pour créer un Trivia Ladder (manche), QuizXpress doit savoir où se termine une manche Trivia Ladder. Une manche Trivia Ladder se termine à l’un des types de diapositives suivants :

- une diapositive ‘End of round’ (voir aussi 3.4.3)

- une autre diapositive Trivia Ladder

- une diapositive Trivia Board

- la fin du quiz (dernière manche ou jeu composé uniquement d’un Trivia Ladder)

Les questions sans points (par exemple Audience response, Demographic, Wager) sont ignorées lors de la création du Trivia Ladder.

Vous pouvez aussi utiliser le Quiz Wizard pour créer une manche Trivia Ladder complète en quelques clics ! Lancez l’assistant (onglet HOME puis ‘Quiz Wizard’) et sélectionnez ‘create a new round’ puis ‘a Trivia Ladder round’. Renseignez ensuite les points et indiquez où se trouvent les échelons de sécurité.

![](../../assets/images/image74.webp){ width="544" loading=lazy }

Choisissez le temps de réponse, les points et le style utilisés dans les pages suivantes, puis appuyez sur ‘Finish’ pour créer l’échelle, les questions et la diapositive de fin de manche. Bien sûr, vous devrez encore saisir les questions elles-mêmes, mais les points, les échelons de sécurité et la structure de l’échelle seront déjà définis pour vous.

## Position sur le Trivia Ladder

Lorsqu’un joueur répond correctement à une question dans une manche Trivia Ladder, il monte d’un échelon. Lorsqu’une question reçoit une réponse incorrecte, voici ce qui peut se produire selon la ‘Wrong answer action’ :

- Same step – le joueur reste sur le même échelon de l’échelle.

- One step down – le joueur descend d’un échelon.

- Fall to safety net – le joueur retombe au premier échelon de sécurité rencontré.

- Back to bottom – le joueur tombe de l’échelle et doit recommencer.

## Aperçu d’un Trivia Ladder

Le Trivia Ladder tel qu’il apparaît dans QuizXpress Studio sur la diapositive Trivia Ladder ne sert qu’à la conception. En définissant les options de style du Trivia Ladder, vous déterminez son apparence (veuillez consulter [Trivia Ladder properties](../user-interface-overview/advanced-properties-grid.md#proprietes-du-trivia-ladder) pour plus de détails sur les options).

![](../../assets/images/image75.webp){ width="596" loading=lazy }

Pour prévisualiser l’échelle telle qu’elle sera affichée pendant le jeu, appuyez sur F5 (ou faites un clic droit sur l’échelle et appuyez sur ‘Preview’) et l’échelle sera générée automatiquement à partir des questions présentes dans la manche Trivia Ladder.
