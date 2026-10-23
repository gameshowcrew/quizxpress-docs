# Trivia Board round

Un Trivia Board round vous permet de créer un tableau de questions de style Jeopardy® avec des thèmes et des questions de difficulté/points variables.

![](../../assets/images/image68.webp){ width="513" loading=lazy }

Comme les diapositives de quiz classiques, un trivia board peut être entièrement stylisé (veuillez consulter la section [Trivia Board properties](../user-interface-overview/advanced-properties-grid.md#proprietes-du-trivia-board) pour plus de détails sur les options).

Pendant le quiz, les questions du tableau peuvent être choisies (au clavier, à la souris ou avec la télécommande de l’animateur de quiz) ou tirées au hasard, auquel cas un sélecteur aléatoire parcourt l’écran et choisit l’une des cases.

## Comment créer un Trivia Board ?

Pour créer un trivia board, commencez par insérer une diapositive trivia board dans le quiz (allez dans le menu INSERT, cliquez sur la liste déroulante de la section Quiz Slides et choisissez la mise en page Trivia Board). Le trivia board sera généré automatiquement à partir des questions qui le suivent.

Pour classer les questions par thèmes et par points (ou par thèmes uniquement), veillez à définir les propriétés suivantes pour les questions qui suivent le trivia board :

- Le thème (topic)

- Les points

Vous pouvez saisir les deux dans l’onglet QUESTION lorsque la question est sélectionnée :

![](../../assets/images/image69.webp){ width="604" loading=lazy }

Vous pouvez aussi saisir ces propriétés dans le panneau de propriétés (s’il n’est pas visible, affichez-le d’abord en sélectionnant l’onglet VIEW et en cochant ‘Properties’).

Un Trivia Board peut être combiné avec d’autres formats de jeu QuizXpress. Pour créer un Trivia Board (manche), QuizXpress doit savoir où se termine une manche Trivia Board. Une manche Trivia Board se termine à l’un des types de diapositives suivants :

- une diapositive ‘End of round’ (voir aussi 3.4.3)

- une autre diapositive Trivia Board

- une diapositive Trivia Ladder

- la fin du quiz (dernière manche ou jeu composé uniquement d’un Trivia Board)

Pendant le quiz, toutes les diapositives d’une manche Trivia Board sont traitées et regroupées par thème. Au sein d’un thème, les questions sont regroupées par nombre de points. Ainsi, derrière chaque case de points du tableau, il peut y avoir plusieurs questions. Lorsque les questions d’une case sont épuisées, la case est grisée et ne peut plus être choisie.

Les questions sans points (par exemple Audience response, Demographic, Wager) sont ignorées lors de la création du Trivia Board.

Vous pouvez aussi utiliser le Quiz Wizard pour créer une manche Trivia Board complète en quelques clics ! Lancez l’assistant (onglet HOME puis ‘Quiz Wizard’) et sélectionnez ‘create a new round’ puis ‘a Trivia Board round’. Renseignez ensuite les thèmes, les points et les autres préférences.

![](../../assets/images/image70.webp){ width="499" loading=lazy }

Choisissez le temps de réponse, les points et le style utilisés dans les pages suivantes, puis appuyez sur ‘Finish’ pour créer le tableau, les questions et la diapositive de fin de manche. Bien sûr, vous devrez encore saisir les questions elles-mêmes, mais le thème et les points corrects seront déjà définis pour vous.

## Aperçu d’un Trivia Board

La diapositive Trivia Board dans QuizXpress Studio affiche le tableau tel qu’il apparaîtra pendant le spectacle : les vrais thèmes et valeurs de points de la manche, disposés selon vos paramètres de design (position, espacement, images et texte). En définissant les options de style du Trivia Board ainsi que l’arrière-plan, vous déterminez l’apparence du tableau.

![Une diapositive Trivia Board conçue dans Studio](../../assets/images/trivia-board-studio-slide.webp){ loading=lazy }

Pour essayer le tableau tel qu’il sera joué pendant le jeu, appuyez sur F5 et le tableau sera généré automatiquement à partir des questions présentes dans la manche Trivia Board.

## Concevoir votre propre tableau

Outre le tableau bleu classique, vous pouvez donner à un Trivia Board un design entièrement personnel : un arrière-plan thématique, des en-têtes de thèmes illustrés et vos propres cases. Quelques exemples :

![Un tableau musical avec des cases néon et des en-têtes de thèmes illustrés](../../assets/images/trivia-board-custom-music.webp){ loading=lazy }

![Un tableau sportif avec un titre en arrière-plan et des en-têtes photo](../../assets/images/trivia-board-custom-sports.webp){ loading=lazy }

![Un tableau de voyage sur une carte illustrée avec des étiquettes de thèmes colorées](../../assets/images/trivia-board-custom-world.webp){ loading=lazy }

Un design comme ceux-ci se compose de quelques images :

- **Un arrière-plan** pour la diapositive (1920 × 1080 pour un quiz en 16:9), avec tout ce qui ne change pas pendant le jeu : le décor, un titre, un cadre autour du tableau.
- **Une image par thème** pour les cases de thèmes, par exemple une illustration contenant le nom du thème, comme dans les exemples ci-dessus.
- **Une image de case** pour les cases de points, par exemple un bouton ou un coup de pinceau. Enregistrez-la au format PNG avec des coins transparents, afin que l’arrière-plan apparaisse autour de la case.

Tous les paramètres de design se trouvent sur la page 'Design' du panneau de propriétés lorsque le tableau est sélectionné. Toutes les images sont stockées dans le fichier du quiz, vous n’avez donc pas besoin de les copier avec le quiz.

![Les propriétés de design du tableau musical](../../assets/images/trivia-board-properties-custom.webp){ width="380" loading=lazy }

Le tableau musical ci-dessus, par exemple, a une position personnalisée, une hauteur de ligne de thèmes de 390 % pour les hauts en-têtes, une image de thème sur toute la case pour chaque thème avec le nom du thème désactivé (les images le contiennent déjà), un arrière-plan de case de thème transparent et une image de case pour les cases de points.

### Position du tableau

'Board position' détermine où le tableau apparaît :

- **Automatic** remplit l’écran, comme le tableau classique. Les cases utilisent alors une couleur de remplissage au lieu d’images.
- **Custom** place le tableau là où il se trouve sur la diapositive. Faites glisser et redimensionnez le tableau dans Studio pour l’ajuster au cadre de votre arrière-plan. Les paramètres d’image ci-dessous ne sont disponibles qu’avec une position personnalisée.

Sous 'Layout', vous pouvez également définir :

- **Topic row height** : la hauteur des cases de thèmes par rapport aux cases de points (par exemple 250 % pour de grands en-têtes illustrés).
- **Column spacing** et **Row spacing** : l’espace entre les cases.

### Images de cases

- **Tile image** (dans 'Topic tiles' et dans 'Question tiles') remplace la couleur de remplissage des cases par une image.
- **Image scaling** détermine comment l’image est ajustée dans une case : 'Stretch' (remplit exactement la case), 'Fit' (conserve la forme de l’image), 'Fill' (conserve la forme et coupe ce qui dépasse) ou 'Keep corners' (étire le milieu de l’image et conserve ses coins tels quels, utile pour les cases encadrées).
- **Vary tiles** reflète l’image des cases de points différemment sur chaque case, afin qu’une case avec par exemple des éclaboussures de peinture ne soit pas identique partout.

### Images de thèmes

Cliquez sur le bouton à côté de 'Topic images' pour donner à chaque thème de la manche sa propre image. La boîte de dialogue liste les thèmes des questions situées après le tableau :

![La boîte de dialogue Topic images](../../assets/images/trivia-board-topic-images-dialog.webp){ width="600" loading=lazy }


- Cliquez sur 'Choose…' pour choisir une image pour un thème, ou faites glisser un fichier image sur sa ligne.
- 'Assign from files…' attribue plusieurs images en une seule fois : chaque image est attribuée au thème portant le même nom que le fichier. Les majuscules et minuscules, les accents, les espaces, les tirets et les tirets bas n’ont pas d’importance, de sorte que `dutch-pop.png` est attribué au thème 'Dutch Pop'.
- Les images des thèmes qui ne font plus partie de la manche sont listées en bas, afin que vous puissiez les supprimer.

'Image position' place l’image du thème sur toute la case, ou à gauche, à droite ou au-dessus du nom du thème. Lorsque vos images contiennent déjà le nom du thème (comme les exemples ci-dessus), désactivez 'Show topic name'.

!!! tip
    Les images de thèmes sont associées à un thème par son nom. Lorsque vous renommez un thème dans les questions, choisissez à nouveau son image.

### Texte des cases

![Les sections Tile text et Tile states du panneau de propriétés](../../assets/images/trivia-board-properties-tile-text.webp){ width="380" loading=lazy }

- **Same text size for all tiles** : lorsque cette option est activée, tous les noms de thèmes ont la même taille de texte et toutes les valeurs de points ont la même taille de texte : la plus grande taille à laquelle chaque texte tient dans sa case, sans jamais dépasser la taille de police que vous avez définie. Les noms de thèmes longs sont répartis sur deux lignes. Lorsqu’elle est désactivée, chaque texte est agrandi autant que sa propre case le permet, de sorte que les textes courts sont plus grands que les textes longs.
- **Text effect** ajoute une ombre ou un contour autour du texte des cases, dans la couleur 'Effect color'.

### Sélection et cases jouées

- **Selection highlight** détermine comment la sélection aléatoire montre la case choisie : 'Fill' recouvre la case de la couleur de surbrillance (l’aspect classique), 'Tint' la colore en partie, 'Outline' et 'Glow' dessinent une bordure colorée et laissent l’image de votre case visible.
- **Highlight color** définit la couleur de la sélection aléatoire.
- **Played tiles** détermine l’aspect d’une case une fois ses questions jouées : 'Dimmed', 'Hidden' ou 'No text' (la case reste, sans sa valeur de points).

### Vidéo d’arrière-plan

Une diapositive Trivia Board peut également avoir une [vidéo d’arrière-plan](../backgrounds.md#video-en-arriere-plan). Elle est lue derrière le tableau avec les propres paramètres de la vidéo (boucle, silencieux, volume) et se met en pause pendant l’affichage d’une question.

!!! note
    Les anciennes versions de QuizXpress peuvent toujours ouvrir un quiz avec un tableau personnalisé, mais l’affichent comme un tableau classique.
